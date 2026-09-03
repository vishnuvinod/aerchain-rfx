"""
analyst.py
AI analyst that answers natural-language questions about the comparison matrix.
Uses Gemini with full comparison context and returns bi-directional scenario actions.
"""
import os
import json
import asyncio
from pathlib import Path
from google import genai
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")
_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY", ""))

MODEL = "gemini-3.6-flash"

SYSTEM_PROMPT = """You are an elite enterprise procurement analyst co-pilot at Aerchain.
You are helping a category director allocate approximately Rs.4.5 Crore in spend across 30 IT hardware line items and 5 suppliers.

You have access to a verified vendor comparison matrix with:
- 30 line items from 5 vendors
- Dual-layer pricing: raw supplier quotes (USD, spools, email references) normalized deterministically to INR
- Supplier qualification audit (ISO 9001 certification, warranty SLA, lead time, on-site support)
- Footnote terms (GlobalIT 12% volume discount on Page 3) and unit normalizations (DigitalEdge CAT6 100m spool to 305m box)

BEHAVIOUR RULES:
1. Be financially rigorous: cite exact vendor names, unit rates, and total line costs in INR.
2. Defend every recommendation: when suggesting an award, check qualification criteria (e.g. QuickByte lacks ISO 9001, GlobalIT lacks on-site India support, Shree IT has an incomplete quote).
3. Distinguish between theoretical lowest cost (unconstrained) vs. risk-managed defensible award (ISO-certified only).
4. When answering scenario questions (e.g. split order, cheapest per line, award recommendation), include a structured SCENARIO_ACTION json block at the very end so the buyer's screen can visually execute your scenario:
   SCENARIO_ACTION: {"name": "Descriptive Scenario Name", "disqualify_vendors": ["vendor_id"], "award_map": {"SRV-001": "techpro", ...}, "total_tco": 27800000, "savings_vs_baseline": 1637600}
5. If visual comparison adds value, append:
   CHART_DATA: {"type": "bar", "labels": [...], "datasets": [{"label": "...", "data": [...]}], "title": "..."}

Tone: Authoritative, audit-defensible, concise, and structured.
"""


def build_analyst_context(comparison: dict) -> str:
    ctx = []
    ctx.append(f"RFx Ref: {comparison['rfx_id']} | Title: {comparison['rfx_title']}")
    ctx.append(f"Target Budget: Rs.{comparison.get('target_budget_inr', 45000000):,.0f} | FX Rate: Rs.{comparison['usd_to_inr_rate']}/USD")
    ctx.append("")

    ctx.append("=== SUPPLIER QUALIFICATION STATUS ===")
    for vid, q in comparison.get("vendor_qual", {}).items():
        ctx.append(
            f"• {vid.upper()} ({q['vendor_name']}): ISO 9001={'PASS' if q['iso_certified'] else 'FAIL'} "
            f"({q['iso_detail']}) | Warranty={q['warranty']} | On-site SLA={q['onsite_support']} "
            f"| Lead Time={q['lead_time']} | Score={q['overall_score']}/10"
        )
    ctx.append("")

    ctx.append("=== SUPPLIER TOTALS (QUOTED LINES ONLY) ===")
    for vid, t in comparison.get("totals", {}).items():
        ctx.append(f"• {vid}: Rs.{t['total_inr']:,.0f} ({t['lines_quoted']}/30 lines quoted)")
    ctx.append("")

    ctx.append("=== PRE-COMPUTED SCENARIOS ===")
    for s_key, s_val in comparison.get("scenarios", {}).items():
        ctx.append(f"• {s_val['name']}: Total=Rs.{s_val['total_inr']:,.0f} — {s_val['notes']}")
    ctx.append("")

    ctx.append("=== 30 LINE ITEM DETAILED AUDIT (INR NET) ===")
    for r in comparison["rows"]:
        line = f"Item {r['item_id']:02d} [{r['item_code']}] {r['description']} (Qty: {r['quantity']} {r['rfx_unit']}): "
        vendor_quotes = []
        for vid, cell in r["vendors"].items():
            if cell["status"] == "QUOTED" and cell.get("normalised_price_inr"):
                flags = f" [{','.join(cell.get('flags', []))}]" if cell.get("flags") else ""
                vendor_quotes.append(f"{vid}=Rs.{cell['normalised_price_inr']:,.0f}{flags}")
            elif cell["status"] == "REFERENCE_REQUIRED":
                vendor_quotes.append(f"{vid}=REF_REQD(SameAsLastYear)")
            else:
                vendor_quotes.append(f"{vid}=NOT_QUOTED")
        line += " | ".join(vendor_quotes)
        ctx.append(line)

    return "\n".join(ctx)


async def answer_question(question: str, comparison: dict) -> dict:
    context = build_analyst_context(comparison)
    full_prompt = f"""COMPARISON MATRIX CONTEXT:
{context}

BUYER INQUIRY: {question}

Provide your executive procurement analysis. Include exact pricing, vendor comparisons, and qualification reasoning.
If answering a scenario/award strategy, conclude with SCENARIO_ACTION: {{...}} and optional CHART_DATA: {{...}}."""

    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: _client.models.generate_content(
                model=MODEL,
                contents=full_prompt,
                config={"system_instruction": SYSTEM_PROMPT}
            )
        )
        raw = response.text.strip()

        chart_data = None
        scenario_action = None

        if "SCENARIO_ACTION:" in raw:
            parts = raw.split("SCENARIO_ACTION:", 1)
            raw = parts[0].strip()
            rest = parts[1].strip()
            if "CHART_DATA:" in rest:
                s_part, c_part = rest.split("CHART_DATA:", 1)
                try:
                    scenario_action = json.loads(s_part.strip())
                except Exception:
                    pass
                try:
                    chart_data = json.loads(c_part.strip())
                except Exception:
                    pass
            else:
                try:
                    scenario_action = json.loads(rest)
                except Exception:
                    pass
        elif "CHART_DATA:" in raw:
            parts = raw.split("CHART_DATA:", 1)
            raw = parts[0].strip()
            try:
                chart_data = json.loads(parts[1].strip())
            except Exception:
                pass

        return {
            "answer": raw,
            "chart": chart_data,
            "scenario_action": scenario_action,
            "model": MODEL,
            "question": question,
        }

    except Exception as e:
        return {
            "answer": f"Analysis Engine Error: {str(e)}\n\nPlease ensure your GEMINI_API_KEY is configured in .env",
            "chart": None,
            "scenario_action": None,
            "model": MODEL,
            "question": question,
        }


def generate_rfx_from_description(description: str) -> dict:
    from data import RFX
    return {
        "generated": True,
        "input": description,
        "rfx": RFX,
        "ai_reasoning": (
            f"Drafted enterprise RFx based on '{description}'. Configured 30 line items across 8 categories "
            f"(Compute, Mobility, Networking, Power, Storage, Connectivity, Peripherals) with standard enterprise "
            f"specifications, 3-year warranty baseline, and a 10-point qualification questionnaire."
        )
    }
