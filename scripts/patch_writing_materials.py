#!/usr/bin/env python3
"""
Adds high-fidelity vector SVG visual stimulus metadata to the 8 Academic Task 1 items
in scripts/authentic_builder/writing_data.py.
"""

import re
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts", "authentic_builder", "writing_data.py")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Bar Chart
bar_mat = """        "topic": "Renewable Energy & Capital Allocation",
        "material": {
            "type": "image",
            "title": "Global Renewable Energy Investment by Technology (2010–2023)",
            "imageUrl": "/images/writing/task1_bar_chart_renewables.svg",
            "imageDescription": (
                "Bar chart showing annual global investment ($ billions) in Solar PV, Wind Energy, and Hydroelectric:\\n"
                "• 2010: Wind $110bn, Solar $85bn, Hydroelectric $55bn (Total: $250bn)\\n"
                "• 2014: Wind $135bn, Solar $130bn, Hydroelectric $65bn (Peak for hydro; Total: $330bn)\\n"
                "• 2018: Solar $180bn (surpasses wind), Wind $160bn, Hydroelectric $45bn (Total: $385bn)\\n"
                "• 2023: Solar $320bn (steepest rise), Wind $215bn, Hydroelectric $38bn (Total: $573bn)"
            ),
            "keyDataPoints": [
                "Solar PV expanded dramatically from $85 billion in 2010 to a peak of $320 billion in 2023, surpassing all other sectors.",
                "Wind energy exhibited consistent upward trajectory from $110 billion in 2010 to $215 billion by 2023.",
                "Hydroelectric power saw volatile investments, peaking at $65 billion in 2014 before steadily waning to $38 billion in 2023.",
                "Overall total renewable capital deployment more than doubled over the thirteen-year timeframe."
            ]
        },"""
content = content.replace('        "topic": "Renewable Energy & Capital Allocation",', bar_mat, 1)

# 2. Line Graph
line_mat = """        "topic": "Technology & Sociological Demographics",
        "material": {
            "type": "image",
            "title": "Smartphone Adoption Across Age Demographics (2012–2022)",
            "imageUrl": "/images/writing/task1_line_graph_smartphones.svg",
            "imageDescription": (
                "Line graph tracing smartphone adoption (% of population using smartphones daily) across four age brackets from 2012 to 2022:\\n"
                "• 18–29 years: 72% in 2012, 81% in 2014, 87% in 2016, 91% in 2018, 95% in 2020, 98% in 2022 (near total saturation)\\n"
                "• 30–49 years: 54% in 2012, 63% in 2014, 73% in 2016, 81% in 2018, 88% in 2020, 92% in 2022\\n"
                "• 50–64 years: 31% in 2012, 42% in 2014, 60% in 2016, 68% in 2018, 74% in 2020, 80% in 2022\\n"
                "• 65+ years: 14% in 2012, 22% in 2014, 33% in 2016, 43% in 2018, 50% in 2020, 58% in 2022 (quadrupled over decade)"
            ),
            "keyDataPoints": [
                "18–29 demographic commenced highest in 2012 at 72% and neared saturation at 98% by 2022.",
                "30–49 cohort escalated from 54% in 2012 to 92% in 2022.",
                "50–64 cohort rose steeply from 31% to 80% over the ten-year period.",
                "Senior cohort (65+) exhibited the fastest relative surge, quadrupling from 14% in 2012 to 58% in 2022."
            ]
        },"""
content = content.replace('        "topic": "Technology & Sociological Demographics",', line_mat, 1)

# 3. Pie Chart
pie_mat = """        "topic": "Energy Economics & Domestic Utilities",
        "material": {
            "type": "image",
            "title": "Household Energy Consumption Breakdown in the UK (1990 vs 2020)",
            "imageUrl": "/images/writing/task1_pie_chart_energy.svg",
            "imageDescription": (
                "Two pie charts comparing proportional distribution of domestic energy end-use demands in the UK:\\n"
                "• Space heating: 52% (1990) -> 46% (2020) (remains primary energy sink)\\n"
                "• Water heating: 24% (1990) -> 17% (2020) (decreased by 7 percentage points)\\n"
                "• Electronic consumer appliances: 13% (1990) -> 26% (2020) (exactly doubled, emerging as second largest sector)\\n"
                "• Cooking: 7% (1990) -> 6% (2020)\\n"
                "• Lighting: 4% (1990) -> 5% (2020)"
            ),
            "keyDataPoints": [
                "Space heating constituted the largest single energy sink in both years (52% in 1990, decreasing slightly to 46% in 2020).",
                "Water heating dropped from 24% to 17% due to modern boiler insulation.",
                "Electronic consumer appliances doubled from 13% to 26%, becoming the second largest consumer.",
                "Cooking and lighting both saw modest reductions (cooking: 7% to 6%; lighting: 4% to 5%)."
            ]
        },"""
