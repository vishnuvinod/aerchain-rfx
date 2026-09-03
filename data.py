"""
Aerchain RFx — Core Data
All fabricated RFx and vendor ground-truth data lives here.
"""

# ─── RFx Document ────────────────────────────────────────────────────────────
RFX = {
    "id": "RFX-2024-ITH-001",
    "title": "IT Hardware Procurement — 200-Seat Office Expansion",
    "buyer": "Vishnu Vinod",
    "designation": "Category Manager – IT",
    "organization": "DemoCorp Pvt. Ltd.",
    "deadline": "2024-12-15",
    "currency": "INR",
    "delivery_location": "Bengaluru, Karnataka – 560001",
    "quote_validity_days": 60,
    "line_items": [
        {"id": 1,  "code": "SRV-001", "description": "Rack Server 2U",                  "qty": 10,  "unit": "unit", "specs": "Dual Intel Xeon Gold 6330, 128GB DDR5 ECC RAM, 4×1.92TB NVMe SSD, Redundant PSU, IPMI", "category": "Servers"},
        {"id": 2,  "code": "SRV-002", "description": "Rack Server 1U",                  "qty": 5,   "unit": "unit", "specs": "Single Intel Xeon Silver 4310, 64GB DDR4 ECC, 2×960GB SSD, Redundant PSU",           "category": "Servers"},
        {"id": 3,  "code": "SRV-003", "description": "Blade Server Chassis",             "qty": 2,   "unit": "unit", "specs": "Full-height blade chassis, 10-blade capacity, dual 10GbE pass-through switches",       "category": "Servers"},
        {"id": 4,  "code": "SRV-004", "description": "Blade Server Module",              "qty": 8,   "unit": "unit", "specs": "Half-height blade, Intel Xeon Gold, 64GB RAM, 2×800GB SSD RAID-1",                    "category": "Servers"},
        {"id": 5,  "code": "LPT-001", "description": "Business Laptop (High-End)",       "qty": 50,  "unit": "unit", "specs": "Intel Core i7 13th Gen, 16GB DDR5, 512GB NVMe SSD, 14\" FHD IPS, Backlit KB, Win11 Pro","category": "Laptops"},
        {"id": 6,  "code": "LPT-002", "description": "Business Laptop (Standard)",       "qty": 100, "unit": "unit", "specs": "Intel Core i5 13th Gen, 8GB DDR4, 256GB NVMe SSD, 14\" FHD, Win11 Home",               "category": "Laptops"},
        {"id": 7,  "code": "WKS-001", "description": "CAD Workstation",                  "qty": 5,   "unit": "unit", "specs": "Intel Core i9-13900K, 64GB ECC RAM, 2TB NVMe, NVIDIA RTX A4000 16GB, Win11 Pro",       "category": "Workstations"},
        {"id": 8,  "code": "DSK-001", "description": "Desktop PC (Office)",              "qty": 50,  "unit": "unit", "specs": "Intel Core i5 13th Gen, 8GB RAM, 512GB SSD, Win11 Home, USB keyboard+mouse",           "category": "Desktops"},
        {"id": 9,  "code": "TNC-001", "description": "Thin Client",                      "qty": 30,  "unit": "unit", "specs": "AMD Ryzen R1505G, 8GB RAM, 64GB eMMC, Windows IoT Enterprise",                         "category": "Desktops"},
        {"id": 10, "code": "NSW-001", "description": "Network Switch 24P L2 (PoE+)",     "qty": 10,  "unit": "unit", "specs": "24×1GbE PoE+, 4×10GbE SFP+ uplinks, managed, 370W PoE budget",                        "category": "Networking"},
        {"id": 11, "code": "NSW-002", "description": "Network Switch 48P L2 (PoE+)",     "qty": 5,   "unit": "unit", "specs": "48×1GbE PoE+, 4×10GbE SFP+ uplinks, managed, 740W PoE budget",                        "category": "Networking"},
        {"id": 12, "code": "NSW-003", "description": "Network Switch 24P L3",            "qty": 3,   "unit": "unit", "specs": "24×1GbE + 4×10GbE SFP+, Layer-3 routing, stacking capable",                           "category": "Networking"},
        {"id": 13, "code": "RTR-001", "description": "Core Router",                      "qty": 2,   "unit": "unit", "specs": "Enterprise router, 2×10GbE WAN, 6×1GbE LAN, SD-WAN capable, hardware failover",        "category": "Networking"},
        {"id": 14, "code": "FWL-001", "description": "Enterprise Firewall (NGFW)",       "qty": 2,   "unit": "unit", "specs": "Next-gen firewall, 10Gbps throughput, IPS/IDS, SSL inspection, centralised mgmt",      "category": "Networking"},
        {"id": 15, "code": "WAP-001", "description": "Wireless Access Point (Wi-Fi 6)",  "qty": 40,  "unit": "unit", "specs": "Wi-Fi 6 (802.11ax), Dual-band 2.4+5GHz, PoE+, indoor, 160MHz channel support",         "category": "Networking"},
        {"id": 16, "code": "WLC-001", "description": "Wireless LAN Controller",          "qty": 2,   "unit": "unit", "specs": "Manages up to 100 APs, centralised SSID management, RF optimisation",                  "category": "Networking"},
        {"id": 17, "code": "UPS-001", "description": "UPS 1 kVA",                        "qty": 20,  "unit": "unit", "specs": "1kVA / 900W, Line-interactive, 10min backup at full load, USB monitoring",              "category": "Power"},
        {"id": 18, "code": "UPS-002", "description": "UPS 3 kVA",                        "qty": 5,   "unit": "unit", "specs": "3kVA / 2.7kW, Online double-conversion, 20min at 50% load, SNMP card",                 "category": "Power"},
        {"id": 19, "code": "UPS-003", "description": "UPS 10 kVA",                       "qty": 2,   "unit": "unit", "specs": "10kVA / 9kW, Online double-conversion, scalable battery runtime, parallel capability",  "category": "Power"},
        {"id": 20, "code": "PDU-001", "description": "Rack PDU (Metered)",               "qty": 10,  "unit": "unit", "specs": "19\" rack mount, 16A, 8×C13 + 2×C19 outlets, per-outlet metering",                    "category": "Power"},
        {"id": 21, "code": "KVM-001", "description": "IP KVM Switch (8-Port)",           "qty": 5,   "unit": "unit", "specs": "8-port over-IP KVM, remote BIOS access, 1080p, USB+HDMI, web UI",                      "category": "Infrastructure"},
        {"id": 22, "code": "SFP-001", "description": "SFP+ Module 10GbE SR",             "qty": 20,  "unit": "unit", "specs": "10GBASE-SR, 850nm VCSEL, max 300m OM3, LC duplex, DDM support",                        "category": "Infrastructure"},
        {"id": 23, "code": "CAB-001", "description": "CAT6 Cable (305m box)",            "qty": 15,  "unit": "box",  "specs": "CAT6 UTP solid copper, 305m/box, 23AWG, PVC jacket, TIA-568 compliant",                 "category": "Cabling"},
        {"id": 24, "code": "PAT-001", "description": "Fiber Patch Panel 24-Port",        "qty": 8,   "unit": "unit", "specs": "24-port LC duplex, 1U rackmount, OS2 singlemode, pre-loaded, hinged",                  "category": "Cabling"},
        {"id": 25, "code": "NAS-001", "description": "NAS Storage (4-Bay)",              "qty": 3,   "unit": "unit", "specs": "4-bay NAS, 2×10GbE, hardware RAID 0/1/5/6/10, hot-swap trays, expandable",            "category": "Storage"},
        {"id": 26, "code": "SSD-001", "description": "Enterprise SSD 1TB",              "qty": 50,  "unit": "unit", "specs": "1TB 2.5\" SATA Enterprise SSD, DWPD 3, 5yr warranty, server-grade",                    "category": "Storage"},
        {"id": 27, "code": "RAM-001", "description": "RAM Module 32GB DDR5 ECC",        "qty": 100, "unit": "unit", "specs": "32GB DDR5-4800 ECC RDIMM, server-grade, registered, heat spreader",                    "category": "Components"},
        {"id": 28, "code": "GPU-001", "description": "Data Center GPU",                  "qty": 5,   "unit": "unit", "specs": "NVIDIA A100 40GB PCIe or equivalent, HPC/AI workloads, NVLink support",                "category": "Components"},
        {"id": 29, "code": "MON-001", "description": "Monitor 27\" 4K UHD",             "qty": 60,  "unit": "unit", "specs": "27\" UHD IPS 4K, USB-C 65W PD, height/tilt/pivot adjustable, VESA 100×100",            "category": "Peripherals"},
        {"id": 30, "code": "RAK-001", "description": "Server Rack Cabinet 42U",         "qty": 5,   "unit": "unit", "specs": "42U 800×1000mm deep, glass front door, perforated rear, PDU rails, lockable",          "category": "Infrastructure"},
    ],
    "questionnaire": [
        {"id": 1,  "question": "Is your organization ISO 9001:2015 certified? Attach certificate.", "type": "yesno+doc"},
        {"id": 2,  "question": "State the warranty period (in months) for each product category quoted.", "type": "text"},
        {"id": 3,  "question": "What is the expected delivery lead time (in calendar days) from PO date?", "type": "number"},
        {"id": 4,  "question": "What payment terms can you offer? (e.g., Net 30 / Net 60 / advance)", "type": "text"},
        {"id": 5,  "question": "Do you provide on-site technical support? State SLA response time.", "type": "text"},
        {"id": 6,  "question": "What percentage of quoted products are locally sourced vs. imported?", "type": "text"},
        {"id": 7,  "question": "Provide your GST Registration Number.", "type": "text"},
        {"id": 8,  "question": "Are any of the quoted products End-of-Life (EOL) within 18 months?", "type": "yesno"},
        {"id": 9,  "question": "Provide references from at least 2 enterprise deployments of similar scale.", "type": "text"},
        {"id": 10, "question": "Can you fulfill a partial order of minimum 60% of line items?", "type": "yesno"},
    ],
    "terms": [
        "All prices must be quoted in INR, inclusive of all applicable duties, exclusive of GST.",
        "Delivery must be completed within 30 calendar days of PO issuance to Bengaluru, Karnataka.",
        "Minimum warranty: 3 years on-site for servers and networking; 1 year for peripherals.",
        "Quote validity: 60 days from submission date.",
        "Payment: Net 30 days from delivery and acceptance.",
        "Buyer reserves the right to award to multiple vendors (split order).",
    ]
}

