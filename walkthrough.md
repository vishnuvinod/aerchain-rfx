# 🎬 Aerchain RFx Intelligence Cockpit — Executive Video Walkthrough Script

> **Tone:** Authentic, conversational, sharp, and grounded. Speak like an experienced Senior/Principal PM walking peers through a prototype you built with care and conviction.

---

## ⏱️ Pre-Record Checklist (15 Seconds)
- Open Chrome to: `http://localhost:8000`
- Press `Cmd + Shift + B` (hides bookmarks bar)
- Press `Cmd + 0` (resets zoom to 100%)
- Have your phone propped up directly under your monitor with `phone_notes_script.md` open.
- Take a deep breath, smile, and start recording.

---

## 🎬 Act 1: The Hook & The Real Pain (0:00 – 0:50)

👉 **What to do on screen:**
- Start on **Step 1: Draft RFx Scope**.
- Move your mouse naturally over the prompt input and the 4 sizing cards below.

🗣️ **What to say:**
> *"Hey Raghunath, Neel, and the Aerchain team—I’m Vishnu.
>
> Let’s be honest: every enterprise procurement team knows this pain. You need to buy 30 line items of IT hardware for a new campus. You send out an RFx. And over the next nine days, complete chaos lands in your inbox.
>
> One vendor sends an Excel sheet that completely ignores your template. Another sends a PDF with a 12% discount buried in a footnote on page 3. Someone sends a Word document with prices in paragraphs. Someone else takes an angled photo of a paper rate card on their phone. And another vendor just replies: 'same as last year, freight extra.'
>
> A category buyer spends three full days retyping all of this into a spreadsheet just to answer one basic question: 'Who should we award this to?'
>
> We built this system to delete that week.
>
> We start right here in our RFx Studio. Instead of forcing rigid Excel templates that suppliers hate, the buyer just describes their campus scope in plain English. Our engine automatically translates that intent into a full 30-item Bill of Materials—servers, networking, UPS power, and cabling—ready for market."*

---

## 🎬 Act 2: Real-World Ingestion (0:50 – 1:40)

👉 **What to do on screen:**
- Click **Step 2: Ingest Submissions** in the top navigation bar.
- Slowly scroll past the 5 vendor cards.

🗣️ **What to say:**
> *"Now, let's see what happens when the responses arrive.
>
> In enterprise procurement, you can’t force suppliers into a rigid portal. They reply with whatever they have.
>
> Look at our Ingestion Inbox: 5 suppliers, 5 completely different formats, zero forced templates:
> - **TechPro** sent a clean Excel sheet, but omitted 3 critical lines.
> - **GlobalIT** quoted in US Dollars, with that sneaky 12% footnote discount.
> - **QuickByte** sent a Word document where the pricing is buried inside prose paragraphs.
> - **DigitalEdge** literally took an angled smartphone photo of a printed paper rate card.
> - And **Shree IT** sent a quick email saying 'rest same as last year'.
>
> Our multimodal engine parses all five formats without breaking a sweat.
>
> Now, let's enter the Decision Cockpit."*

---

## 🎬 Act 3: The Cockpit & Commercial Traps (1:40 – 3:00)

👉 **What to do on screen:**
- Click **Step 3: Normalize & Compare**.
- **Action 1:** Check the box `Require Strict ISO 9001:2015`. *(Pause 2 sec as QuickByte & Shree dim out with red badges).* Uncheck it.
- **Action 2:** Hover over **Row 5 (LPT-001)** under **GlobalIT**.
  - Point to the bold `₹77,154 net` on top, and `$1,050 USD · -12% Ftnt` below it.
- **Action 3:** Check the box `Require 3-Yr On-Site SLA`.
  - *(Watch GlobalIT dim with red "NO ONSITE SLA", and the green AWARDED badge instantly jump to TechPro at ₹88,000!).*
- **Action 4:** In the top ribbon, click the **`30-Line`** button.
  - Hover over **Shree IT’s column header**: show the partial ₹1.73 Cr jump to the true 30-line estimate of **₹2.93 Crore**.

🗣️ **What to say:**
> *"This is the comparison grid. Everything is normalized to Indian Rupees and common units.
>
> Notice three things that make this enterprise-grade:
>
> **First: Compliance Gatekeeping.** 
> Before a buyer looks at price, they have to know if a vendor is legally qualified. Watch what happens when I toggle `Strict ISO 9001`—QuickByte and Shree IT immediately dim out. We don't let buyers make rookie mistakes on uncertified suppliers.
>
> **Second: Dual-Layer Traceability & The SLA Gate.**
> Look at Row 5 for GlobalIT. On top, you see the normalized rate: **₹77,154**. Right underneath, you see the raw provenance: **$1,050 in USD with the 12% footnote discount applied**. The buyer never has to guess where a number came from.
>
> Now look closer at GlobalIT: pure price optimization would give them our 50 developer laptops to save a few thousand rupees. But our 10-point audit catches that **GlobalIT only offers remote support from Singapore!** 
> For 50 developers in Bengaluru, remote-only support is an operational disaster. Watch what happens when I toggle `Require 3-Year On-Site SLA`: GlobalIT is disqualified from the lot, and the award instantly routes to **TechPro**, backed by their 4-hour local Bengaluru depot!
>
> **Third: Disarming Incomplete Quotes.**
> Look at Shree IT over here. Their headline total says ₹1.73 Crore. It looks cheap—until you realize they only quoted 16 of our 30 lines! 
> When I toggle our 30-line view, the engine imputes baseline category benchmarks for their missing lines. Their real projected TCO jumps to **₹2.93 Crore**—and their paper discount completely evaporates."*

---

## 🎬 Act 4: The Ugly Edges & Spec Drift (3:00 – 4:00)