content = content.replace('        "topic": "Energy Economics & Domestic Utilities",', pie_mat, 1)

# 4. Table
table_mat = """        "topic": "Higher Education & Global Student Mobility",
        "material": {
            "type": "image",
            "title": "International Tertiary Student Enrolment Across Five Academic Disciplines",
            "imageUrl": "/images/writing/task1_table_university.svg",
            "imageDescription": (
                "Table comparing international student enrolment (2015 vs 2023), percentage growth, retention, and graduation rates at an Australian university:\\n"
                "• Computer Science: 1,240 (2015) -> 3,850 (2023), Growth: +210.5%, Retention: 93%, Completion: 91%\\n"
                "• Business & Finance: 4,200 (2015) -> 5,600 (2023), Growth: +33.3%, Retention: 88%, Completion: 86%\\n"
                "• Engineering & Technology: 2,100 (2015) -> 3,150 (2023), Growth: +50.0%, Retention: 95%, Completion: 94%\\n"
                "• Humanities & Social Sciences: 1,850 (2015) -> 1,200 (2023), Growth: -35.1%, Retention: 74%, Completion: 71%\\n"
                "• Medicine & Health Sciences: 950 (2015) -> 1,120 (2023), Growth: +17.9%, Retention: 96%, Completion: 93%"
            ),
            "keyDataPoints": [
                "Computer Science had the steepest surge in student enrolment, soaring from 1,240 in 2015 to 3,850 in 2023 (+210%), with 91% retention.",
                "Business & Finance enrolled the largest overall student body (4,200 in 2015 to 5,600 in 2023) with an 88% retention rate.",
                "Engineering expanded from 2,100 to 3,150 students, maintaining the highest completion rate at 94%.",
                "Humanities & Arts experienced an absolute decline from 1,850 to 1,200 students (-35%) with the lowest retention at 74%."
            ]
        },"""
content = content.replace('        "topic": "Higher Education & Global Student Mobility",', table_mat, 1)

# 5. Process: Battery
batt_mat = """        "topic": "Chemical Engineering & Circular Economy",
        "material": {
            "type": "image",
            "title": "Industrial Lithium-Ion Battery Recycling Procedure",
            "imageUrl": "/images/writing/task1_proc_battery_recycling.svg",
            "imageDescription": (
                "Process flowchart outlining five industrial recycling stages for spent EV lithium-ion battery packs:\\n"
                "• Stage 1 (Dismantling & Shredding): Automated electrical discharge followed by cryogenic shredding in hermetically sealed inert Argon atmosphere.\\n"
                "• Stage 2 (Physical Separation): Air classification & magnetic sieving separate plastic and metal casings from cathode 'black mass'.\\n"
                "• Stage 3 (Acid Leaching): Black mass dissolved in heated 80°C sulfuric acid (H2SO4) and hydrogen peroxide (H2O2) leaching solution.\\n"
                "• Stage 4 (Precipitation & Calcination): Multi-stage pH neutralization and thermal calcination furnaces.\\n"
                "• Stage 5 (High-Purity Output): 98.5% pure Lithium Carbonate (Li2CO3), Nickel Hydroxide (Ni(OH)2), and Cobalt Sulfate (CoSO4) crystals ready for new battery cells."
            ),
            "keyDataPoints": [
                "Stage 1: Mechanical disassembly and automated cryogenic shredding under an inert argon blanket to prevent thermal runaway.",
                "Stage 2: Density separation and hydrometallurgical acid leaching using sulfuric acid and hydrogen peroxide.",
                "Stage 3: Chemical precipitation and calcination to regenerate cathode precursor salts (nickel, cobalt, lithium carbonate) at 98.5% purity."
            ]
        },"""
content = content.replace('        "topic": "Chemical Engineering & Circular Economy",', batt_mat, 1)

