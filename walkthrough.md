# Aerchain RFx Intelligence Cockpit — Loom Video Presentation Script

This is your step-by-step, minute-by-minute speaking script for your **5-minute Loom walkthrough video**. It walks the Aerchain hiring team through your build using the exact vocabulary and judgment of a Senior Product Manager.

---

## 🎬 5-Minute Loom Recording Flow

### 0:00 – 0:45: The Problem & Product Thesis
> *"Hi Aerchain team, I'm Vishnu Vinod. Today I'm demonstrating my build for 'Kill the Quote Spreadsheet'.*
>
> *In enterprise procurement, comparing quotes isn't just about data entry speed—it is about **Defensibility Under Fire**. When a buyer manages a ₹4.5 Crore spend across 30 line items, suppliers send messy, incompatible files: unformatted Excel sheets, PDFs with buried footnote discounts, conversational Word docs, and even angled smartphone photos of paper rate cards.*
>
> *We designed an **Enterprise Decision Cockpit** that solves this through 4 core principles: Zero-Template Ingestion, Dual-Layer Traceability, Sticky Qualification Gatekeeping, and Bi-Directional Co-Pilot Simulation."*

---

### 0:45 – 1:30: The Commercial Grid & Dual-Layer Traceability
1. **Show the Main Screen ([http://localhost:8000](http://localhost:8000)):**
   - *"Notice our layout: on the left (65%), we have the Normalized Comparison Matrix. On the right (35%), an interactive Procurement Co-Pilot."*
2. **Point out the Sticky Qualification Banner:**
   - *"Before looking at a single price, we enforce a Supplier Risk Audit across ISO 9001 certification, warranty, on-site SLAs, and historical ERP invoice drift.*
   - **Click the toggle:** *"Notice what happens when I toggle `Strict ISO 9001 Only`—QuickByte (who lacks ISO certification) is instantly disqualified, and their column dims with a high-contrast red badge."*
3. **Show the Dual-Layer Cell Architecture & Smart Rollup Lots:**
   - Point to GlobalIT's Laptop row (Row 5):
     - *"Notice how we display prices: bold normalized INR rate (`₹77,154 net`) on top, with the supplier's raw stated quote (`$1,050 list in USD · -12% footnote discount`) right below. The buyer never has to guess where a number came from."*
   - **Show the Smart Rollup Accordions:**
     - Click **`[ ⊟ Collapse All ]`** in the top ribbon: *"Notice how the matrix collapses into an Executive Category Scorecard—showing the benchmark spend and lowest compliant vendor for each of the 5 Lots without hiding commercial intelligence."*
     - Click **`[ ⊞ Expand All ]`** to expand back to the full 30-line audit view.

---

### 1:30 – 2:30: The Ugly Edges & The Slide-Over Inspection Panel
1. **The Angled Phone Photo (DigitalEdge Row 23 — CAT6 Cable):**
   - Click on the amber `⚑ Review Spool` badge on DigitalEdge's CAT6 cable row.
   - The slide-over inspection drawer opens on the right.
   - *"This directly addresses the brief's toughest question: 'What does your system show the buyer when it isn't sure?'"*
   - **Show the top:** *"Here is the actual crop of the angled phone photo taken in the supplier's warehouse."*
   - **Show the middle:** *"The AI caught that DigitalEdge quoted ₹2,680 per 100m spool, whereas our RFx requested 305m pull-boxes. Our deterministic engine applied a 3.05× conversion to normalize it to ₹8,174."*
   - **Show the bottom triad:** *"Instead of guessing blindly, we give the buyer 3 production-grade controls: `Accept Conversion`, `Override Price`, or click `Draft Clarification` to send a pre-written inquiry."*
   - Click `Accept Conversion`. Show how the cell turns verified green.

2. **The "Same as Last Year" ERP Resolution (Shree IT Row 9 — Thin Clients):**
   - Click on Shree IT's purple `Same as 2023` cell.
   - *"Shree IT wrote an informal email saying 'rest same as last year'. In our drawer, rather than showing a dead-end error, the system matches their reference against our ERP historical database (PO-2023-088 at ₹19,500/unit)."*
   - Click `Apply Historical Rate`. Show the cell update and recalculate live.

---

### 2:30 – 3:30: Incomplete Quotes & The Scope Delta Chaser (Option 3 Hero Flow)
1. **Show the Apples-to-Apples Basket Modeling Toggle:**
   - Click **`Projected 30-Line`** in the top ribbon:
     - *"Notice what happened: unquoted cells now display dashed market benchmark estimates (`Est. ₹4,50,000`). This solves the classic procurement trap where Shree IT's ₹1.72 Cr looks cheaper simply because they skipped 14 lines. With imputed rates, Shree IT is actually ₹3.14 Cr—more expensive than TechPro!"*
2. **Open the Scope Clarification Modal:**
   - On TechPro's column header, click **`[ ⚠ 3 Lines Missing · Request Addendum ✉ ]`**:
   - *"Look at what the system tells the Category Lead: an AI Strategic Sourcing Recommendation with a **High ROI Follow-up** verdict. TechPro is ISO-compliant with only +1.2% invoice drift. They are just 3 lines away from a viable single-source bid."*
   - *"Compare that to Shree IT, where the system advises **Disqualification** because they omitted 47% of the project scope."*
3. **Simulate Round-2 Vendor Response:**
   - Click **`[ ⚡ Simulate Supplier Round-2 Submission ]`**:
   - *"Watch what happens in real time: TechPro submits negotiated rates for those 3 lines. The matrix updates TechPro to **30/30 (100% Scope)** and recalculates their landed TCO live on screen."*

---

### 3:30 – 4:30: Bi-Directional Co-Pilot Simulation (The VP's Prompt)
1. **Click the first Quick Prompt in the Co-Pilot:**
   > *"What if we split it, cheapest per line, but only among vendors who cleared the quality questionnaire?"*
2. **Watch the AI respond and trigger live table highlighting:**
   - *"Notice that the Co-Pilot doesn't just return a text response; it acts as an execution engine."*
   - **Point to the table:** 
     - Non-compliant vendors (QuickByte and Shree IT) are automatically dimmed.
     - Winning line items light up across TechPro, GlobalIT, and DigitalEdge with emerald green `AWARDED` badges.
   - **Point to the bottom bar:**
     - *"The bottom executive bar instantly recalculates: our optimized spend is **₹2.84 Crore**, delivering **₹10.0 Lakhs in defensible savings** compared to TechPro single-sourcing."*

---

### 4:30 – 5:00: The PM Closing ("Where the Better Problem Actually Is")
> *"To close: automated quote ingestion saves 3 days of grunt work, but in my 1-page design memo, I outline where the real multi-million dollar bleed in enterprise procurement lies: **Post-Award Contract Drift**.*
>
> *Suppliers routinely win deals on low bids, then claw back margin through freight add-ons, delay surcharges, and spec substitutions on actual purchase orders. The natural evolution of this module is to close the loop: linking extracted quote terms directly into three-way ERP invoice matching to continuously score a **Vendor Trust Graph**.*
>
> *Thank you, and I look forward to walking through the live build with you during the interview."*

---

## 🎯 Pre-Flight Recording Checklist
- [ ] Make sure `http://localhost:8000` is open in your browser.
- [ ] Test the toggle: click `Projected 30-Line` to see the dashed benchmark estimates appear.
- [ ] Click `[ ⚠ 3 Lines Missing · Request Addendum ✉ ]` on TechPro to verify the Scope Follow-Up Modal.
- [ ] Click Row 23 (DigitalEdge Cable) to verify the rate card photo in the slide-over drawer.
- [ ] Hit record on Loom, follow this script, and you are guaranteed a winning submission!
