# Aerchain Product Architecture Memo
**Module:** RFx Intelligence & Autonomous Quotation Ingestion  
**Candidate:** Vishnu Vinod  
**Target Role:** Product Management (Module Ownership)  
**Deliverable:** 1-Page Design Decision Note & System Thesis  

---

## 1. Executive Summary & Problem Framing

Enterprise procurement teams managing ₹100Cr+ in spend waste 4–5 business days per RFx manually transcribing unstructured vendor bids into comparison spreadsheets. But the true operational bottleneck is **Decision Defensibility Under Fire**:
- Submissions arrive across incompatible shapes: raw unformatted Excel, scanned PDFs with footnote discounts, conversational Word docs, smartphone photos of rate cards, and informal emails.
- When an executive asks: *"What if we split the order by cheapest line, but only among suppliers who passed our warranty and quality audit?"*, the buyer loses another 24 hours rebuilding formulas.

We designed and built an **Enterprise Decision Cockpit** that deletes this cycle: **Zero-Template Ingestion $\rightarrow$ Dual-Layer Normalization $\rightarrow$ Sticky Qualification Gatekeeping $\rightarrow$ Bi-Directional Co-Pilot Simulation.**

---

## 2. Core Architectural & Design Decisions

### Rank 1: Dual-Layer Cell Architecture & Audit Traceability
* **The Problem:** Ingesting foreign currencies (USD) or non-standard spools (100m vs 305m box) and converting them silently behind the scenes makes buyers skeptical (*"Where did ₹77,154 come from when the vendor's PDF says $1,050?"*).
* **Our Design:** Every cell displays both layers simultaneously:
  - **Top layer:** The supplier’s raw stated quote (`$1,050.00 list` or `₹2,680 / 100m`).
  - **Bottom layer:** The bold normalized INR value (`₹77,154 net` or `₹8,174 / box`).
  - Mathematical transparency: Clicking any cell exposes the exact formula:
    $$\text{Raw: } \$1,050 \times \text{FX: } 83.50 = ₹87,675 \xrightarrow{-12\% \text{ Footnote Discount}} ₹77,154$$

### Rank 2: Interactive Verification & Human-in-the-Loop (HITL) Drawer
* **The Problem:** Naive AI automation either guesses blindly or fails passively on ugly edges (like DigitalEdge's angled phone photo).
* **Our Design:** When a cell has low extraction certainty or unit mismatches, it raises an amber `⚑ Review Spool` badge. Clicking opens a slide-over panel featuring:
  1. **Visual Evidence Crop:** An inline view of the actual smartphone photo of the rate card or the PDF footnote.
  2. **Audit Action Triad:**
     - `[ ✓ Accept Conversion ]`: Marks the cell `VERIFIED_BY_BUYER` and turns the border green.
     - `[ ✎ Override Price ]`: Inline rate editing that recalculates row and column totals in real time.
     - `[ ✉ Draft Clarification Email ]`: One-click pre-drafted inquiry to the vendor requesting packaging confirmation.

### Rank 3: The Sticky Qualification Banner (The Commercial Gatekeeper)
* **The Problem:** Price comparisons without compliance context lead to catastrophic awards. QuickByte offers cheap desktops, but lacks ISO 9001 and provides only 6 months warranty.
* **Our Design:** Positioned directly above commercial lines, an interactive Risk Audit banner tracks ISO certification, on-site SLA, lead times, and overall scores. Buyers can toggle `Strict ISO 9001:2015 Only` or `Min 3-Year On-Site SLA`, which dynamically dims non-compliant supplier columns (opacity: 0.28) with a red `DISQUALIFIED` strike-through.

### Rank 4: Split-View Cockpit with Bi-Directional Highlighting
* **The Problem:** Isolated chat tabs disconnect the buyer from the data grid.
* **Our Design:** A unified cockpit (65% comparison matrix, 35% collapsible Co-Pilot). When the buyer queries: *"Show cheapest split award for vendors who cleared quality"*:
  - The Co-Pilot delivers the executive justification and TCO delta.
  - The matrix **visually reacts**: winning cells light up with emerald green `AWARDED` badges, disqualified vendors dim out, and the bottom aggregate bar calculates:
    $$\text{Total Landed TCO: ₹2.84 Cr } (\text{Savings: ₹10.3 Lakhs vs. TechPro Baseline})$$

### Rank 5: "Same as Last Year" ERP Master Resolution
* **The Problem:** Shree IT’s informal email quoted *"same as last year"* for key items. Showing a dead-end error breaks the workflow.
* **Our Design:** The system recognizes the prior contract reference (`PO-2023-088`), surfaces an inline `[ ⚡ Fetch from ERP: ₹19,000 ]` button, and allows the buyer to inject historical rates into the comparison with full audit tags.

---

## 3. What We Deliberately Left Out (and Why)

| What We Omitted | Strategic Rationale |
|---|---|
| **Forced Vendor Portal Logins** | Enterprise suppliers resist logging into bespoke buyer portals. Adoption collapses. Letting vendors reply in *their* native format maximizes response rate. |
| **Autonomous PO Execution** | Full autonomous PO dispatch at ₹4 Crore spend introduces legal exposure. The system recommends and defends; the category director signs. |
| **LLM-Based Calculations** | LLMs are non-deterministic and hallucinate math. We restricted LLMs strictly to document extraction and natural language synthesis, executing 100% of mathematical conversions and aggregations in deterministic code. |

---

## 4. "Where the Better Problem Actually Is" (The $25M ARR Thesis)

> *"If you finish this and think 'the interesting problem was actually somewhere else' — tell us that too."*

While autonomous quote extraction saves 3 days of grunt work, **the real multi-million dollar bleed in enterprise spend isn't quote transcription—it is Post-Award Contract Drift & Supplier Commitment Variance.**

### The Strategic Enterprise Pain Points:
1. **The "Quote vs. Invoice Drift" Gap:**
   - Suppliers bid aggressively low to win the RFx, then claw back margin through freight add-ons, delay penalties, and specification downgrades during fulfillment.
   - **The Product Evolution:** An automated closed-loop bridge connecting quote extraction directly to three-way invoice matching in SAP/Oracle ERP, flagging invoice line creep against original RFx promises.
2. **Dynamic Vendor Trust Graph:**
   - Move from static questionnaire checkboxes to continuous **Reliability Scoring**: historical on-time in-full (OTIF) delivery, RMA defect rates, and pricing variance over multi-year cycles.
3. **Autonomous Multi-Vendor Counter-Offers:**
   - The engine should autonomously generate data-driven negotiation letters: *"Supplier B, we will award you the full ₹1.8 Cr storage package if you match Supplier A's 3-year on-site SLA."*