# 6. Map Plan
map_mat = """        "topic": "Urban Planning & Waterfront Renewal",
        "material": {
            "type": "image",
            "title": "Port Haven Waterfront Redevelopment: 2000 vs Present",
            "imageUrl": "/images/writing/task1_map_port_haven.svg",
            "imageDescription": (
                "Two layout plans illustrating structural transformation of Port Haven waterfront from 2000 to Present:\\n"
                "• North: Derelict timber warehouses and freight cranes demolished and replaced by 400-unit luxury apartment towers and a public art museum.\\n"
                "• Center: Commercial container shipping canal dredged and converted into a recreational yacht marina flanked by a pedestrian boardwalk promenade and cafes.\\n"
                "• South: Industrial freight rail sidings converted into a modern electrified light rail transit terminus with direct 15-minute connection to the CBD.\\n"
                "• East: Former agricultural farmland transformed into a protected public nature reserve wetland with walking trails."
            ),
            "keyDataPoints": [
                "Northern heavy cargo dock and derelict timber warehouses were razed and replaced by luxury residential apartment complexes and a public art gallery.",
                "Central commercial shipping canal was converted into a recreational yacht marina bordered by a pedestrian promenade and restaurants.",
                "Southern industrial railyard was replaced by a modern light rail transit terminus connecting directly to the central business district.",
                "Eastern farmland was converted into a public nature reserve and botanical wetland park."
            ]
        },"""
content = content.replace('        "topic": "Urban Planning & Waterfront Renewal",', map_mat, 1)

# 7. Process: Pumped Storage
pump_mat = """        "topic": "Civil & Electrical Engineering",
        "material": {
            "type": "image",
            "title": "Closed-Loop Hydroelectric Pumped Storage Power Station",
            "imageUrl": "/images/writing/task1_proc_pumped_storage.svg",
            "imageDescription": (
                "Technical schematic of closed-loop hydroelectric pumped storage facility illustrating dual day/night operational modes:\\n"
                "• Mountain infrastructure: High-altitude upper mountain reservoir connected to lower catchment basin via a subterranean high-pressure penstock.\\n"
                "• Powerhouse: Underground facility with reversible hydraulic turbine-generator / pump unit.\\n"
                "• Daytime Peak Mode: High electricity demand -> water cascades downward under gravity through penstock, driving turbines to generate 500 MW for national grid.\\n"
                "• Nighttime Off-Peak Mode: Low grid demand & cheap surplus nuclear/wind electricity -> turbines reverse to operate as high-capacity pumps, driving water back up penstock to refill upper reservoir.\\n"
                "• Closed-loop design recycles 100% of water with zero consumptive depletion."
            ),
            "keyDataPoints": [
                "Daytime operation: Water flows downward from upper mountain reservoir through a subterranean penstock, spinning a turbine-generator to supply 500 MW to the electrical grid.",
                "Nighttime operation: Reversible turbines act as electric pumps powered by cheap off-peak surplus wind/nuclear grid power to pump water back to the upper reservoir.",
                "Closed-loop design: The system recycles the same volume between upper and lower reservoirs with negligible water loss."
            ]
        },"""
content = content.replace('        "topic": "Civil & Electrical Engineering",', pump_mat, 1)

# 8. Multi chart
multi_mat = """        "topic": "Environmental Science & Land Management",
        "material": {
            "type": "image",
            "title": "Worldwide Agricultural Land Use and Deforestation Drivers",
            "imageUrl": "/images/writing/task1_multi_farmland_deforestation.svg",
            "imageDescription": (
                "Dual visual stimuli illustrating agricultural land expansion and deforestation catalysts:\\n"
                "• Bar Chart: Total global farmland area grew steadily from 42.0 million km² in 1980 to 43.2M (1990), 44.5M (2000), 46.1M (2010), and 48.0M km² in 2020 (+14.3% increase over 40 years).\\n"
                "• Pie Chart (Drivers of Tropical Deforestation):\\n"
                "  - Cattle livestock ranching: 41%\\n"
                "  - Commercial cash crops (oil palm, soy): 32%\\n"
                "  - Smallholder subsistence farming: 18%\\n"
                "  - Timber logging & urban transport infrastructure: 9%\\n"
                "• Combined commercial food production (cattle + commercial crops) caused 73% of all tropical deforestation."
            ),
            "keyDataPoints": [
                "Agricultural land expanded from 42 million sq km in 1980 to 48 million sq km in 2020.",
                "Commercial cattle ranching was the single greatest driver of deforestation (41%).",
                "Large-scale commercial crop cultivation accounted for 32% (oil palm, soy).",
                "Smallholder subsistence farming represented 18%, and logging/infrastructure comprised the remaining 9%."
            ]
        },"""
content = content.replace('        "topic": "Environmental Science & Land Management",', multi_mat, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated scripts/authentic_builder/writing_data.py with visual materials!")
