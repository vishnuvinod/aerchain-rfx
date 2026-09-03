# Aerchain RFx Intelligence System

> **Aerchain Product Management Take-Home Assignment**
> Kill the Quote Spreadsheet — Build the system that drafts an RFx, reads whatever vendors send back, and lets a buyer interrogate the result in plain language.

## Quick Start

```bash
# 1. Install dependencies
pip3 install -r requirements.txt

# 2. Create vendor response files (Excel, PDF, Word, Image, Email)
python3 create_vendor_files.py

# 3. Start the app
python3 main.py

# 4. Open in browser
open http://localhost:8000
```

## What It Does

| Feature | Detail |
|---|---|
| **RFx Builder** | AI co-pilot drafts RFx from plain-language description (30 line items, questionnaire, terms) |
| **Vendor Inbox** | 5 vendor responses in 5 formats (Excel, PDF, Word, Image, Email text) |
| **AI Extraction** | Gemini 1.5 Pro reads every format including angled phone photos |
| **Comparison Table** | Normalised to same units + currency, colour-coded, source-attributed |
| **AI Analyst** | Natural language Q&A over real extracted data — no hardcoded answers |

## The 5 Vendors & Their Edge Cases

| Vendor | Format | Edge Case |
|---|---|---|
| TechPro Solutions | Excel | Quotes 27/30 lines (3 items missing) |
| GlobalIT Supplies | PDF | All prices in USD · 12% discount buried in footnote (page 3) |
| QuickByte India | Word | Prices in paragraph prose · Not ISO certified |
| DigitalEdge Corp | Angled photo | Unit mismatch: CAT6 per 100m ≠ per box (305m) |
| Shree IT Traders | Email | Partial · "Same as last year" for 3 items · Incomplete questionnaire |

## Project Structure

```
aerchain-rfx/
├── main.py                 # FastAPI backend
├── data.py                 # RFx data + vendor pricing truth
├── extractor.py            # Gemini extraction (all formats)
├── comparison.py           # Normalise + build matrix
├── analyst.py              # AI analyst (Gemini Q&A)
├── create_vendor_files.py  # Generate vendor response files
├── static/index.html       # Single-page frontend
├── data/
│   ├── vendor_responses/   # Raw vendor files
│   └── extracted/          # Cached JSON per vendor
└── requirements.txt
```

## Trust Features

- **Source attribution** on every price cell ("Excel Sheet1, Row 4")
- **Confidence scores** (0–100%) per extracted value
- **Explicit uncertainty** — AI says "I'm not sure" rather than guessing
- **Flags** on every anomaly: UNIT_MISMATCH, CURRENCY_CONVERSION_NEEDED, EOL_WARNING, DISCOUNT_APPLIED
- **Audit trail** — cached extraction JSON viewable per vendor

## Demo Script

1. **Build RFx** → type "IT hardware for 200-seat office" → AI generates full RFx
2. **Vendor Inbox** → show 5 formats, click "Process All Responses"
3. **Comparison Table** → colour-coded grid, click any cell for source detail
4. **AI Analyst** → ask:
   - "Which vendor gives the lowest total cost?"
   - "What if I take cheapest per line item?"
   - "Show only ISO certified vendors"
   - "DigitalEdge responded via photo — what should I verify?"
   - "Shree said same as last year for RAM — can I use that price?"