# ─── Vendor Master ────────────────────────────────────────────────────────────
VENDORS = [
    {
        "id": "techpro",
        "name": "TechPro Solutions Pvt. Ltd.",
        "contact": "sales@techpro-solutions.in",
        "response_file": "techpro_response.xlsx",
        "response_format": "Excel",
        "lines_quoted": 27,
        "submission_date": "2024-11-22",
        "description": "Clean Excel response — quotes 27/30 lines (misses SRV-003, WKS-001, UPS-003). Competitive pricing, well-structured.",
        "edge_case": "3 lines not quoted",
    },
    {
        "id": "globalit",
        "name": "GlobalIT Supplies Inc.",
        "contact": "bids@globalit-supplies.com",
        "response_file": "globalit_response.pdf",
        "response_format": "PDF",
        "lines_quoted": 27,
        "submission_date": "2024-11-23",
        "description": "PDF on company letterhead. All prices in USD with 12% discount buried in a footnote on page 3. Quotes 27/30 lines.",
        "edge_case": "USD pricing + discount in footnote + EOL flag on LPT-002",
    },
    {
        "id": "quickbyte",
        "name": "QuickByte India",
        "contact": "rfq@quickbyte.co.in",
        "response_file": "quickbyte_response.docx",
        "response_format": "Word",
        "lines_quoted": 25,
        "submission_date": "2024-11-24",
        "description": "Word document where prices are written in paragraph prose. Cheapest vendor overall. NOT ISO certified. References incomplete.",
        "edge_case": "Prose format + not ISO certified",
    },
    {
        "id": "digitaledge",
        "name": "DigitalEdge Corp",
        "contact": "procurement@digitaledge.in",
        "response_file": "digitaledge_ratecard.png",
        "response_format": "Image",
        "lines_quoted": 28,
        "submission_date": "2024-11-25",
        "description": "A photo of a printed rate card, taken at an angle on a phone. Unit for CAT6 cable is 'per 100m' instead of 'per box (305m)'.",
        "edge_case": "Angled photo + unit mismatch on CAB-001",
    },
    {
        "id": "shree",
        "name": "Shree IT Traders",
        "contact": "shreeittrd@gmail.com",
        "response_file": "shree_email.txt",
        "response_format": "Email",
        "lines_quoted": 22,
        "submission_date": "2024-11-26",
        "description": "Plain email. Partial quote — 22/30 lines. Some items referenced as 'same as last year'. Questionnaire mostly unanswered.",
        "edge_case": "Partial quote + 'same as last year' references + incomplete questionnaire",
    },
]