👉 **What to do on screen:**
- **Action 1:** Scroll down to **Row 23 (DigitalEdge CAT6 Cable)**. Click the amber **`⚑ Review Spool`** badge.
  - Drawer opens on right. Point to the cropped rate card photo. Point to the `3.05×` math formula.
  - Click the green button: `[ ✓ Accept Conversion as Defensible ]`.
- **Action 2:** Scroll to **Row 5 (QuickByte Laptop)**. Click the pulsing amber **`⚠ Spec Drift`** badge.
  - Show the memory comparison (32GB ECC requested vs 16GB soldered quoted). Show the `+₹7.25 Lakhs` penalty. Close drawer.

🗣️ **What to say:**
> *"Now let's talk about the ugly edges that break traditional tools.
>
> On Row 23, DigitalEdge submitted an angled photo where they quoted CAT6 cable **per 100-meter spool**. But our RFx asked for **305-meter master boxes**. 
>
> Our engine recognized the unit mismatch, applied an exact 3.05x multiplier, and calculated **₹8,174 per box**. But because confidence was 62%—below our 75% threshold—it flagged it for human audit. 
> The buyer opens this inspection drawer, sees the actual photo snippet, checks the formula, and clicks *Accept Conversion*. That is true Human-in-the-Loop governance.
>
> Even sneakier is **Spec Drift on Row 5**: QuickByte quoted a cheap laptop, but buried in their Word document was a specification downgrade: they quoted **16GB soldered RAM** instead of our mandated **32GB ECC upgradeable RAM**. 
> Instead of missing it, our engine flags it and calculates a **+₹7.25 Lakh remediation penalty** right into their landed cost."*

---

## 🎬 Act 5: The AI Co-Pilot & The L1 Trap (4:00 – 5:00)

👉 **What to do on screen:**
- Move cursor to the right-hand **AI Co-Pilot** panel.
- Click prompt pill **`Q4`**: *"QuickByte quoted ₹2.70 Cr. Why shouldn't we award to them? (L1 Trap)"*
  - *(Wait 2-3 sec as AI streams the breakdown and cost chart).*
- Click prompt pill **`Q1`** or **`Q5`**: *"Split award among ISO-cleared vendors only"*.
  - *(AI returns the ₹2.84 Cr / ₹2.99 Cr scenario).*
  - Click **`[ Highlight in Table ]`**: show the matrix light up with green `AWARDED` badges!

🗣️ **What to say:**
> *"Now, the buyer stops clicking and starts asking questions.
>
> I'll click Q4: *'QuickByte quoted ₹2.70 Crore. Why shouldn't we just award to them?'*
>
> This is the classic **L1 procurement trap**. QuickByte looks ₹14 Lakhs cheaper on paper. But our AI analyst breaks down the hidden reality:
> - They skipped 3 critical lines: **+₹18.5 Lakhs** to spot-buy elsewhere.
> - Soldered RAM downgrade: **+₹7.25 Lakhs** remediation.
> - Only a 12-month carry-in warranty: **+₹3.8 Lakhs** uplift.
> - FOB warehouse freight: **+₹2.1 Lakhs**.
>
> QuickByte's **True Landed TCO is actually ₹3.02 Crore**—they are the most expensive vendor in the tender!
>
> Now I'll ask Q1 to model our optimal split award among qualified vendors. 
> With one click on *Highlight in Table*, the matrix executes the strategy: 
> We award 12 items to TechPro, 10 to GlobalIT, and 8 to DigitalEdge. Total spend is **₹2.84 Crore**—saving **₹1.65 Crore against our budget** with zero compliance risk."*

---

## 🎬 Act 6: ERP PO Export & The Bigger Problem (5:00 – 5:45)

👉 **What to do on screen:**
- Click the blue button in top-right: **`[ Award Selected Allocation ]`**.
  - Modal opens. Show the 3 split vendor summaries.
  - Toggle from `Executive Sourcing Memo` $\to$ `Coupa JSON Payload` $\to$ `NetSuite CSV Export`.
  - Click **`[ Copy Coupa Payload ]`**.
- Look up at the camera for the closing statement.

🗣️ **What to say:**
> *"Finally, we close the loop. 
>
> A recommendation is useless if a buyer has to spend another afternoon retyping lines into Coupa or SAP. 
>
> Clicking *Award Selected Allocation* generates our complete audit package: an **Executive Sourcing Memo** defending the decision, alongside **ready-to-ingest Coupa JSON and NetSuite CSV payloads**—item codes, quantities, and landed INR rates perfectly matched.
>
> ---
>
> ### 💡 The Closing Thought (The $25M ARR Thesis)
> I want to leave you with one final product thought. 
>
> Deleting the 3 days of spreadsheet transcription is huge. But as Aerchain scales to $25M ARR, **the real multi-million dollar problem in enterprise spend isn't quote extraction—it’s Post-Award Invoice & Contract Drift.**
>
> Suppliers bid aggressively to win the RFx, and then claw back margin through freight add-ons and spec downgrades during fulfillment. 
>
> The real breakthrough is connecting this extraction engine directly to 3-way invoice matching in SAP—so that the promises made during negotiation are enforced down to the last rupee on the invoice.
>
> That is how we turn procurement from a reactive back-office cost center into an intelligent profit driver.
>
> Thank you so much for your time—I'm looking forward to diving into the details with you!"*

---

### 🎉 Recording Tips for a Confident Delivery
1. **Don't rush:** You have plenty of time. If you mispronounce a word, just pause for 1 second, repeat the sentence cleanly, and keep going (nobody expects a Hollywood cut).
2. **Smile when you start and end:** It projects natural senior PM confidence.
3. **Keep the mouse purposeful:** Hover only over what you're talking about so the viewer's eyes follow effortlessly.
