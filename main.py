"""
main.py — Aerchain RFx System
FastAPI backend serving:
  - Static HTML frontend
  - REST API for RFx, extraction, comparison, AI analyst
"""
import os
import json
import asyncio
from pathlib import Path
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

BASE = Path(__file__).parent
EXTRACTED_DIR = BASE / "data" / "extracted"
EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Aerchain RFx System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE / "static")), name="static")

# ── Pydantic models ───────────────────────────────────────────────────────────
class GenerateRFxRequest(BaseModel):
    description: str

class AnalystRequest(BaseModel):
    question: str

class ExtractRequest(BaseModel):
    vendor_id: str
    force_rerun: bool = False

# ── Cached comparison (rebuilt when extraction changes) ───────────────────────
_comparison_cache = None
_extraction_status = {}  # vendor_id -> "pending"|"extracting"|"done"|"error"


def _load_comparison():
    global _comparison_cache
    from comparison import build_comparison
    _comparison_cache = build_comparison()
    return _comparison_cache


# ── Routes ────────────────────────────────────────────────────────────────────
@app.get("/")
async def root():
    return FileResponse(str(BASE / "static" / "index.html"))

@app.get("/api/rfx")
async def get_rfx():
    from data import RFX
    return RFX

@app.get("/api/vendors")
async def get_vendors():
    from data import VENDORS
    statuses = {}
    for v in VENDORS:
        cache = EXTRACTED_DIR / f"{v['id']}.json"
        statuses[v["id"]] = "done" if cache.exists() else _extraction_status.get(v["id"], "pending")
    return [{"status": statuses[v["id"]], **v} for v in VENDORS]

@app.post("/api/rfx/generate")
async def generate_rfx(req: GenerateRFxRequest):
    from analyst import generate_rfx_from_description
    result = generate_rfx_from_description(req.description)
    return result

@app.post("/api/extract/{vendor_id}")
async def trigger_extraction(vendor_id: str, background_tasks: BackgroundTasks, force: bool = False):
    """Trigger extraction for a single vendor (runs in background)."""
    from data import VENDORS
    vendor = next((v for v in VENDORS if v["id"] == vendor_id), None)
    if not vendor:
        raise HTTPException(404, f"Vendor {vendor_id} not found")

    if _extraction_status.get(vendor_id) == "extracting":
        return {"status": "already_running", "vendor_id": vendor_id}

    _extraction_status[vendor_id] = "extracting"

    async def do_extract():
        global _comparison_cache
        try:
            from extractor import extract_vendor
            extract_vendor(vendor_id, vendor["name"], vendor["response_file"], force_rerun=force)
            _extraction_status[vendor_id] = "done"
            _comparison_cache = None  # invalidate cache
        except Exception as e:
            _extraction_status[vendor_id] = f"error: {str(e)[:100]}"

    background_tasks.add_task(do_extract)
    return {"status": "started", "vendor_id": vendor_id}

@app.post("/api/extract-all")
async def trigger_all_extraction(background_tasks: BackgroundTasks, force: bool = False):
    """Trigger extraction for all vendors."""
    from data import VENDORS

    async def do_extract_all():
        global _comparison_cache
        for vendor in VENDORS:
            vid = vendor["id"]
            _extraction_status[vid] = "extracting"
            try:
                from extractor import extract_vendor
                extract_vendor(vid, vendor["name"], vendor["response_file"], force_rerun=force)
                _extraction_status[vid] = "done"
            except Exception as e:
                _extraction_status[vid] = f"error: {str(e)[:100]}"
        _comparison_cache = None  # invalidate cache

    background_tasks.add_task(do_extract_all)
    return {"status": "started", "vendors": [v["id"] for v in VENDORS]}

@app.get("/api/extraction-status")
async def extraction_status():
    from data import VENDORS
    result = {}
    for v in VENDORS:
        cache = EXTRACTED_DIR / f"{v['id']}.json"
        if cache.exists() and _extraction_status.get(v["id"]) != "extracting":
            result[v["id"]] = "done"
        else:
            result[v["id"]] = _extraction_status.get(v["id"], "pending")
    return result

@app.get("/api/extracted/{vendor_id}")
async def get_extracted(vendor_id: str):
    cache = EXTRACTED_DIR / f"{vendor_id}.json"
    if not cache.exists():
        raise HTTPException(404, "Not yet extracted")
    return json.loads(cache.read_text())

@app.get("/api/comparison")
async def get_comparison():
    global _comparison_cache
    if _comparison_cache is None:
        _comparison_cache = _load_comparison()
    if "error" in _comparison_cache:
        raise HTTPException(400, _comparison_cache["error"])
    return _comparison_cache

@app.post("/api/analyst")
async def analyst_query(req: AnalystRequest):
    from analyst import answer_question
    global _comparison_cache
    if _comparison_cache is None:
        _comparison_cache = _load_comparison()
    if "error" in _comparison_cache:
        raise HTTPException(400, "Run extraction first before using the analyst.")
    result = await answer_question(req.question, _comparison_cache)
    return result

@app.get("/api/questionnaire")
async def get_questionnaire():
    from data import RFX, QUESTIONNAIRE_RESPONSES, VENDORS
    result = {}
    for vendor in VENDORS:
        vid = vendor["id"]
        q = QUESTIONNAIRE_RESPONSES.get(vid, {})
        result[vid] = {
            "vendor_name": vendor["name"],
            "responses": [
                {
                    "question_id": qid,
                    "question": next((rq["question"] for rq in RFX["questionnaire"] if rq["id"] == qid), ""),
                    "answer": r.get("answer", "Not answered"),
                    "pass": r.get("pass", False),
                    "flag": r.get("flag"),
                    "detail": r.get("detail"),
                }
                for qid, r in q.items()
            ],
            "score": sum(1 for r in q.values() if r.get("pass")),
            "total": len(q),
        }
    return result

@app.get("/api/health")
async def health():
    api_key = os.getenv("GEMINI_API_KEY", "")
    key_ok = bool(api_key and len(api_key) > 10)
    extracted_count = len(list(EXTRACTED_DIR.glob("*.json")))
    return {
        "status": "ok",
        "api_key_configured": key_ok,
        "api_key_prefix": api_key[:8] + "..." if key_ok else "NOT SET",
        "vendors_extracted": extracted_count,
        "vendor_files_exist": len(list((BASE / "data" / "vendor_responses").glob("*"))),
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