# ─── Ground Truth Prices (INR per unit, for file generation) ─────────────────
# None = item NOT quoted by this vendor
# "SAME_AS_LAST_YEAR" = vendor referenced previous quote (Shree only)
# "UNIT_UNCLEAR" = unit ambiguous (DigitalEdge CAT6 cable - per 100m not per box)
PRICES = {
    # item_id: { vendor_id: price_inr }
    1:  {"techpro": 285000,  "globalit": 300600,  "quickbyte": 272000,  "digitaledge": 265000,  "shree": None},
    2:  {"techpro": 188000,  "globalit": 192050,  "quickbyte": 175000,  "digitaledge": 178000,  "shree": 182000},
    3:  {"techpro": None,    "globalit": 876750,  "quickbyte": None,    "digitaledge": None,    "shree": None},
    4:  {"techpro": 96000,   "globalit": 91850,   "quickbyte": 91000,   "digitaledge": 92000,   "shree": 89000},
    5:  {"techpro": 95000,   "globalit": 87675,   "quickbyte": 88000,   "digitaledge": 90000,   "shree": 87500},
    6:  {"techpro": 62000,   "globalit": 56780,   "quickbyte": 54000,   "digitaledge": 57000,   "shree": 53500},
    7:  {"techpro": None,    "globalit": None,    "quickbyte": 172000,  "digitaledge": 175000,  "shree": None},
    8:  {"techpro": 42000,   "globalit": 43420,   "quickbyte": 35000,   "digitaledge": 38000,   "shree": 34500},
    9:  {"techpro": 24000,   "globalit": 24215,   "quickbyte": 19500,   "digitaledge": 21000,   "shree": "SAME_AS_LAST_YEAR"},
    10: {"techpro": 18500,   "globalit": 18370,   "quickbyte": 16500,   "digitaledge": 17500,   "shree": 16800},
    11: {"techpro": 34000,   "globalit": 35905,   "quickbyte": 29000,   "digitaledge": 31500,   "shree": 29500},
    12: {"techpro": 68000,   "globalit": 68470,   "quickbyte": 60000,   "digitaledge": 65000,   "shree": None},
    13: {"techpro": 132000,  "globalit": 133600,  "quickbyte": 118000,  "digitaledge": 125000,  "shree": None},
    14: {"techpro": 285000,  "globalit": 317300,  "quickbyte": None,    "digitaledge": 275000,  "shree": None},
    15: {"techpro": 13500,   "globalit": 12943,   "quickbyte": 11800,   "digitaledge": 12500,   "shree": 12200},
    16: {"techpro": 88000,   "globalit": 83500,   "quickbyte": None,    "digitaledge": None,    "shree": None},
    17: {"techpro": 15800,   "globalit": 14613,   "quickbyte": 13500,   "digitaledge": 14200,   "shree": 13200},
    18: {"techpro": 42000,   "globalit": 42585,   "quickbyte": 36500,   "digitaledge": 38500,   "shree": 36000},
    19: {"techpro": None,    "globalit": None,    "quickbyte": None,    "digitaledge": 142000,  "shree": None},
    20: {"techpro": 9500,    "globalit": 9185,    "quickbyte": 7800,    "digitaledge": 8800,    "shree": "SAME_AS_LAST_YEAR"},
    21: {"techpro": 13500,   "globalit": 13193,   "quickbyte": 10800,   "digitaledge": 11500,   "shree": None},
    22: {"techpro": 3800,    "globalit": 3841,    "quickbyte": 3100,    "digitaledge": 3400,    "shree": 3200},
    23: {"techpro": 8200,    "globalit": 7348,    "quickbyte": 7100,    "digitaledge": "UNIT_UNCLEAR",  "shree": 7500},
    24: {"techpro": 6200,    "globalit": 6012,    "quickbyte": 5100,    "digitaledge": 5500,    "shree": 5000},
    25: {"techpro": 92000,   "globalit": 93520,   "quickbyte": 80000,   "digitaledge": 85000,   "shree": None},
    26: {"techpro": 19500,   "globalit": 19205,   "quickbyte": 16800,   "digitaledge": 18000,   "shree": 16500},
    27: {"techpro": 13800,   "globalit": 12358,   "quickbyte": 12100,   "digitaledge": 12800,   "shree": "SAME_AS_LAST_YEAR"},
    28: {"techpro": 650000,  "globalit": None,    "quickbyte": None,    "digitaledge": 620000,  "shree": None},
    29: {"techpro": 34000,   "globalit": 35070,   "quickbyte": 29500,   "digitaledge": 31000,   "shree": 30000},
    30: {"techpro": 28500,   "globalit": 29643,   "quickbyte": 25500,   "digitaledge": 26500,   "shree": 25800},
}

# GlobalIT original USD prices (before INR conversion at 83.5)
GLOBALIT_USD_PRICES = {
    1: 3600, 2: 2300, 3: 10500, 4: 1100, 5: 1050, 6: 680, 8: 520, 9: 290,
    10: 220, 11: 430, 12: 820, 13: 1600, 14: 3800, 15: 155, 16: 1000,
    17: 175, 18: 510, 20: 110, 21: 158, 22: 46, 23: 88, 24: 72, 25: 1120,
    26: 230, 27: 148, 29: 420, 30: 355
}
# Note: GlobalIT applies a 12% discount (buried in footnote) to listed USD prices.
# The prices above are AFTER the 12% discount is applied.
# Pre-discount prices are: each price / 0.88

# ─── Questionnaire Responses ─────────────────────────────────────────────────
QUESTIONNAIRE_RESPONSES = {
    "techpro": {
        1: {"answer": "Yes", "detail": "ISO 9001:2015, Certificate No. ISO9001-2023-TP-4521, valid till Dec 2026", "pass": True},
        2: {"answer": "Servers: 36 months on-site | Laptops: 24 months carry-in | Networking: 36 months | Others: 12 months", "pass": True},
        3: {"answer": "21 calendar days", "pass": True},
        4: {"answer": "Net 30, Net 45, or Net 60 days — negotiable", "pass": True},
        5: {"answer": "Yes — on-site support. SLA: 4-hour response, next business day resolution", "pass": True},
        6: {"answer": "40% locally assembled, 60% imported (OEM authorised distributor)", "pass": True},
        7: {"answer": "29AABCT4520E1ZQ", "pass": True},
        8: {"answer": "No products quoted are EOL within 18 months", "pass": True},
        9: {"answer": "1. Infosys Mysore (2023) — 500 laptops + 50 servers\n2. Wipro Bengaluru (2022) — full IT infra for new campus\n3. HDFC Bank Pune (2023) — 200 desktops + networking", "pass": True},
        10: {"answer": "Yes — can fulfil minimum 50% partial order", "pass": True},
    },
    "globalit": {
        1: {"answer": "Yes", "detail": "ISO 9001:2022, Certificate No. ISO9001-2022-GI-8812, valid till Sep 2025", "pass": True},
        2: {"answer": "Servers: 36 months on-site | Laptops: 12 months carry-in | All others: 12 months", "pass": True},
        3: {"answer": "28 calendar days (import clearance included)", "pass": True},
        4: {"answer": "Net 45 days only", "pass": True},
        5: {"answer": "Remote support only. No on-site support offered in India.", "pass": False},
        6: {"answer": "10% locally managed, 90% imported direct from OEM (USA/Taiwan)", "pass": True},
        7: {"answer": "27AABCG7891B1ZF", "pass": True},
        8: {"answer": "LPT-002 (Business Laptop Standard) is scheduled EOL in 14 months.", "pass": False, "flag": "EOL_WARNING"},
        9: {"answer": "1. TCS Hyderabad (2023) — 300 laptops\n2. Cognizant Chennai (2022) — server refresh", "pass": True},
        10: {"answer": "Yes — minimum 60% of lines", "pass": True},
    },
    "quickbyte": {
        1: {"answer": "No — QuickByte India is not ISO 9001 certified at this time.", "pass": False, "flag": "QUALITY_FAIL"},
        2: {"answer": "Servers: 12 months | Laptops: 12 months | Networking: 12 months | Others: 6 months", "pass": False},
        3: {"answer": "14 calendar days for in-stock items", "pass": True},
        4: {"answer": "Net 30 or Net 60 days", "pass": True},
        5: {"answer": "Yes — on-site support available. SLA: 8 business hours", "pass": True},
        6: {"answer": "70% locally sourced / assembled, 30% imported", "pass": True},
        7: {"answer": "32AABCQ1234C1ZA", "pass": True},
        8: {"answer": "No EOL products in quote", "pass": True},
        9: {"answer": "1. Startup client (NDA, cannot disclose name)", "pass": False, "flag": "INCOMPLETE_REFERENCES"},
        10: {"answer": "Yes", "pass": True},
    },
    "digitaledge": {
        1: {"answer": "Yes", "detail": "ISO 9001:2021, Certificate No. ISO9001-2021-DE-3309, valid till Mar 2027", "pass": True},
        2: {"answer": "All products: 24 months comprehensive warranty", "pass": True},
        3: {"answer": "30 calendar days", "pass": True},
        4: {"answer": "Net 30 days", "pass": True},
        5: {"answer": "On-site support. SLA: 6-hour response, same-day resolution for Bengaluru", "pass": True},
        6: {"answer": "50% local, 50% imported", "pass": True},
        7: {"answer": "19AABCD5678D1ZB", "pass": True},
        8: {"answer": "No EOL products.", "pass": True},
        9: {"answer": "1. Amazon India Hyderabad (2024) — 500-seat setup\n2. Flipkart Bengaluru (2023) — 200-seat expansion\n3. PhonePe Pune (2023) — network infra", "pass": True},
        10: {"answer": "Yes — minimum 50% of lines", "pass": True},
    },
    "shree": {
        1: {"answer": None, "pass": False, "flag": "NOT_ANSWERED"},
        2: {"answer": "Standard OEM warranty applies", "pass": False, "flag": "VAGUE"},
        3: {"answer": "10–15 days for items in stock. Imported items may take longer.", "pass": True},
        4: {"answer": "Net 30 days preferred.", "pass": True},
        5: {"answer": "Will coordinate with OEM service centre. No dedicated support team.", "pass": False, "flag": "VAGUE"},
        6: {"answer": None, "pass": False, "flag": "NOT_ANSWERED"},
        7: {"answer": "29AABCS9876E1ZC", "pass": True},
        8: {"answer": None, "pass": False, "flag": "NOT_ANSWERED"},
        9: {"answer": None, "pass": False, "flag": "NOT_ANSWERED"},
        10: {"answer": "Yes, can do partial order.", "pass": True},
    },
}

USD_TO_INR = 83.5
