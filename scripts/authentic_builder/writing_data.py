"""
Authentic IELTS Writing Dataset Specification
Contains 28 high-caliber, fully developed IELTS Writing tasks:
- 8 Academic Task 1 (Bar Chart, Line Graph, Pie Chart, Table, Process Diagram, Map Redevelopment, Pumped Storage, Multi-chart)
- 6 General Training Task 1 (Formal, Semi-formal, Informal letters)
- 14 Task 2 (Opinion, Discussion, Problem-Solution, Advantages-Disadvantages, Two-Part)

All tasks include authentic prompts, comprehensive keyDataPoints / bulletPoints,
full 160-330 word authentic model essays, band ratings, and detailed examiner criteria highlights.
"""

WRITING_ITEMS = [
    # =========================================================================
    # ACADEMIC TASK 1 (8 Tasks)
    # =========================================================================
    {
        "id": "writ-acad-bar-01",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Global Renewable Energy Investment by Technology (2010–2023)",
        "topic": "Renewable Energy & Capital Allocation",
        "material": {
            "type": "image",
            "title": "Global Renewable Energy Investment by Technology (2010–2023)",
            "imageUrl": "/images/writing/task1_bar_chart_renewables.svg",
            "imageDescription": (
                "Bar chart showing annual global investment ($ billions) in Solar PV, Wind Energy, and Hydroelectric:\n"
                "• 2010: Wind $110bn, Solar $85bn, Hydroelectric $55bn (Total: $250bn)\n"
                "• 2014: Wind $135bn, Solar $130bn, Hydroelectric $65bn (Peak for hydro; Total: $330bn)\n"
                "• 2018: Solar $180bn (surpasses wind), Wind $160bn, Hydroelectric $45bn (Total: $385bn)\n"
                "• 2023: Solar $320bn (steepest rise), Wind $215bn, Hydroelectric $38bn (Total: $573bn)"
            ),
            "keyDataPoints": [
                "Solar PV expanded dramatically from $85 billion in 2010 to a peak of $320 billion in 2023, surpassing all other sectors.",
                "Wind energy exhibited consistent upward trajectory from $110 billion in 2010 to $215 billion by 2023.",
                "Hydroelectric power saw volatile investments, peaking at $65 billion in 2014 before steadily waning to $38 billion in 2023.",
                "Overall total renewable capital deployment more than doubled over the thirteen-year timeframe."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "bar_chart",
            "prompt": "The bar chart illustrates global capital investment (measured in billions of US dollars) across three major renewable energy sectors—Solar Photovoltaic, Wind Energy, and Hydroelectric Power—between 2010 and 2023 at four-year intervals.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Solar PV expanded dramatically from $85 billion in 2010 to a peak of $320 billion in 2023, surpassing all other sectors.",
                "Wind energy exhibited consistent upward trajectory from $110 billion in 2010 to $215 billion by 2023.",
                "Hydroelectric power saw volatile investments, peaking at $65 billion in 2014 before steadily waning to $38 billion in 2023.",
                "Overall total renewable capital deployment more than doubled over the thirteen-year timeframe."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The bar chart delineates the volume of international capital deployed into solar, wind, "
                "and hydroelectric energy infrastructure over a thirteen-year timeframe spanning from 2010 to 2023.\n\n"
                "Overall, it is immediately apparent that global investment in renewable energy expanded substantially, "
                "predominantly propelled by exponential expenditure in solar photovoltaics. Conversely, while wind power "
                "demonstrated sustained and stable growth, hydroelectric allocations experienced a notable long-term contraction.\n\n"
                "In 2010, wind power led global financing at $110 billion, closely followed by solar energy at $85 billion, "
                "whereas hydroelectricity accounted for a modest $55 billion. By 2014, hydroelectric funding reached its apex "
                "at $65 billion; however, it subsequently entered a secular decline, tumbling to $45 billion in 2018 and "
                "concluding at just $38 billion in 2023.\n\n"
                "In stark contrast, solar photovoltaic investments surged remarkably, more than doubling to $180 billion by 2018 "
                "before skyrocketing to $320 billion in 2023, establishing it as the undisputed dominant sector. Meanwhile, "
                "capital allocations toward wind turbine infrastructure grew progressively, crossing the $150 billion threshold "
                "in 2018 and ultimately settling at $215 billion in 2023."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Full reporting of all three energy sectors with precise figures, clear overview highlighting overall surge and divergent sector trajectories.",
                "coherenceCohesion": "Exemplary logical paragraphing, sophisticated comparative transitions ('In stark contrast', 'Conversely', 'In 2010').",
                "lexicalResource": "Rich domain-specific vocabulary: 'secular decline', 'apex', 'capital deployed', 'photovoltaic', 'contracted'.",
                "grammaticalRange": "Complex sentential architecture incorporating participial clauses, compound comparative structures, and flawless passive phrasing."
            }
        }
    },
    {
        "id": "writ-acad-line-02",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Smartphone Adoption and Screen Time Across Age Demographics (2012–2022)",
        "topic": "Technology & Sociological Demographics",
        "material": {
            "type": "image",
            "title": "Smartphone Adoption Across Age Demographics (2012–2022)",
            "imageUrl": "/images/writing/task1_line_graph_smartphones.svg",
            "imageDescription": (
                "Line graph tracing smartphone adoption (% of population using smartphones daily) across four age brackets from 2012 to 2022:\n"
                "• 18–29 years: 72% in 2012, 81% in 2014, 87% in 2016, 91% in 2018, 95% in 2020, 98% in 2022 (near total saturation)\n"
                "• 30–49 years: 54% in 2012, 63% in 2014, 73% in 2016, 81% in 2018, 88% in 2020, 92% in 2022\n"
                "• 50–64 years: 31% in 2012, 42% in 2014, 60% in 2016, 68% in 2018, 74% in 2020, 80% in 2022\n"
                "• 65+ years: 14% in 2012, 22% in 2014, 33% in 2016, 43% in 2018, 50% in 2020, 58% in 2022 (quadrupled over decade)"
            ),
            "keyDataPoints": [
                "18–29 demographic commenced highest in 2012 at 72% and neared saturation at 98% by 2022.",
                "30–49 cohort escalated from 54% in 2012 to 92% in 2022.",
                "50–64 cohort rose steeply from 31% to 80% over the ten-year period.",
                "Senior cohort (65+) exhibited the fastest relative surge, quadrupling from 14% in 2012 to 58% in 2022."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "line_graph",
            "prompt": "The line graph displays the percentage of individuals who owned and daily utilized smartphones across four distinct age demographics (18–29, 30–49, 50–64, and 65+) in a European nation from 2012 to 2022.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "18–29 demographic commenced highest in 2012 at 72% and neared saturation at 98% by 2022.",
                "30–49 cohort escalated from 54% in 2012 to 92% in 2022.",
                "50–64 cohort rose steeply from 31% to 80% over the ten-year period.",
                "Senior cohort (65+) exhibited the fastest relative surge, quadrupling from 14% in 2012 to 58% in 2022."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The line graph traces the proportion of smartphone ownership and daily usage across four age groups "
                "in a selected European country between 2012 and 2022.\n\n"
                "Overall, smartphone adoption increased markedly across every surveyed demographic over the decade. "
                "While younger cohorts consistently registered the highest penetration rates and approached near-total saturation, "
                "the elderly demographic demonstrated the most dramatic relative expansion.\n\n"
                "In 2012, approximately 72% of young adults aged 18 to 29 owned and operated smartphones, followed by 54% "
                "of those aged 30 to 49. Both cohorts recorded sustained upward momentum throughout the decade: by 2018, "
                "the 18–29 bracket had climbed to 91% before plateauing at 98% in 2022, whilst the 30–49 group followed a similar "
                "trajectory, culminating at 92%.\n\n"
                "Conversely, ownership was considerably lower among older generations at the outset, standing at 31% for 50–64-year-olds "
                "and a mere 14% for seniors aged 65 and above. However, the 50–64 group witnessed substantial acceleration, "
                "rising to 60% in 2016 and terminating at 80% in 2022. Remarkably, the 65+ demographic quadrupled over the timeframe, "
                "climbing steadily to reach 58% by 2022, thereby substantially narrowing the intergenerational technology gap."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Identifies both absolute dominance of younger cohorts and greatest proportional gain of the senior bracket with exact figures.",
                "coherenceCohesion": "Cohesive progression moving from overall overview to younger brackets then older demographics.",
                "lexicalResource": "Academic phrasing: 'near-total saturation', 'quadrupled', 'plateauing', 'intergenerational gap'.",
                "grammaticalRange": "Accurate coordination of time phrases, non-finite clauses, and parallel comparative clauses."
            }
        }
    },
    {
        "id": "writ-acad-pie-03",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "easy",
        "band": "Band 7.0–8.0",
        "granularity": "drill",
        "title": "Household Energy Consumption Breakdown in the UK (1990 vs 2020)",
        "topic": "Energy Economics & Domestic Utilities",
        "material": {
            "type": "image",
            "title": "Household Energy Consumption Breakdown in the UK (1990 vs 2020)",
            "imageUrl": "/images/writing/task1_pie_chart_energy.svg",
            "imageDescription": (
                "Two pie charts comparing proportional distribution of domestic energy end-use demands in the UK:\n"
                "• Space heating: 52% (1990) -> 46% (2020) (remains primary energy sink)\n"
                "• Water heating: 24% (1990) -> 17% (2020) (decreased by 7 percentage points)\n"
                "• Electronic consumer appliances: 13% (1990) -> 26% (2020) (exactly doubled, emerging as second largest sector)\n"
                "• Cooking: 7% (1990) -> 6% (2020)\n"
                "• Lighting: 4% (1990) -> 5% (2020)"
            ),
            "keyDataPoints": [
                "Space heating constituted the largest single energy sink in both years (52% in 1990, decreasing slightly to 46% in 2020).",
                "Water heating dropped from 24% to 17% due to modern boiler insulation.",
                "Electronic consumer appliances doubled from 13% to 26%, becoming the second largest consumer.",
                "Cooking and lighting both saw modest reductions (cooking: 7% to 6%; lighting: 4% to 5%)."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "pie_chart",
            "prompt": "The two pie charts compare the proportional distribution of household energy consumption across five main categories in the United Kingdom in 1990 and 2020.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Space heating constituted the largest single energy sink in both years (52% in 1990, decreasing slightly to 46% in 2020).",
                "Water heating dropped from 24% to 17% due to modern boiler insulation.",
                "Electronic consumer appliances doubled from 13% to 26%, becoming the second largest consumer.",
                "Cooking and lighting both saw modest reductions (cooking: 7% to 6%; lighting: 4% to 5%)."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "The two pie charts delineate how domestic energy was consumed across five distinct household categories "
                "in the United Kingdom in the years 1990 and 2020.\n\n"
                "Overall, space heating represented the predominant energy expenditure in both surveyed years despite "
                "recording a modest decrease. In contrast, electrical consumer appliances exhibited the most substantial growth, "
                "doubling its proportion and emerging as the second most demanding sector by 2020.\n\n"
                "In 1990, more than half of all residential energy (52%) was consumed by space heating. Although this figure "
                "moderated over the thirty-year span, it remained the primary consumer in 2020 at 46%. Water heating constituted "
                "the second largest requirement in 1990 at roughly a quarter (24%), but experienced a significant reduction "
                "down to 17% by 2020.\n\n"
                "Conversely, power dedicated to operating home electrical appliances grew exponentially from 13% in 1990 "
                "to exactly 26% in 2020, representing an exact two-fold surge. The remaining energy allocations registered "
                "negligible variations: cooking slipped marginally from 7% to 6%, while domestic lighting accounted for 4% in 1990 "
                "and 5% in 2020."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly highlights the dominance of space heating alongside the dramatic expansion of consumer electronics.",
                "coherenceCohesion": "Smooth logical transitions ('Overall', 'In 1990', 'Conversely', 'The remaining energy allocations').",
                "lexicalResource": "Natural range of vocabulary: 'predominant', 'energy expenditure', 'moderated', 'negligible variations'.",
                "grammaticalRange": "Diverse structure utilizing concessions, compound sentences, and varied noun phrases."
            }
        }
    },
    {
        "id": "writ-acad-table-04",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "International Tertiary Student Enrolment Across Five Academic Disciplines",
        "topic": "Higher Education & Global Student Mobility",
        "material": {
            "type": "image",
            "title": "International Tertiary Student Enrolment Across Five Academic Disciplines",
            "imageUrl": "/images/writing/task1_table_university.svg",
            "imageDescription": (
                "Table comparing international student enrolment (2015 vs 2023), percentage growth, retention, and graduation rates at an Australian university:\n"
                "• Computer Science: 1,240 (2015) -> 3,850 (2023), Growth: +210.5%, Retention: 93%, Completion: 91%\n"
                "• Business & Finance: 4,200 (2015) -> 5,600 (2023), Growth: +33.3%, Retention: 88%, Completion: 86%\n"
                "• Engineering & Technology: 2,100 (2015) -> 3,150 (2023), Growth: +50.0%, Retention: 95%, Completion: 94%\n"
                "• Humanities & Social Sciences: 1,850 (2015) -> 1,200 (2023), Growth: -35.1%, Retention: 74%, Completion: 71%\n"
                "• Medicine & Health Sciences: 950 (2015) -> 1,120 (2023), Growth: +17.9%, Retention: 96%, Completion: 93%"
            ),
            "keyDataPoints": [
                "Computer Science had the steepest surge in student enrolment, soaring from 1,240 in 2015 to 3,850 in 2023 (+210%), with 91% retention.",
                "Business & Finance enrolled the largest overall student body (4,200 in 2015 to 5,600 in 2023) with an 88% retention rate.",
                "Engineering expanded from 2,100 to 3,150 students, maintaining the highest completion rate at 94%.",
                "Humanities & Arts experienced an absolute decline from 1,850 to 1,200 students (-35%) with the lowest retention at 74%."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "table",
            "prompt": "The table compares the number of international students enrolled in five academic departments at a major Australian university in 2015 and 2023, along with their retention and completion rates.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Computer Science had the steepest surge in student enrolment, soaring from 1,240 in 2015 to 3,850 in 2023 (+210%), with 91% retention.",
                "Business & Finance enrolled the largest overall student body (4,200 in 2015 to 5,600 in 2023) with an 88% retention rate.",
                "Engineering expanded from 2,100 to 3,150 students, maintaining the highest completion rate at 94%.",
                "Humanities & Arts experienced an absolute decline from 1,850 to 1,200 students (-35%) with the lowest retention at 74%."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The table quantifies overseas student admissions across five university departments at an Australian institution "
                "in 2015 and 2023, alongside their corresponding course retention and degree completion percentages.\n\n"
                "Overall, tertiary international enrolment expanded across almost all faculties, led by massive growth in Computer "
                "Science and Business. Furthermore, technical STEM disciplines consistently achieved superior retention and completion "
                "metrics compared to the creative arts.\n\n"
                "Business and Finance enrolled the largest cohort in both benchmark years, rising from 4,200 scholars in 2015 to 5,600 "
                "in 2023, while sustaining a commendable 88% retention rate. Nevertheless, Computer Science recorded the most remarkable "
                "rate of expansion, more than tripling from 1,240 to 3,850 students (+210%) and securing a 91% completion rate. Similarly, "
                "Engineering matriculations rose from 2,100 to 3,150, achieving the university's apex retention score of 94%.\n\n"
                "In stark contrast, Humanities and Social Sciences witnessed an absolute contraction in international interest, tumbling "
                "from 1,850 candidates to 1,200 by 2023. This faculty also registered the lowest academic retention at 74%. Lastly, Medicine "
                "and Health Sciences preserved highly regulated, competitive cohorts, increasing moderately from 950 to 1,120 while delivering "
                "an exceptional 93% graduation rate."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Comprehensive coverage of raw volume shifts, percentage multipliers, and academic outcome statistics.",
                "coherenceCohesion": "Clear structural contrast between booming STEM/Business faculties and declining Humanities.",
                "lexicalResource": "Precise terms: 'matriculations', 'apex retention', 'securing', 'absolute contraction'.",
                "grammaticalRange": "Accurate balance of past perfect, comparative adverbs, and participial clauses."
            }
        }
    },
    {
        "id": "writ-acad-proc-05",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Industrial Lithium-Ion Battery Recycling Procedure",
        "topic": "Chemical Engineering & Circular Economy",
        "material": {
            "type": "image",
            "title": "Industrial Lithium-Ion Battery Recycling Procedure",
            "imageUrl": "/images/writing/task1_proc_battery_recycling.svg",
            "imageDescription": (
                "Process flowchart outlining five industrial recycling stages for spent EV lithium-ion battery packs:\n"
                "• Stage 1 (Dismantling & Shredding): Automated electrical discharge followed by cryogenic shredding in hermetically sealed inert Argon atmosphere.\n"
                "• Stage 2 (Physical Separation): Air classification & magnetic sieving separate plastic and metal casings from cathode 'black mass'.\n"
                "• Stage 3 (Acid Leaching): Black mass dissolved in heated 80°C sulfuric acid (H2SO4) and hydrogen peroxide (H2O2) leaching solution.\n"
                "• Stage 4 (Precipitation & Calcination): Multi-stage pH neutralization and thermal calcination furnaces.\n"
                "• Stage 5 (High-Purity Output): 98.5% pure Lithium Carbonate (Li2CO3), Nickel Hydroxide (Ni(OH)2), and Cobalt Sulfate (CoSO4) crystals ready for new battery cells."
            ),
            "keyDataPoints": [
                "Stage 1: Mechanical disassembly and automated cryogenic shredding under an inert argon blanket to prevent thermal runaway.",
                "Stage 2: Density separation and hydrometallurgical acid leaching using sulfuric acid and hydrogen peroxide.",
                "Stage 3: Chemical precipitation and calcination to regenerate cathode precursor salts (nickel, cobalt, lithium carbonate) at 98.5% purity."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "process_diagram",
            "prompt": "The diagram illustrates the industrial stages involved in recovering battery-grade metals and precursor compounds from spent automotive lithium-ion battery packs.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Stage 1: Mechanical disassembly and automated cryogenic shredding under an inert argon blanket to prevent thermal runaway.",
                "Stage 2: Density separation and hydrometallurgical acid leaching using sulfuric acid and hydrogen peroxide.",
                "Stage 3: Chemical precipitation and calcination to regenerate cathode precursor salts (nickel, cobalt, lithium carbonate) at 98.5% purity."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The schematic illustrates the sequential industrial phases through which decommissioned automotive lithium-ion battery "
                "modules are systematically recycled into battery-grade chemical precursors.\n\n"
                "Overall, the procedure encompasses three core operational stages: initial mechanical dismantling and cryogenic shredding, "
                "followed by hydrometallurgical acid dissolution, and concluding with selective chemical precipitation to yield purified raw materials.\n\n"
                "In the introductory phase, retired battery modules undergo automated electrical discharging to eliminate residual stored energy. "
                "The safe modules are then fed into high-torque shredders operating inside a hermetically sealed chamber filled with inert argon gas, "
                "a preventative measure to forestall spontaneous thermal combustion. Physical sieving and air classification subsequently separate "
                "heavy metallic casings and plastic polymers from the fine 'black mass' powder containing the cathode elements.\n\n"
                "In the hydrometallurgical extraction phase, this black mass is immersed in heated sulfuric acid blended with hydrogen peroxide, "
                "thereby leaching lithium, nickel, cobalt, and manganese into a concentrated aqueous sulfate solution. Finally, targeted chemical "
                "reagents and thermal calcination induce step-by-step precipitation, extracting cobalt crystals, nickel hydroxide, and lithium carbonate "
                "at 98.5% chemical purity, ready for immediate manufacturing reintroduction."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly identifies all three stages from physical shredding through hydrometallurgical leaching to chemical precipitation.",
                "coherenceCohesion": "Flawless sequential connectors: 'In the introductory phase', 'subsequently', 'In the hydrometallurgical extraction phase', 'Finally'.",
                "lexicalResource": "Advanced chemical engineering lexicon: 'cryogenic shredding', 'hydrometallurgical', 'black mass', 'calcination', 'precursor'.",
                "grammaticalRange": "Mastery of the present passive voice essential for academic process descriptions."
            }
        }
    },
    {
        "id": "writ-acad-map-06",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Urban Redevelopment of Port Haven Industrial Docks (2000 vs Present)",
        "topic": "Urban Planning & Waterfront Renewal",
        "material": {
            "type": "image",
            "title": "Port Haven Waterfront Redevelopment: 2000 vs Present",
            "imageUrl": "/images/writing/task1_map_port_haven.svg",
            "imageDescription": (
                "Two layout plans illustrating structural transformation of Port Haven waterfront from 2000 to Present:\n"
                "• North: Derelict timber warehouses and freight cranes demolished and replaced by 400-unit luxury apartment towers and a public art museum.\n"
                "• Center: Commercial container shipping canal dredged and converted into a recreational yacht marina flanked by a pedestrian boardwalk promenade and cafes.\n"
                "• South: Industrial freight rail sidings converted into a modern electrified light rail transit terminus with direct 15-minute connection to the CBD.\n"
                "• East: Former agricultural farmland transformed into a protected public nature reserve wetland with walking trails."
            ),
            "keyDataPoints": [
                "Northern heavy cargo dock and derelict timber warehouses were razed and replaced by luxury residential apartment complexes and a public art gallery.",
                "Central commercial shipping canal was converted into a recreational yacht marina bordered by a pedestrian promenade and restaurants.",
                "Southern industrial railyard was replaced by a modern light rail transit terminus connecting directly to the central business district.",
                "Eastern farmland was converted into a public nature reserve and botanical wetland park."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "map_plan",
            "prompt": "The two plans depict the structural changes that have occurred at the maritime port of Port Haven between the year 2000 and the present day.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Northern heavy cargo dock and derelict timber warehouses were razed and replaced by luxury residential apartment complexes and a public art gallery.",
                "Central commercial shipping canal was converted into a recreational yacht marina bordered by a pedestrian promenade and restaurants.",
                "Southern industrial railyard was replaced by a modern light rail transit terminus connecting directly to the central business district.",
                "Eastern farmland was converted into a public nature reserve and botanical wetland park."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The two architectural maps delineate the extensive urban transformation of Port Haven, comparing its layout "
                "in the year 2000 with its present-day configuration.\n\n"
                "Overall, the site has transitioned completely from an active, heavy industrial cargo hub into a modern, mixed-use "
                "residential, recreational, and environmental precinct, marked by enhanced public transport accessibility.\n\n"
                "In 2000, the northern sector was dominated by heavy shipping cranes and several disused timber warehouses. These industrial "
                "structures have since been completely demolished to make way for multi-storey residential apartment blocks, alongside an "
                "exclusive public art museum. The central deep-water canal, which was previously utilized by bulk container vessels, has "
                "been redeveloped into a recreational yacht marina, now flanked by a tree-lined pedestrian esplanade and commercial cafes.\n\n"
                "Significant infrastructure changes also occurred in the southern and eastern regions. The southern heavy freight rail sidings "
                "were decommissioned and rebuilt into an electrified light rail passenger station, providing rapid direct transit to the downtown core. "
                "Simultaneously, the agricultural land on the eastern perimeter was transformed into a protected public nature wetland with walking trails, "
                "significantly increasing public green space."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Full depiction of changes across all compass directions (north, central, south, east) with clear before/after contrasts.",
                "coherenceCohesion": "Spatial progression from north to central canal to south and east.",
                "lexicalResource": "Superb architectural and spatial vocabulary: 'precinct', 'decommissioned', 'electrified light rail', 'perimeter', 'esplanade'.",
                "grammaticalRange": "Flawless deployment of present perfect passive ('have since been completely demolished') and past passive forms."
            }
        }
    },
    {
        "id": "writ-acad-proc-07",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Closed-Loop Hydroelectric Pumped Storage Power Generation",
        "topic": "Civil & Electrical Engineering",
        "material": {
            "type": "image",
            "title": "Closed-Loop Hydroelectric Pumped Storage Power Station",
            "imageUrl": "/images/writing/task1_proc_pumped_storage.svg",
            "imageDescription": (
                "Technical schematic of closed-loop hydroelectric pumped storage facility illustrating dual day/night operational modes:\n"
                "• Mountain infrastructure: High-altitude upper mountain reservoir connected to lower catchment basin via a subterranean high-pressure penstock.\n"
                "• Powerhouse: Underground facility with reversible hydraulic turbine-generator / pump unit.\n"
                "• Daytime Peak Mode: High electricity demand -> water cascades downward under gravity through penstock, driving turbines to generate 500 MW for national grid.\n"
                "• Nighttime Off-Peak Mode: Low grid demand & cheap surplus nuclear/wind electricity -> turbines reverse to operate as high-capacity pumps, driving water back up penstock to refill upper reservoir.\n"
                "• Closed-loop design recycles 100% of water with zero consumptive depletion."
            ),
            "keyDataPoints": [
                "Daytime operation: Water flows downward from upper mountain reservoir through a subterranean penstock, spinning a turbine-generator to supply 500 MW to the electrical grid.",
                "Nighttime operation: Reversible turbines act as electric pumps powered by cheap off-peak surplus wind/nuclear grid power to pump water back to the upper reservoir.",
                "Closed-loop design: The system recycles the same volume between upper and lower reservoirs with negligible water loss."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "process_diagram",
            "prompt": "The diagram illustrates how a closed-loop pumped storage hydroelectric power station operates during peak daytime hours and off-peak nighttime hours.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Daytime operation: Water flows downward from upper mountain reservoir through a subterranean penstock, spinning a turbine-generator to supply 500 MW to the electrical grid.",
                "Nighttime operation: Reversible turbines act as electric pumps powered by cheap off-peak surplus wind/nuclear grid power to pump water back to the upper reservoir.",
                "Closed-loop design: The system recycles the same volume between upper and lower reservoirs with negligible water loss."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The diagram details the dual operating cycles of a closed-loop pumped storage hydroelectric facility, "
                "contrasting daytime electricity generation with nighttime replenishment pumping.\n\n"
                "Overall, the facility functions as a massive rechargeable water battery. It utilizes gravitational kinetic "
                "energy during daytime peak electricity demand and reverses the flow during off-peak night periods to recycle "
                "the identical volume of water.\n\n"
                "During high-demand daytime intervals, sluice gates at the elevated upper mountain reservoir are opened, releasing "
                "water down a steep subterranean penstock conduit. The gravitational rush of high-pressure water drives a subterranean "
                "hydraulic turbine, which spins an electrical generator capable of delivering 500 megawatts into the national grid. "
                "After passing the turbine, the discharge water collects in a low-altitude catchment basin.\n\n"
                "Conversely, during nighttime off-peak periods when grid electricity demand drops and pricing is low, the process is inverted. "
                "Surplus grid electricity, sourced from wind and nuclear generators, powers the reversible turbines in reverse mode as high-capacity "
                "pumps. These force the collected water back up through the penstock into the upper reservoir, restoring full gravitational potential "
                "ahead of the subsequent morning cycle."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly contrasts the dual operating states (daytime generation vs nighttime pumping) with exact mechanisms.",
                "coherenceCohesion": "Cohesive two-part body paragraphing divided cleanly by operational cycle.",
                "lexicalResource": "Technical vocabulary: 'gravitational kinetic energy', 'penstock conduit', 'subterranean', 'catchment basin'.",
                "grammaticalRange": "Accurate coordination of conditional and causal subordinate clauses."
            }
        }
    },
    {
        "id": "writ-acad-multi-08",
        "skill": "writing",
        "questionType": "task1_academic",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Worldwide Agricultural Land Use and Deforestation Drivers",
        "topic": "Environmental Science & Land Management",
        "material": {
            "type": "image",
            "title": "Worldwide Agricultural Land Use and Deforestation Drivers",
            "imageUrl": "/images/writing/task1_multi_farmland_deforestation.svg",
            "imageDescription": (
                "Dual visual stimuli illustrating agricultural land expansion and deforestation catalysts:\n"
                "• Bar Chart: Total global farmland area grew steadily from 42.0 million km² in 1980 to 43.2M (1990), 44.5M (2000), 46.1M (2010), and 48.0M km² in 2020 (+14.3% increase over 40 years).\n"
                "• Pie Chart (Drivers of Tropical Deforestation):\n"
                "  - Cattle livestock ranching: 41%\n"
                "  - Commercial cash crops (oil palm, soy): 32%\n"
                "  - Smallholder subsistence farming: 18%\n"
                "  - Timber logging & urban transport infrastructure: 9%\n"
                "• Combined commercial food production (cattle + commercial crops) caused 73% of all tropical deforestation."
            ),
            "keyDataPoints": [
                "Agricultural land expanded from 42 million sq km in 1980 to 48 million sq km in 2020.",
                "Commercial cattle ranching was the single greatest driver of deforestation (41%).",
                "Large-scale commercial crop cultivation accounted for 32% (oil palm, soy).",
                "Smallholder subsistence farming represented 18%, and logging/infrastructure comprised the remaining 9%."
            ]
        },
        "writingTask": {
            "taskType": "task1_academic",
            "academicVisualType": "multiple_charts",
            "prompt": "The bar chart shows total global agricultural land area (in millions of square kilometres) between 1980 and 2020, while the pie chart breaks down the primary drivers of tropical forest clearance over the same period.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
            "keyDataPoints": [
                "Agricultural land expanded from 42 million sq km in 1980 to 48 million sq km in 2020.",
                "Commercial cattle ranching was the single greatest driver of deforestation (41%).",
                "Large-scale commercial crop cultivation accounted for 32% (oil palm, soy).",
                "Smallholder subsistence farming represented 18%, and logging/infrastructure comprised the remaining 9%."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The bar chart tracks total global agricultural land area across four decades from 1980 to 2020, "
                "whilst the accompanying pie chart categorizes the principal economic catalysts behind tropical rainforest deforestation.\n\n"
                "Overall, global agricultural territory expanded steadily over the forty-year period. Furthermore, agricultural activities—specifically "
                "cattle livestock grazing and commercial cash-crop farming—were responsible for nearly three-quarters of all tropical deforestation.\n\n"
                "As illustrated by the bar chart, global farmland covered approximately 42 million square kilometres in 1980. This footprint "
                "experienced continuous growth, climbing to 44.5 million in 2000 and culminating at an all-time high of 48 million square kilometres "
                "by 2020, representing an overall increase of approximately 14%.\n\n"
                "Turning to the pie chart, beef cattle ranching constituted the primary driver of tree clearance, accounting for 41% of all "
                "forest destruction. Industrial-scale commercial agriculture (predominantly soy and palm oil plantations) was the second largest "
                "culprit at 32%. Taken together, commercial food production caused 73% of habitat clearance. By contrast, local subsistence farming "
                "contributed 18%, while commercial timber logging and urban transport infrastructure represented a combined 9% of total deforestation."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Accurately integrates data from both visual stimuli, synthesising the combined 73% impact of commercial food production.",
                "coherenceCohesion": "Clear linking between overall expansion in farmland and specific forest destruction drivers.",
                "lexicalResource": "Sophisticated vocabulary: 'catalysts', 'subsistence farming', 'commercial cash-crop', 'culprit'.",
                "grammaticalRange": "Diverse sentential structures with participial phrases ('Taken together...')."
            }
        }
    },

    # =========================================================================
    # GENERAL TRAINING TASK 1 (6 Tasks)
    # =========================================================================
    {
        "id": "writ-gen-form-01",
        "skill": "writing",
        "questionType": "task1_general",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Formal Complaint: International Flight Baggage Delay & Financial Compensation",
        "topic": "Consumer Rights & Aviation Services",
        "writingTask": {
            "taskType": "task1_general",
            "generalLetterType": "formal",
            "prompt": "You recently returned from an international flight during which your checked luggage was mislaid for four days, causing you considerable distress and out-of-pocket expenses.\n\nWrite a letter to the airline's customer service manager. In your letter:\n• Introduce your flight and booking details\n• Explain the inconvenience and specific expenses you incurred\n• State the financial reimbursement and remedial actions you expect",
            "bulletPoints": [
                "Provide booking reference (e.g., BA-74892), flight number, and route.",
                "Detail necessity purchases: professional business attire, emergency prescription medicine, and toiletries.",
                "Specify receipts attached for $420 and demand formal compensation policy application."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "Dear Customer Relations Manager,\n\n"
                "I am writing to register a formal complaint regarding the gross mishandling of my luggage on flight BA-249 "
                "from London Heathrow to Singapore Changi on November 3rd, under booking reference QA-88419.\n\n"
                "Upon arrival in Singapore, my checked suitcase failed to appear on the carousel. Despite filing an immediate "
                "Property Irregularity Report (PIR: SINBA10442), your baggage handling staff were unable to locate my possessions "
                "for four full days. This protracted delay caused severe disruption, as I was traveling to deliver a keynote lecture "
                "at an international medical conference. Consequently, I was compelled to make emergency purchases of formal business "
                "attire, essential toiletries, and prescription medications, amounting to $485.50 in out-of-pocket expenditure.\n\n"
                "Given that this incident arose from operational negligence on the part of your ground personnel, I expect full "
                "financial reimbursement of the $485.50 incurred. I have appended all itemized receipts along with a copy of my PIR documentation. "
                "Furthermore, in accordance with the Montreal Convention baggage liability limits, I request written confirmation of the remedial "
                "steps being taken within fourteen business days.\n\n"
                "I look forward to your prompt response and settlement of this matter.\n\n"
                "Yours faithfully,\n"
                "Dr. Alistair Vance"
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Every bullet point fully developed with plausible names, flight details, itemized monetary figures, and legal references.",
                "coherenceCohesion": "Exemplary formal letter conventions with logical paragraph transitions and clear communicative purpose.",
                "lexicalResource": "High register formal expressions: 'gross mishandling', 'protracted delay', 'operational negligence', 'appended'.",
                "grammaticalRange": "Complex syntax: non-finite clauses ('Given that this incident arose...'), subjunctive and conditional phrasing."
            }
        }
    },
    {
        "id": "writ-gen-semi-02",
        "skill": "writing",
        "questionType": "task1_general",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Semi-formal Notice: Urgent Boiler Breakdown in Rented Apartment",
        "topic": "Tenancy Rights & Property Maintenance",
        "writingTask": {
            "taskType": "task1_general",
            "generalLetterType": "semi_formal",
            "prompt": "You rent an apartment and the main combi-boiler has broken down in the middle of winter, leaving you without heating or hot water.\n\nWrite a letter to your landlord. In your letter:\n• Explain the exact nature and onset of the breakdown\n• Describe the severe impact on your household\n• Request an urgent inspection and professional repair within 24 hours",
            "bulletPoints": [
                "Apartment 4B, 12 Kensington Terrace; boiler failed on Sunday morning, displaying Error Code E-04.",
                "Freezing internal temperatures below 10°C, inability to shower or heat infant's nursery.",
                "Demand certified Gas Safe technician visit by Monday afternoon or notify intent to call emergency contractor."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "Dear Mr. Higgins,\n\n"
                "I am writing to notify you of a critical mechanical breakdown regarding the central heating and hot water system "
                "at Apartment 4B, 12 Kensington Terrace.\n\n"
                "On Sunday morning, December 10th, the wall-mounted combi-boiler shut down abruptly, flashing persistent error code E-04. "
                "Despite resetting the system according to the manufacturer's user manual, the pilot flame fails to ignite, leaving the "
                "unit completely inoperable.\n\n"
                "With outdoor temperatures currently plummeting below freezing, our indoor living conditions have become untenable. "
                "The apartment temperature has fallen to 9°C, and we are without any hot running water for cooking, sanitation, or bathing. "
                "This situation is particularly perilous as we have a seven-month-old infant in the residence.\n\n"
                "Under our residential tenancy agreement, heating infrastructure is the landlord's statutory maintenance responsibility. "
                "I must therefore request that you dispatch an accredited Gas Safe technician to inspect and rectify the boiler within the next "
                "24 hours. Should you be unable to arrange a certified contractor by 2:00 PM tomorrow, I will arrange an emergency call-out "
                "myself and deduct the certified invoice from next month's rental disbursement.\n\n"
                "Thank you for your immediate attention to this urgent welfare issue.\n\n"
                "Warm regards,\n"
                "Marcus Sterling"
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Firm yet courteous tone, setting clear deadlines and referencing statutory tenancy obligations.",
                "coherenceCohesion": "Cohesive flow from mechanical description to household consequence and required action.",
                "lexicalResource": "Precise vocabulary: 'untenable', 'statutory maintenance responsibility', 'disbursement', 'perilous'.",
                "grammaticalRange": "Balanced modal verbs and complex conditional clauses."
            }
        }
    },
    {
        "id": "writ-gen-infor-03",
        "skill": "writing",
        "questionType": "task1_general",
        "difficulty": "easy",
        "band": "Band 7.5–8.0",
        "granularity": "drill",
        "title": "Informal Letter: Inviting a Former University Friend to Stay for a Weekend",
        "topic": "Social Relationships & Leisure",
        "writingTask": {
            "taskType": "task1_general",
            "generalLetterType": "informal",
            "prompt": "You recently relocated to a scenic coastal town and would like to invite a former university roommate to visit you for a weekend.\n\nWrite a letter to your friend. In your letter:\n• Describe your new home and surrounding area\n• Suggest activities you could do together during their visit\n• Suggest suitable dates and transport arrangements",
            "bulletPoints": [
                "Moved to St. Ives, renovated cottage overlooking the harbor.",
                "Activities: Coastal trail hiking, seafood bistro dinner, sea-kayaking.",
                "Dates: Last weekend of next month; offer to pick up from regional train station."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "Dear Liam,\n\n"
                "I hope you're having a brilliant week! I'm thrilled to finally be settled into my new place in St. Ives, "
                "and I'm writing to invite you down for a long-overdue weekend catch-up.\n\n"
                "The cottage is a charming stone house perched right on a cliff overlooking the Atlantic harbor. The views from "
                "the guest room are breathtaking—you can literally hear the waves breaking against the seawall from your bed. "
                "The town itself has a vibrant, bohemian atmosphere, packed with quirky art galleries, cozy bakeries, and traditional seafood pubs.\n\n"
                "I've already mapped out some fantastic things for us to do. We could spend Saturday morning hiking along the South West "
                "Coast Path over to Zennor Head, followed by lunch at an incredible local fish bistro that serves fresh crab sandwiches. "
                "If the weather holds up on Sunday, we could even rent a couple of sea kayaks and explore the sheltered coves.\n\n"
                "Would the weekend of October 27th to 29th work for you? You can easily catch the direct train down from London Paddington, "
                "and I'll happily pick you up from the station. Let me know what you reckon!\n\n"
                "Best,\n"
                "David"
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Natural, warm, enthusiastic informal tone covering all three bullet points completely.",
                "coherenceCohesion": "Effortless informal transitions and colloquial phrasing ('what you reckon', 'long-overdue').",
                "lexicalResource": "Vivid sensory and descriptive language: 'perched right on a cliff', 'bohemian atmosphere', 'sheltered coves'.",
                "grammaticalRange": "Natural informal syntactic variety: dashes, exclamations, mixed modal expressions."
            }
        }
    },
    {
        "id": "writ-gen-form-04",
        "skill": "writing",
        "questionType": "task1_general",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Formal Application: Community Council Environmental Initiative Grant",
        "topic": "Civic Funding & Environmental Stewardship",
        "writingTask": {
            "taskType": "task1_general",
            "generalLetterType": "formal",
            "prompt": "Your local municipal council is offering financial grants for neighborhood environmental improvement projects. You wish to apply for funding to create a community rooftop pollinator garden.\n\nWrite a letter to the Municipal Environmental Grants Committee. In your letter:\n• Introduce your community group and the proposed rooftop garden project\n• Explain how the initiative will benefit local biodiversity and residents\n• Outline the requested funding amount and itemized budget allocation",
            "bulletPoints": [
                "Representing 'Green Oak Community Association'; project on disused public library rooftop.",
                "Native wildflower beds for endangered bees, educational workshops for neighborhood schoolchildren.",
                "Request $8,500: lightweight planter boxes, drip irrigation, safety railings, seeds."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "Dear Members of the Environmental Grants Committee,\n\n"
                "I am writing on behalf of the Green Oak Residents' Association to submit a formal grant application under the "
                "2024 Urban Biodiversity Initiative, in support of our proposed Community Rooftop Pollinator Garden at the Central District Library.\n\n"
                "Our proposal seeks to convert 450 square meters of barren, unused rooftop space into a biodiverse ecological sanctuary. "
                "By installing raised beds populated with indigenous flowering flora, the garden will establish critical feeding habitats for declining "
                "native bees and butterfly populations. Furthermore, the installation will deliver substantial social benefits, serving as an open-air "
                "classroom for local primary schools to study plant biology and urban ecology, while mitigating the surrounding urban heat island effect.\n\n"
                "To bring this initiative to fruition, we are requesting a grant allocation of $8,500. This capital would be systematically apportioned "
                "toward structural safety barriers ($3,200), modular lightweight planter reservoirs ($2,600), an automated solar-powered drip-irrigation "
                "rig ($1,500), and organic soil blends alongside perennial native seed stocks ($1,200). Ongoing maintenance will be voluntarily sustained "
                "by our sixty active association members.\n\n"
                "Thank you for considering our project, and we welcome the opportunity to present our architectural schematics at your upcoming hearing.\n\n"
                "Yours faithfully,\n"
                "Eleanor Shaw\n"
                "Chairperson, Green Oak Association"
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Comprehensive proposal fulfilling all criteria: background, community/ecological benefits, and itemized financial plan.",
                "coherenceCohesion": "Sophisticated formal structure with seamless connective devices.",
                "lexicalResource": "Advanced civic and environmental vocabulary: 'ecological sanctuary', 'indigenous flowering flora', 'apportioned', 'mitigating'.",
                "grammaticalRange": "Polished complex structures, passive infinitives, and participial clauses."
            }
        }
    },
    {
        "id": "writ-gen-semi-05",
        "skill": "writing",
        "questionType": "task1_general",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Semi-formal Notice: Request for Unpaid Sabbatical Leave for Academic Research",
        "topic": "Workplace Relations & Professional Development",
        "writingTask": {
            "taskType": "task1_general",
            "generalLetterType": "semi_formal",
            "prompt": "You wish to take a six-month unpaid sabbatical from your current employment to complete a specialized postgraduate research diploma.\n\nWrite a letter to your department director. In your letter:\n• State the purpose, qualification, and proposed duration of your sabbatical\n• Explain how your new qualifications will benefit the company\n• Propose a handover plan to cover your workload during your absence",
            "bulletPoints": [
                "Postgraduate Diploma in Applied Data Science at City University; duration: March 1st to August 31st.",
                "Acquired skills in predictive machine learning will directly benefit company's client analytics division.",
                "Cross-training senior colleague (Ms. Priya Patel) to assume client management; documentation completed."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "Dear Mr. Davenport,\n\n"
                "I am writing to formally request a six-month period of unpaid sabbatical leave, commencing on March 1st and concluding on August 31st, "
                "in order to undertake a full-time Postgraduate Diploma in Applied Data Science at the City University Institute of Technology.\n\n"
                "Having served as Senior Business Analyst here for over four years, I have recognized that our commercial clients increasingly "
                "require predictive machine learning analytics. This intensive program covers algorithmic forecasting, big data warehousing, and "
                "automated pipeline architecture. Upon my return in September, these advanced capabilities will directly enhance our department's "
                "service portfolio, enabling us to pitch for enterprise-tier analytics contracts that we currently outsource.\n\n"
                "To ensure that my absence does not compromise operational continuity, I have formulated a comprehensive transition roadmap. Over the "
                "past month, I have compiled exhaustive operating standard manuals for all my ongoing client accounts. Furthermore, my senior colleague, "
                "Ms. Priya Patel, has agreed to assume primary oversight of my portfolio, and we have scheduled a three-week cross-training phase throughout February.\n\n"
                "I would be grateful for the opportunity to discuss this proposal with you in person at your earliest convenience.\n\n"
                "Yours sincerely,\n"
                "Jonathan Reed"
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Presents a compelling business case highlighting company benefits alongside a responsible transition plan.",
                "coherenceCohesion": "Smooth logical argument progression from request to justification to risk mitigation.",
                "lexicalResource": "Business and technical vocabulary: 'sabbatical leave', 'predictive machine learning', 'operational continuity', 'transition roadmap'.",
                "grammaticalRange": "Flawless present perfect, modal conditional, and infinitive constructions."
            }
        }
    },
    {
        "id": "writ-gen-infor-06",
        "skill": "writing",
        "questionType": "task1_general",
        "difficulty": "easy",
        "band": "Band 7.5–8.0",
        "granularity": "drill",
        "title": "Informal Thanks: Expressing Gratitude for Hospitality to a Host Family",
        "topic": "Intercultural Exchange & Friendship",
        "writingTask": {
            "taskType": "task1_general",
            "generalLetterType": "informal",
            "prompt": "You recently spent two weeks staying with a friend's family in Canada during your holiday. You have returned home and wish to express your gratitude.\n\nWrite a letter to your friend's parents. In your letter:\n• Thank them warmly for their hospitality and kindness\n• Reminisce about specific memorable moments from your visit\n• Extend an open invitation for them to visit you in your home country",
            "bulletPoints": [
                "Returned safely to Sydney; express deep appreciation for their warmth.",
                "Highlight memorable experiences: homemade maple blueberry pancakes, Banff canoe excursion.",
                "Invite them to stay at your home in Sydney whenever they plan a trip to Australia."
            ],
            "minWords": 150,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "Dear Mr. and Mrs. Campbell,\n\n"
                "I just wanted to drop you a quick note to let you know that I arrived back home safely in Sydney yesterday, "
                "and to thank you from the bottom of my heart for your incredible hospitality over the past fortnight.\n\n"
                "Staying with your family in Calgary was undoubtedly the highlight of my entire overseas travels. You made me feel like "
                "a cherished family member from the moment I walked through your front door. I will never forget Mrs. Campbell's legendary "
                "homemade blueberry pancakes on Sunday mornings, nor the breathtaking afternoon we spent canoeing across the turquoise waters "
                "of Lake Louise in Banff. Your warmth and generosity made me feel so completely at home.\n\n"
                "Please know that whenever you and Mr. Campbell decide to take your dream trip to Australia, my spare bedroom in Sydney is "
                "permanently reserved for you! I would love nothing more than to show you around the harbor, take you down the coastal cliff paths, "
                "and treat you to a proper Aussie barbecue.\n\n"
                "Please give my warmest regards to Greg and the rest of the family.\n\n"
                "With warmest gratitude,\n"
                "Sophie Turner"
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Genuinely touching, warm, respectful informal tone hitting every bullet point with authentic memories.",
                "coherenceCohesion": "Emotional warmth and natural flow connecting gratitude to memories and future reciprocity.",
                "lexicalResource": "Natural expressive language: 'cherished family member', 'legendary homemade blueberry pancakes', 'proper Aussie barbecue'.",
                "grammaticalRange": "Conversational yet grammatically impeccable compound sentences and inversion structures."
            }
        }
    },

    # =========================================================================
    # TASK 2 (14 Academic & General Essays across 5 Core Categories)
    # =========================================================================
    {
        "id": "writ-t2-opin-01",
        "skill": "writing",
        "questionType": "task2_opinion",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Artificial Intelligence & White-Collar Professional Obsolescence",
        "topic": "Artificial Intelligence & Labor Economics",
        "writingTask": {
            "taskType": "task2_opinion",
            "essayCategory": "agree_disagree",
            "prompt": "Some economists predict that advances in artificial intelligence and autonomous generative systems will render the majority of white-collar professional careers obsolete within decades.\n\nTo what extent do you agree or disagree with this statement?",
            "bulletPoints": [
                "Introduction: Paraphrase prompt and state balanced thesis (disagree with complete obsolescence; agree roles will transform).",
                "Body 1: Routine cognitive tasks (paralegal discovery, bookkeeping, basic diagnostics) will indeed automate rapidly.",
                "Body 2: Uniquely human competencies (ethical jurisprudence, empathetic therapy, high-stakes diplomacy) cannot be replicated by algorithms.",
                "Conclusion: Synthesis that collaboration ('centaur workforces') rather than wholesale replacement will define the future."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "It is increasingly argued by certain economists that rapid advancements in artificial intelligence and cognitive automation "
                "will precipitate the wholesale obsolescence of white-collar professional occupations within the coming decades. While I concede "
                "that algorithmic tools will extinguish numerous repetitive analytical workflows, I largely disagree with the forecast of widespread "
                "human redundancy, as strategic discernment, ethical judgment, and interpersonal empathy remain irreproducible by machines.\n\n"
                "On the one hand, artificial neural networks undeniably possess an unparalleled capacity to digest vast unstructured data volumes "
                "and synthesize complex patterns far faster than human practitioners. In disciplines such as routine corporate law, financial auditing, "
                "and diagnostic radiology, automated models are already outperforming human counterparts at identifying contractual anomalies or "
                "detecting early-stage oncological malignancies. Consequently, entry-level paralegals, junior accountants, and clerical data processors "
                "face severe structural contraction. When organizations can execute quantitative discovery at near-zero marginal cost, purely procedural "
                "desk jobs will undoubtedly be phased out.\n\n"
                "Nevertheless, true professional excellence transcends mechanical pattern matching. High-stakes vocations inherently demand contextual "
                "wisdom, moral accountability, and human trust—qualities fundamentally beyond probabilistic silicon architectures. A court judge, for "
                "instance, must interpret constitutional intent and weigh societal ethos rather than simply computing statistical precedent. Similarly, "
                "medical oncology requires delivering terminal prognoses with genuine compassionate bedside manner, while corporate leadership demands "
                "motivating diverse human teams through existential corporate crises. In these spheres, algorithmic outputs serve as cognitive prostheses "
                "rather than human substitutes, elevating human professionals into higher-order supervisory and creative roles.\n\n"
                "In conclusion, while artificial intelligence will irrevocably eliminate routine cognitive drudgery, it will transform professional "
                "careers rather than obliterate them. The future workspace will belong to hybrid professionals who synergize algorithmic computational "
                "power with irreplaceable human empathy and ethical leadership."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Nuanced, fully developed position maintained throughout; directly addresses 'to what extent' with clear boundaries.",
                "coherenceCohesion": "Exemplary topic sentences, paragraph transitions ('On the one hand', 'Nevertheless', 'In conclusion'), and thematic unity.",
                "lexicalResource": "Exceptional academic register: 'precipitate wholesale obsolescence', 'cognitive prostheses', 'probabilistic silicon architectures'.",
                "grammaticalRange": "Wide range of complex structures executed with total flexibility and natural accuracy."
            }
        }
    },
    {
        "id": "writ-t2-opin-02",
        "skill": "writing",
        "questionType": "task2_opinion",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Government Subsidies for Universal Higher Education",
        "topic": "Educational Policy & Public Finance",
        "writingTask": {
            "taskType": "task2_opinion",
            "essayCategory": "agree_disagree",
            "prompt": "Many people believe that university education should be completely free for all students, funded entirely by the state through general taxation.\n\nTo what extent do you agree or disagree with this perspective?",
            "bulletPoints": [
                "Introduction: Outline debate regarding tuition-free tertiary schooling and state position (partially agree).",
                "Body 1: Societal advantages: Meritocracy, economic innovation, eradication of debt burdens.",
                "Body 2: Counter-arguments: Sovereign fiscal strain, subsidizing affluent demographics, proliferation of low-utility degrees.",
                "Conclusion: Advocate for a targeted hybrid model (free STEM/healthcare plus income-contingent loans)."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "The question of whether national governments should provide tuition-free tertiary education funded exclusively through taxpayer revenues "
                "remains a contentious socio-economic debate. While universal fee abolition fosters equal opportunity and stimulates national innovation, "
                "I contend that blanket state funding is fiscally regressive and unsustainable, and that public subsidies should instead target high-priority "
                "disciplines and underprivileged demographics.\n\n"
                "Proponents of universal free higher education rightly emphasize the democratizing effect of removing financial barriers. In many modern "
                "economies, spiraling university fees and predatory student loans force promising youths from low-income backgrounds to forego higher education "
                "or shoulder crippling debt for decades. By nationalizing tuition costs, as demonstrated by Nordic models, societies foster genuine meritocracy "
                "where academic aptitude rather than familial wealth dictates socioeconomic mobility. Moreover, an educated populace elevates civic participation, "
                "boosts technological productivity, and yields higher taxable revenues over graduates' working lifetimes, theoretically recouping state expenditure.\n\n"
                "However, an unconditional state-funded framework presents profound fiscal and structural dilemmas. Fully funding higher education places an "
                "enormous strain on national budgets, inevitably competing with vital infrastructure such as primary healthcare, eldercare, and early childhood "
                "education. Paradoxically, universal free tuition often functions as a regressive subsidy for the affluent, who already possess the private tutoring "
                "advantages to secure competitive university placements. Furthermore, when degrees carry zero direct financial cost, universities frequently face "
                "course commodification, producing legions of graduates in oversaturated disciplines with poor labor-market alignment.\n\n"
                "In conclusion, while the aspiration of universal tertiary access is noble, fully free university for every student is financially imprudent. "
                "Governments should instead adopt a calibrated strategy: providing 100% scholarship coverage for disadvantaged students and critical national shortages "
                "such as medicine, engineering, and teaching, while maintaining income-contingent graduate contributions for general degree paths."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly stated, well-reasoned qualification of the prompt with robust supporting arguments.",
                "coherenceCohesion": "Cohesive progression utilizing strong transitional sentences and clear internal logic.",
                "lexicalResource": "Domain-relevant academic expressions: 'fiscally regressive', 'predatory student loans', 'meritocracy', 'income-contingent'.",
                "grammaticalRange": "Skillful integration of concessive clauses, participial modifiers, and passive verb forms."
            }
        }
    },
    {
        "id": "writ-t2-disc-03",
        "skill": "writing",
        "questionType": "task2_discussion",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Universal Basic Income vs Targeted Social Welfare Assistance",
        "topic": "Socioeconomic Policy & Poverty Alleviation",
        "writingTask": {
            "taskType": "task2_discussion",
            "essayCategory": "discuss_both_views",
            "prompt": "Some economists argue that governments should establish an unconditional Universal Basic Income (UBI) for every adult citizen. Others maintain that targeted, means-tested welfare programs represent a more equitable and fiscally responsible mechanism.\n\nDiscuss both views and give your own opinion.",
            "bulletPoints": [
                "View 1: UBI eradicates bureaucratic stigma, cushions labor displacement from AI, guarantees baseline dignity.",
                "View 2: Means-tested welfare concentrates limited fiscal resources on the truly destitute, avoids hyper-inflationary risks.",
                "Author's View: Phased Negative Income Tax or targeted conditional safety net preserves sovereign solvency."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "As technological automation and economic polarization reshape contemporary labor markets, debate has intensified over the optimal "
                "architecture of sovereign social safety nets. While some advocates champion an unconditional Universal Basic Income (UBI) paid to all "
                "citizens regardless of wealth, others contend that targeted, means-tested welfare remains the only fiscally sound and equitable approach. "
                "This essay will examine both perspectives before articulating my support for targeted assistance.\n\n"
                "Advocates of Universal Basic Income emphasize its administrative elegance and radical empowerment of vulnerable citizens. Traditional "
                "welfare systems are notoriously burdened by sprawling bureaucratic overhead, intrusive surveillance of recipients, and the degrading "
                "stigma of means-testing. Furthermore, conventional conditional benefits often generate a 'welfare trap', where unemployed individuals "
                "are disincentivized from seeking low-wage work because doing so immediately terminates their state aid. An unconditional cash floor "
                "eliminates this barrier, provides an essential economic safety net during rapid automation transitions, and acknowledges unpaid caregiving "
                "and community volunteerism as socially valuable contributions.\n\n"
                "Conversely, proponents of means-tested assistance argue that universal disbursements represent an astonishingly inefficient and fiscally "
                "reckless deployment of public capital. Distributing identical monthly stipends to billionaire executives and impoverished families alike "
                "dilutes state resources, leaving insufficient funding for citizens with profound disabilities or chronic illnesses who require intensive, "
                "specialized care. Economists also caution that funding a truly livable universal payout would necessitate crippling tax hikes on the working "
                "middle class or trigger severe demand-pull inflation, ultimately eroding the purchasing power of the poor.\n\n"
                "In my view, while the philosophical premise of UBI is commendable, its practical execution would bankrupt national treasuries or starve "
                "targeted public services. A far more prudent model is a modernized, streamlined means-tested safety net, such as a Negative Income Tax, "
                "which channels maximum state resources directly to those beneath the poverty line while preserving work incentives and sovereign solvency."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Thoroughly examines both sides with balanced intellectual rigor before delivering a decisive, justified personal synthesis.",
                "coherenceCohesion": "Clear structural layout with impeccable inter-paragraph linking and cohesive signposting.",
                "lexicalResource": "Advanced economic vocabulary: 'administrative elegance', 'welfare trap', 'means-tested', 'demand-pull inflation', 'sovereign solvency'.",
                "grammaticalRange": "Exceptional variety: balanced compound-complex sentences, rhetorical contrasts, and absolute clarity."
            }
        }
    },
    {
        "id": "writ-t2-disc-04",
        "skill": "writing",
        "questionType": "task2_discussion",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Individual Consumer Habits vs State Regulation in Climate Mitigation",
        "topic": "Environmental Governance & Climate Action",
        "writingTask": {
            "taskType": "task2_discussion",
            "essayCategory": "discuss_both_views",
            "prompt": "Some believe that global environmental degradation can only be solved if individual consumers drastically alter their daily lifestyles and purchasing habits. Others argue that significant ecological progress requires strict governmental legislation and corporate regulation.\n\nDiscuss both views and give your own opinion.",
            "bulletPoints": [
                "View 1: Consumer power: Dietary shifts (plant-based), recycling, reducing aviation, driving market demand.",
                "View 2: Regulatory power: 100 fossil companies cause 70% emissions; only carbon taxes, green zoning, and legal bans scale fast enough.",
                "Author's View: Top-down regulatory mandates must establish the structural boundary within which consumer habits can become impactful."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "The escalating planetary climate emergency has sparked extensive debate regarding where the primary responsibility for ecological "
                "remediation resides. While one school of thought contends that environmental preservation hinges upon voluntary shifts in individual consumer "
                "lifestyles, another asserts that meaningful progress is unattainable without stringent governmental regulation of industrial polluters. "
                "This essay explores both perspectives before arguing that centralized state intervention is the indispensable catalyst.\n\n"
                "Those advocating for consumer-led action highlight the transformative power of aggregate market demand. When millions of citizens choose "
                "to adopt plant-rich diets, reduce personal air travel, minimize single-use plastics, and install domestic solar panels, they send powerful "
                "economic signals to corporations. The burgeoning global market for electric vehicles and plant-based proteins demonstrates how consumer "
                "ethos can compel multinational conglomerates to decarbonize their offerings. Proponents maintain that without bottom-up civic commitment, "
                "top-down environmental laws will inevitably encounter political resistance and non-compliance from an unwilling populace.\n\n"
                "Nevertheless, reliance on voluntary individual virtue is woefully insufficient to avert catastrophic warming. Empirical data indicates that "
                "a mere one hundred multinational fossil fuel enterprises account for over 70% of global industrial greenhouse emissions. An individual "
                "sorting household recycling cannot offset systemic industrial pollution, coal-fired power grids, or international shipping emissions. "
                "Only sovereign states possess the legislative authority to enforce binding carbon taxes, subsidize clean energy grid infrastructure, mandate "
                "circular economy standards, and legally ban destructive practices like deforestation. Regulatory frameworks establish structural boundaries "
                "that compel entire economic sectors to decarbonize rapidly.\n\n"
                "In conclusion, while conscientious lifestyle choices cultivate vital ecological consciousness, individual efforts remain negligible against "
                "the scale of industrial emissions. I firmly believe that strict state legislation must serve as the primary engine of environmental reform, "
                "creating the infrastructure and legal frameworks within which sustainable personal habits can genuinely flourish."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly develops both perspectives and presents a convincing personal opinion grounded in empirical realities.",
                "coherenceCohesion": "Exemplary structural progression with clear topic sentences and smooth linking expressions.",
                "lexicalResource": "Rich environmental policy terms: 'ecological remediation', 'aggregate market demand', 'decarbonize', 'circular economy standards'.",
                "grammaticalRange": "Accurate complex syntax including cleft sentences and dependent clauses."
            }
        }
    },
    {
        "id": "writ-t2-prob-05",
        "skill": "writing",
        "questionType": "task2_problem_solution",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Urban Sprawl, Congestion, and Loss of Green Space in Megacities",
        "topic": "Urban Planning & Environmental Infrastructure",
        "writingTask": {
            "taskType": "task2_problem_solution",
            "essayCategory": "causes_solutions",
            "prompt": "In many global metropolises, uncontrolled urban sprawl and reliance on private motor vehicles have created chronic traffic congestion, severe air pollution, and the destruction of surrounding green belts.\n\nWhat are the primary causes of this phenomenon, and what effective solutions can municipal governments implement?",
            "bulletPoints": [
                "Causes: Car-centric zoning laws, inadequate public transit subsidies, uncoordinated peripheral real estate speculation.",
                "Solutions: High-density Transit-Oriented Development (TOD), dynamic congestion charging zones, pedestrianized urban cores."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "Across the globe, rapid urbanization has resulted in low-density suburban sprawl, overwhelming municipal road networks "
                "and causing chronic vehicular gridlock, debilitating air pollution, and the erosion of surrounding rural ecosystems. This essay "
                "will examine the architectural and economic drivers underlying this crisis and propose viable interventions for city administrations.\n\n"
                "The root causes of urban sprawl and traffic congestion stem primarily from flawed twentieth-century urban planning and private automobile "
                "dependency. For decades, municipal zoning ordinances enforced strict spatial segregation between residential suburbs and commercial city centers, "
                "forcing millions of commuters to embark on lengthy daily journeys. Compounding this issue is chronic underinvestment in rapid public mass transit, "
                "which leaves suburban residents with no viable alternative to private car ownership. Furthermore, unregulated real estate speculation on city "
                "fringes continues to devour agricultural green belts, creating sprawling, low-density housing developments that are economically impractical "
                "to service with electrified rail or bus networks.\n\n"
                "To reverse this trajectory, municipal authorities must execute bold structural remedies centered on Transit-Oriented Development (TOD). "
                "Firstly, city planners should reform zoning codes to encourage high-density, mixed-use neighborhoods where residences, workplaces, and retail "
                "hubs coexist within walkable distances, often termed 'fifteen-minute cities'. Secondly, governments must divert highway expansion budgets "
                "into building integrated metro rail systems, dedicated bus rapid transit (BRT) lanes, and protected cycling corridors. Finally, metropolitan "
                "leaders should introduce dynamic urban congestion pricing, as pioneered in London and Singapore, directly penalizing private vehicle entry "
                "into central corridors and reinvesting toll revenues into public transport subsidies.\n\n"
                "In conclusion, unchecked urban expansion is driven by outdated car-centric zoning and public transit deficits. By implementing high-density "
                "mixed-use redevelopment alongside punitive congestion pricing and mass transit investment, contemporary metropolises can transform into "
                "sustainable, breathable, and human-centric urban spaces."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly identifies distinct causes and proposes realistic, concrete solutions with real-world examples (London, Singapore).",
                "coherenceCohesion": "Cohesive two-part body paragraphing divided cleanly between etiology (causes) and remedies (solutions).",
                "lexicalResource": "Sophisticated urban design terminology: 'low-density suburban sprawl', 'Transit-Oriented Development', 'zoning ordinances', 'congestion pricing'.",
                "grammaticalRange": "Complex, error-free sentences showing versatile use of relative clauses, non-finite clauses, and passive structures."
            }
        }
    },
    {
        "id": "writ-t2-prob-06",
        "skill": "writing",
        "questionType": "task2_problem_solution",
        "difficulty": "medium",
        "band": "Band 7.5–8.0",
        "granularity": "drill",
        "title": "Sedentary Lifestyles, Ultra-Processed Diets, and the Youth Health Crisis",
        "topic": "Public Health & Nutritional Policy",
        "writingTask": {
            "taskType": "task2_problem_solution",
            "essayCategory": "causes_solutions",
            "prompt": "In many developed and developing countries, childhood obesity and chronic lifestyle diseases among adolescents are rising at alarming rates.\n\nWhat are the primary causes of this health crisis, and what effective measures can be taken by families and policymakers?",
            "bulletPoints": [
                "Causes: Ubiquity of cheap hyper-palatable ultra-processed foods (high sugar/fat), excessive recreational screen time displacing active play.",
                "Solutions: Mandatory junk food advertising bans targeting children, sugar taxation, subsidizing school sports and nutrition education."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "In recent decades, an alarming surge in childhood obesity, pediatric type-2 diabetes, and juvenile cardiovascular risk factors "
                "has emerged across both affluent and developing societies. This troubling epidemic is fueled by the commercial proliferation of "
                "hyper-palatable ultra-processed foodstuffs and the displacement of physical activity by recreational screen time. Resolving this crisis "
                "demands decisive legislative intervention combined with domestic dietary reform.\n\n"
                "The fundamental drivers of declining adolescent health are twofold. Firstly, the contemporary food landscape is dominated by aggressively "
                "marketed, inexpensive convenience foods saturated with refined sugars, trans fats, and artificial additives. Food conglomerates exploit "
                "children's evolutionary preferences for caloric density through cartoon mascots and gamified smartphone advertising, establishing addictive "
                "dietary habits from early childhood. Simultaneously, the digital revolution has transformed youth leisure into an intensely sedentary "
                "experience. Video games, algorithmic social media platforms, and on-demand video streaming now consume hours of daily time that was previously "
                "dedicated to outdoor athletics, active commuting, and spontaneous playground games.\n\n"
                "Combating this pediatric health crisis requires a comprehensive multi-pronged strategy. At the macroeconomic level, national policymakers "
                "must implement fiscal disincentives, such as targeted taxation on sugar-sweetened beverages and ultra-processed snacks, utilizing the resulting "
                "revenues to subsidize fresh agricultural produce for lower-income households. Furthermore, governments should enforce stringent bans on junk-food "
                "advertising across children's digital media and television programming. Within the educational sector, schools must mandate daily physical "
                "education curriculums and ban commercial vending machines from campuses, replacing them with balanced, freshly prepared school meals. "
                "Concurrently, parents must establish firm domestic screen-time limits and cultivate family meal routines centered around whole foods.\n\n"
                "In conclusion, the youth health epidemic is an unnatural byproduct of commercial food exploitation and digital sedentariness. Through bold "
                "statutory regulations on food marketing and taxation, coupled with school and parental stewardship, societies can reclaim the metabolic "
                "well-being of the next generation."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Comprehensive analysis of both dietary and behavioral causes with actionable, multi-tiered solutions.",
                "coherenceCohesion": "Smooth logical progression with clear structural signposts ('Firstly', 'Simultaneously', 'At the macroeconomic level').",
                "lexicalResource": "Advanced public health vocabulary: 'hyper-palatable', 'caloric density', 'sedentary experience', 'fiscal disincentives'.",
                "grammaticalRange": "Varied complex sentence structures with accurate use of passive voice and participial phrases."
            }
        }
    },
    {
        "id": "writ-t2-adva-07",
        "skill": "writing",
        "questionType": "task2_advantages_disadvantages",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "The Global Transition to a Completely Cashless Society",
        "topic": "Financial Technology & Monetary Economics",
        "writingTask": {
            "taskType": "task2_advantages_disadvantages",
            "essayCategory": "advantages_outweigh",
            "prompt": "An increasing number of nations are transitioning toward a completely cashless society where all commercial transactions are conducted digitally.\n\nDo the advantages of this trend outweigh the disadvantages?",
            "bulletPoints": [
                "Advantages: Eliminates armed robbery/petty cash theft, curbs tax evasion and underground black markets, seamless commercial friction reduction.",
                "Disadvantages: Vulnerability to cyberattacks and power grid failures, financial exclusion of elderly/unbanked citizens, surveillance of privacy.",
                "Thesis: Advantages outweigh disadvantages provided statutory protections safeguard unbanked citizens and digital infrastructure."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "In recent years, breakthroughs in mobile payments, digital banking, and contactless payment gateways have accelerated the global shift "
                "toward a completely cashless economy. While this monetary evolution presents legitimate concerns regarding privacy surveillance and "
                "technological vulnerability, I believe the advantages in combating fiscal crime and streamlining economic velocity substantially outweigh "
                "the drawbacks.\n\n"
                "On the one hand, a fully digital transaction ecosystem introduces distinct social and technical risks. The primary drawback is the threat "
                "of financial disenfranchisement among vulnerable demographics. Elderly citizens, unhoused individuals, and impoverished rural residents "
                "often lack the smartphones, digital literacy, or formal bank accounts required to navigate cashless commerce, risking systemic marginalization. "
                "Moreover, a cashless infrastructure is acutely vulnerable to power grid disruptions, telecommunications blackouts, and malicious cyberattacks. "
                "If payment processing servers fail, entire national retail ecosystems can grind to an instantaneous halt. Lastly, digital transactions create "
                "an immutable electronic trail, enabling state agencies and commercial banking monopolies to surveil private consumer behavior, thereby "
                "eroding traditional personal privacy.\n\n"
                "Notwithstanding these valid concerns, the socio-economic benefits of cashless systems are profound. Foremost among them is the drastic "
                "curtailment of illicit financial networks. Physical cash is the lifeblood of tax evasion, money laundering, narcotics trafficking, and the "
                "unregistered shadow economy. By requiring electronic verification for all exchanges, governments can close massive tax loopholes, generating "
                "billions in legitimate sovereign revenue for public infrastructure. Furthermore, digital commerce eradicates physical currency logistics—such "
                "as printing, transporting, and securing paper banknotes—while virtually eliminating violent crimes like bank robberies and street muggings. "
                "For everyday consumers and business owners, the speed, transparency, and frictionless nature of instant digital clearing undeniably enhance "
                "economic productivity.\n\n"
                "In conclusion, while safeguards must be enacted to protect personal privacy and ensure cash alternatives for marginalized groups, the "
                "superior security, administrative efficiency, and transparency of digital payments render the cashless transition overwhelmingly beneficial."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Presents a balanced appraisal of both sides before firmly concluding that benefits outweigh risks with clear justification.",
                "coherenceCohesion": "Clear contrasting structures ('On the one hand', 'Notwithstanding these valid concerns', 'In conclusion').",
                "lexicalResource": "Domain-specific financial terminology: 'disenfranchisement', 'immutable electronic trail', 'shadow economy', 'frictionless nature'.",
                "grammaticalRange": "Sophisticated complex sentences combining noun clauses, conditionality, and concessive transitions."
            }
        }
    },
    {
        "id": "writ-t2-adva-08",
        "skill": "writing",
        "questionType": "task2_advantages_disadvantages",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "International Tourism as an Economic Engine in Developing Nations",
        "topic": "Global Economics & Cultural Anthropology",
        "writingTask": {
            "taskType": "task2_advantages_disadvantages",
            "essayCategory": "advantages_outweigh",
            "prompt": "In many developing nations, the expansion of international mass tourism has become a primary pillar of national economic development.\n\nDo the advantages of relying on international tourism outweigh the disadvantages?",
            "bulletPoints": [
                "Advantages: Foreign currency injection, rapid employment generation across hospitality/transport, funding infrastructure and wildlife preservation.",
                "Disadvantages: Environmental degradation of fragile biomes, cultural commodification, economic volatility ('leakage' to foreign resort chains).",
                "Thesis: Advantages outweigh drawbacks if managed through eco-tourism and retaining domestic capital."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "For many emerging economies, the development of international tourism has been embraced as a rapid shortcut to economic prosperity "
                "and job creation. However, while foreign visitor inflows generate indispensable foreign exchange reserves, this reliance also risks "
                "environmental degradation, cultural commodification, and economic vulnerability. In my assessment, the economic advantages outweigh the "
                "disadvantages only when tourism is sustainably regulated to preserve ecological and cultural assets.\n\n"
                "On the negative side, uncontrolled mass tourism can inflict catastrophic damage on host nations. Ecologically, the sudden influx of seasonal "
                "tourists frequently overwhelms fragile municipal ecosystems, accelerating coral reef destruction, water table depletion, and unmanageable "
                "plastic pollution in pristine coastal or mountain areas. Culturally, sacred indigenous rituals and architectural monuments risk being reduced "
                "to commercialized spectacles tailored for superficial tourist entertainment, thereby eroding authentic heritage. Furthermore, tourism is an "
                "inherently volatile industry, vulnerable to sudden geopolitical crises, pandemics, and global recessions. Developing nations that over-rely "
                "on foreign travelers face catastrophic economic collapse when tourist flows dry up, as witnessed during the global Covid-19 pandemic.\n\n"
                "Conversely, when properly harnessed, international tourism delivers unprecedented socioeconomic benefits that few other sectors can match. "
                "It serves as an immediate conduit for foreign currency injection, dramatically expanding national foreign exchange reserves and providing "
                "employment for millions of unskilled and semi-skilled workers in hospitality, transportation, and gastronomy. Moreover, tourism revenues "
                "often provide the primary economic justification and tax capital required to construct modern airports, paved highway networks, and water "
                "treatment utilities that directly uplift local living standards. Critically, in regions endowed with unique wildlife—such as East Africa—safari "
                "tourism provides the financial foundation for anti-poaching operations and national park preservation that would otherwise be unfundable.\n\n"
                "In conclusion, while over-reliance on unbridled mass tourism carries severe cultural and environmental liabilities, its power to eradicate "
                "poverty and finance national infrastructure is irreplaceable. Provided governments enforce strict visitor caps and reinvest revenues locally, "
                "the advantages of tourism decisively outweigh its disadvantages."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Deeply nuanced response evaluating both ecological/cultural threats and profound economic realities.",
                "coherenceCohesion": "Cohesive paragraph flow with seamless internal transitions and precise thematic balance.",
                "lexicalResource": "Exceptional descriptive vocabulary: 'conduit for foreign currency', 'unbridled mass tourism', 'cultural commodification', 'fragile municipal ecosystems'.",
                "grammaticalRange": "Mastery of complex grammar, non-restrictive relative clauses, and inversion."
            }
        }
    },
    {
        "id": "writ-t2-doub-09",
        "skill": "writing",
        "questionType": "task2_two_part",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Aging Demographics in Developed Nations: Economic Strain & Policy Interventions",
        "topic": "Demography & Public Healthcare Economics",
        "writingTask": {
            "taskType": "task2_two_part",
            "essayCategory": "double_question",
            "prompt": "In many developed nations, the proportion of elderly citizens is increasing rapidly while birth rates continue to decline.\n\nWhat socioeconomic challenges does an aging demographic structure present, and what measures can governments implement to address them?",
            "bulletPoints": [
                "Question 1 (Challenges): Shrinking tax base/labor shortages, ballooning public pension liabilities, overwhelming geriatric healthcare systems.",
                "Question 2 (Solutions): Raising retirement age gradually, encouraging female workforce participation, pro-family childcare subsidies, selective skilled immigration."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "Throughout the developed world, medical breakthroughs and elevated living standards have extended human longevity, while reproductive "
                "fertility rates have plunged well below the generational replacement threshold of 2.1 children per woman. This dramatic demographic "
                "transformation precipitates profound economic dilemmas, but targeted public policy interventions can mitigate the impending crisis.\n\n"
                "The primary socioeconomic challenges associated with an aging populace stem from a shrinking labor force paired with soaring fiscal liabilities. "
                "As the ratio of active taxpayers to retired pensioners contracts, national treasuries experience acute revenue deficits precisely when expenditures "
                "on state pensions, geriatric care, and specialized medical treatments for chronic degenerative illnesses escalate exponentially. Furthermore, "
                "widespread labor shortages in key sectors—such as manufacturing, logistics, and social eldercare—threaten to depress gross domestic product (GDP) "
                "growth and stifle corporate innovation. Simultaneously, younger generations bear an unsustainable tax burden to finance the welfare of their elders, "
                "exacerbating intergenerational friction.\n\n"
                "To counter these systemic strains, sovereign administrations must implement multi-pronged demographic and labor reforms. Firstly, governments "
                "should enact phased statutory adjustments to the official retirement age, aligning retirement eligibility with extended healthy life expectancy "
                "and incentivizing senior professionals to remain in flexible or consulting roles. Secondly, policymakers must overhaul family support infrastructure "
                "by offering heavily subsidized childcare, mandatory parental leave, and child tax credits, thereby alleviating the severe financial penalties "
                "that dissuade young couples from starting families. Finally, nations facing demographic deficits should embrace selective skilled immigration "
                "policies, actively welcoming qualified foreign professionals and caregivers to rejuvenate the domestic workforce and replenish sovereign tax coffers.\n\n"
                "In conclusion, an inverted demographic pyramid threatens economic solvency through labor deficits and skyrocketing healthcare costs. However, by "
                "combining delayed retirement incentives, pro-natalist childcare subsidies, and strategic skilled immigration, modern nations can effectively navigate "
                "this demographic transition."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Directly and fully answers both questions: distinct socioeconomic challenges and concrete policy solutions.",
                "coherenceCohesion": "Clear two-part body paragraph structure answering Question 1 in Body 1 and Question 2 in Body 2.",
                "lexicalResource": "Accurate demographic and economic terminology: 'generational replacement threshold', 'degenerative illnesses', 'pro-natalist', 'intergenerational friction'.",
                "grammaticalRange": "Polished complex sentence structures with varied clauses and natural cohesion."
            }
        }
    },
    {
        "id": "writ-t2-doub-10",
        "skill": "writing",
        "questionType": "task2_two_part",
        "difficulty": "medium",
        "band": "Band 7.5–8.0",
        "granularity": "drill",
        "title": "The Proliferation of Single-Person Households in Modern Cities",
        "topic": "Urban Sociology & Contemporary Lifestyles",
        "writingTask": {
            "taskType": "task2_two_part",
            "essayCategory": "double_question",
            "prompt": "In many modern cities, an unprecedented percentage of adults are choosing to live alone rather than in traditional nuclear families or shared households.\n\nWhy is this occurring, and is this a positive or negative development for society?",
            "bulletPoints": [
                "Question 1 (Why): Economic autonomy (especially for career women), delayed marriage, desire for individual personal space in high-stress careers.",
                "Question 2 (Evaluation): Largely positive for personal self-determination, though poses risks of social isolation and housing affordability pressure."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "In metropolitan centers across the globe, demographic censuses reveal an unprecedented surge in single-person households. This shift "
                "away from traditional multigenerational and nuclear living arrangements is propelled by evolving economic independence and sociocultural "
                "values. On balance, while solitary living presents psychological and environmental challenges, I consider it a predominantly positive "
                "manifestation of individual autonomy and gender equality.\n\n"
                "The primary catalysts for the rise of solo living are financial empowerment and delayed family formation. Historically, cohabitation was "
                "an economic necessity, particularly for women who lacked access to independent financial income. Today, widespread tertiary educational attainment "
                "and career opportunities have enabled both men and women to achieve financial self-sufficiency, liberating them from remaining in unhappy marriages "
                "or living with relatives for purely financial support. Concurrently, societal norms have decoupled adulthood from immediate marriage. Young professionals "
                "increasingly prioritize career consolidation, creative freedom, and personal autonomy during their twenties and thirties, choosing the privacy "
                "and peace of solitary living over the compromises inherent in shared domestic spaces.\n\n"
                "Regarding its broader societal impact, this phenomenon offers significant personal advantages despite certain collective drawbacks. On the one hand, "
                "a proliferation of solo residences intensifies urban housing shortages and increases per-capita carbon footprints, as each resident operates separate "
                "refrigerators, heating units, and appliances. Solitary living can also exacerbate feelings of alienation and chronic loneliness if individuals fail "
                "to maintain external social networks. Nevertheless, the ability to live independently is a profound indicator of human freedom. It nurtures personal "
                "resilience, self-reliance, and freedom from domestic coercion, particularly empowering women to author their own lives rather than submitting to "
                "patriarchal domestic expectations.\n\n"
                "In conclusion, the preference for solitary living is rooted in financial independence and cultural shifts toward individual self-actualization. "
                "Although it creates urban housing pressures, its role in fostering personal liberty and gender equality makes it a predominantly progressive development."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Clearly unpacks root causes (Question 1) and delivers a balanced, justified evaluation (Question 2).",
                "coherenceCohesion": "Cohesive transitions separating the causal analysis from the normative evaluation.",
                "lexicalResource": "Rich sociological vocabulary: 'multigenerational', 'financial self-sufficiency', 'domestic coercion', 'self-actualization'.",
                "grammaticalRange": "Smoothly controls concessive structures, noun clauses, and complex participial modifiers."
            }
        }
    },
    {
        "id": "writ-t2-opin-11",
        "skill": "writing",
        "questionType": "task2_opinion",
        "difficulty": "medium",
        "band": "Band 7.5–8.0",
        "granularity": "drill",
        "title": "Compulsory Arts and Music Education in Primary School Curriculums",
        "topic": "Primary Education & Cognitive Development",
        "writingTask": {
            "taskType": "task2_opinion",
            "essayCategory": "agree_disagree",
            "prompt": "Some educators argue that creative subjects such as music, drama, and visual arts should be compulsory components of primary school curriculums, on par with mathematics and science.\n\nTo what extent do you agree or disagree with this view?",
            "bulletPoints": [
                "Introduction: State complete agreement that creative arts are indispensable for balanced neurocognitive and emotional growth.",
                "Body 1: Cognitive and neurological benefits: Music enhances spatial-temporal reasoning and linguistic processing; painting fosters motor control.",
                "Body 2: Psychological and emotional development: Creative expression provides emotional outlets, empathy, and lateral thinking essential for STEM innovation.",
                "Conclusion: Reiterate that holistic education requires equal standing for creative arts alongside STEM."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "In contemporary educational discourse, there is an ongoing dispute regarding whether creative disciplines—such as visual art, instrumental "
                "music, and theatrical drama—should be granted mandatory status in primary curriculums alongside foundational STEM subjects like mathematics "
                "and science. I wholeheartedly agree with this perspective, as artistic instruction is not a frivolous indulgence, but an indispensable catalyst "
                "for cognitive development, creative problem-solving, and emotional resilience.\n\n"
                "From a neurological standpoint, engagement with the arts significantly amplifies children's overall intellectual capacity. Neuroscientific "
                "studies consistently demonstrate that learning to read musical notation and play an instrument stimulates bilateral brain activity, enhancing "
                "spatial-temporal reasoning and mathematical acuity. Similarly, visual arts—such as drawing, sculpture, and design—refine fine motor skills, "
                "visual-spatial awareness, and geometric intuition. Far from detracting from academic performance in scientific subjects, rigorous exposure to the "
                "arts actually bolsters the cognitive architecture required to excel in complex mathematical and analytical tasks.\n\n"
                "Furthermore, creative education cultivates essential non-cognitive competencies that traditional rote learning cannot foster. In theatrical "
                "drama and collective orchestral performance, children learn collaborative empathy, active listening, and public speaking confidence. Visual arts "
                "encourage divergent thinking—the ability to conceive multiple unconventional solutions to open-ended problems—which is the very bedrock of scientific "
                "innovation in the modern knowledge economy. Crucially, the arts provide young learners with a healthy cathartic outlet to process complex emotions "
                "and stress, nurturing mental well-being in an increasingly high-pressure academic environment.\n\n"
                "In conclusion, treating the arts as optional extracurricular hobbies undermines the holistic development of children. Creative education should be "
                "mandated as an essential core pillar of primary schooling, working in full synergy with scientific disciplines to nurture well-rounded, innovative, "
                "and emotionally resilient future citizens."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Unambiguous, enthusiastic stance maintained across cognitive and socio-emotional arguments.",
                "coherenceCohesion": "Exemplary thematic progression: neurological/intellectual merits in Body 1, non-cognitive/emotional merits in Body 2.",
                "lexicalResource": "Advanced educational vocabulary: 'bilateral brain activity', 'spatial-temporal reasoning', 'divergent thinking', 'holistic development'.",
                "grammaticalRange": "Complex, error-free sentence structures incorporating passive voice, dashes, and parallel phrases."
            }
        }
    },
    {
        "id": "writ-t2-disc-12",
        "skill": "writing",
        "questionType": "task2_discussion",
        "difficulty": "advanced",
        "band": "Band 8.0–8.5",
        "granularity": "drill",
        "title": "Space Exploration Funding vs Planetary Environmental Remediation",
        "topic": "Scientific Research & Resource Allocation",
        "writingTask": {
            "taskType": "task2_discussion",
            "essayCategory": "discuss_both_views",
            "prompt": "Some argue that governments should allocate billions of dollars to space exploration and interplanetary missions. Others contend that state resources should be prioritized exclusively to resolve urgent terrestrial challenges such as poverty, climate change, and environmental restoration.\n\nDiscuss both views and give your own opinion.",
            "bulletPoints": [
                "View 1: Space investment drives secondary technologies (satellite climate monitoring, GPS, solar efficiency) and long-term existential insurance.",
                "View 2: Immediate moral imperative to resolve terrestrial poverty, clean water, and global warming before exploring dead planets.",
                "Author's View: Space exploration should continue, but its funding must be integrated with direct climate observation and green tech breakthroughs."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The allocation of national scientific research budgets between extra-planetary exploration and immediate terrestrial welfare is a subject "
                "of fierce ethical and economic debate. While critics argue that spending billions on lunar and Martian expeditions is unconscionable while Earth "
                "grapples with poverty and climate destruction, proponents assert that space science yields indispensable technological breakthroughs. This essay "
                "will evaluate both arguments before presenting my own perspective.\n\n"
                "Those who advocate prioritizing Earth-bound challenges emphasize the urgent moral duty governments have toward their citizens. Millions of "
                "people globally continue to suffer from acute malnutrition, lack of potable drinking water, and inadequate primary healthcare. Furthermore, "
                "our terrestrial biosphere faces catastrophic ecological tipping points caused by rampant global warming, ocean acidification, and biodiversity "
                "collapse. From this perspective, spending vast sovereign revenues on sending rovers to barren, uninhabitable planets represents a frivolous "
                "vanity project, especially when those identical financial resources could immediately finance reforestation, clean water desalination, and the "
                "decarbonization of national energy grids.\n\n"
                "Conversely, champions of space exploration contend that its critics misunderstand the profound terrestrial dividends generated by aerospace "
                "innovation. The technological demands of space missions have historically catalyzed revolutionary spin-off technologies that transformed everyday "
                "life on Earth, including satellite telecommunications, advanced water purification filters, photovoltaic solar cells, and modern medical telemetry. "
                "Crucially, our entire modern understanding of planetary climate change—from Antarctic ozone depletion to rising sea levels—is derived almost "
                "exclusively from Earth-observation satellites designed by space agencies. Far from distracting from environmental protection, space science provides "
                "the vital sensory apparatus needed to diagnose and combat ecological degradation.\n\n"
                "In conclusion, while urgent terrestrial crises rightfully command the lion's share of public expenditure, abandoning space exploration would be "
                "short-sighted. I believe governments should maintain robust, targeted space programs that prioritize Earth-observation satellites and sustainable "
                "aerospace engineering, thereby harnessing the wonders of the cosmos to preserve our fragile home planet."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Sophisticated treatment of both sides; convincingly shows how space science directly contributes to solving Earth's climate crisis.",
                "coherenceCohesion": "Cohesive structural development with smooth contrasting discourse markers.",
                "lexicalResource": "Domain-rich scientific lexicon: 'extra-planetary exploration', 'ecological tipping points', 'spin-off technologies', 'photovoltaic solar cells'.",
                "grammaticalRange": "Masterful variety of conditional, passive, and complex sentences."
            }
        }
    },
    {
        "id": "writ-t2-prob-13",
        "skill": "writing",
        "questionType": "task2_problem_solution",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Juvenile Delinquency: Family Breakdown vs Socioeconomic Deprivation",
        "topic": "Criminology & Social Welfare",
        "writingTask": {
            "taskType": "task2_problem_solution",
            "essayCategory": "causes_solutions",
            "prompt": "In many urban areas, rates of juvenile delinquency and youth anti-social behavior are escalating.\n\nWhat are the primary causes of this trend, and what effective interventions can be undertaken to reintegrate troubled youths?",
            "bulletPoints": [
                "Causes: Domestic neglect/absentee parenting, lack of community youth infrastructure, gang recruitment in impoverished neighborhoods.",
                "Solutions: Community mentoring programs, restorative justice rather than incarceration, state funding for youth vocational apprenticeships."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.0",
            "sampleEssay": (
                "In many contemporary urban centers, escalating rates of juvenile delinquency, vandalism, and youth gang involvement represent a grave "
                "social crisis. This phenomenon is largely rooted in fractured domestic environments, educational disengagement, and socioeconomic "
                "deprivation. Mitigating this problem requires a shift away from punitive incarceration toward proactive community support, vocational "
                "training, and restorative justice.\n\n"
                "The genesis of youth anti-social behavior is rarely an innate criminal disposition; rather, it is symptomatic of systemic environmental "
                "failure. Firstly, dysfunctional or neglectful home environments—often exacerbated by parental substance abuse, domestic violence, or the "
                "intense economic pressures of working multiple low-wage jobs—leave adolescents without emotional stability or moral guidance. Lacking positive "
                "role models at home, vulnerable teenagers frequently seek validation and protection in street gangs. Secondly, chronic underfunding of public "
                "amenities in marginalized neighborhoods has eliminated youth clubs, recreational sports centers, and arts facilities, leaving idle adolescents "
                "susceptible to criminal street culture. Finally, educational systems that prioritize academic conformity often alienate non-academic students, "
                "pushing them toward truancy and petty crime.\n\n"
                "To reverse this trajectory, societies must deploy compassionate, evidence-based interventions. At the community level, governments should invest "
                "in accessible youth community hubs staffed by professional social workers and athletic mentors who provide structured after-school activities. "
                "Within the judicial system, authorities must replace harsh juvenile detention centers—which typically function as 'schools of crime'—with restorative "
                "justice diversion programs. These compel young offenders to confront the human impact of their actions, perform community restitution, and receive "
                "psychological counseling. Crucially, secondary schools must partner with industry to offer subsidized vocational apprenticeships in fields like "
                "carpentry, coding, and culinary arts, providing troubled youths with a viable pathway to financial dignity and legitimate employment.\n\n"
                "In conclusion, juvenile crime is the tragic consequence of familial breakdown and community neglect. By investing in after-school mentorship, "
                "restorative rehabilitation, and vocational pathways, societies can dismantle the pipelines to delinquency and empower troubled youths to become "
                "productive citizens."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Insightful criminology analysis examining root causes and proposing concrete rehabilitation over punitive detention.",
                "coherenceCohesion": "Cohesive layout with clear logical progression between etiology and solutions.",
                "lexicalResource": "Precise sociological terms: 'juvenile delinquency', 'innate criminal disposition', 'restorative justice', 'truancy'.",
                "grammaticalRange": "Fluid command of complex sentential constructions, dashes, and participial phrases."
            }
        }
    },
    {
        "id": "writ-t2-adva-14",
        "skill": "writing",
        "questionType": "task2_advantages_disadvantages",
        "difficulty": "medium",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Remote Telecommuting: Productivity Freedom vs Professional Isolation",
        "topic": "Organizational Psychology & Future of Work",
        "writingTask": {
            "taskType": "task2_advantages_disadvantages",
            "essayCategory": "advantages_outweigh",
            "prompt": "Following advancements in communication technology, an increasing number of companies are allowing employees to work remotely from home full-time rather than commuting to an office.\n\nDo the advantages of full-time telecommuting outweigh the disadvantages?",
            "bulletPoints": [
                "Advantages: Elimination of soul-destroying commutes, enhanced work-life flexibility, cost savings on commercial office leases, broader talent pools.",
                "Disadvantages: Blurring of work-life boundaries leading to burnout, erosion of spontaneous creative collaboration, professional loneliness.",
                "Thesis: Advantages outweigh drawbacks, especially when structured as flexible hybrid or clear digital boundaries."
            ],
            "minWords": 250,
            "sampleExaminerBand": "Band 8.5",
            "sampleEssay": (
                "The rapid proliferation of high-speed cloud computing, collaborative software, and video conferencing has cemented full-time remote "
                "work as a viable operational model for millions of corporate enterprises. While telecommuting introduces genuine risks concerning professional "
                "isolation and the erosion of collaborative synergy, I believe that the profound benefits in personal well-being, reduced commuting overhead, "
                "and corporate productivity decisively outweigh the drawbacks.\n\n"
                "Admittedly, permanent remote work is not without considerable psychological and organizational challenges. Chief among these is the insidious "
                "blurring of boundaries between professional obligations and domestic life. When the living room becomes the office, employees often find it "
                "impossible to mentally disconnect, resulting in chronic burnout and prolonged screen fatigue. Furthermore, digital communication channels "
                "cannot fully replicate the serendipitous creativity that occurs during spontaneous face-to-face interactions by office water coolers. "
                "Junior staff members, in particular, may suffer from a lack of informal mentorship, while prolonged physical separation from colleagues can "
                "engender profound feelings of alienation and weaken corporate cultural cohesion.\n\n"
                "Nevertheless, the tangible advantages of remote employment are transformative. Most significant is the elimination of the daily commute, "
                "which historically consumed billions of hours annually in stressful traffic congestion, while generating massive vehicular emissions. Liberated "
                "from lengthy commutes, workers reclaim valuable time for physical exercise, healthy home cooking, and family care, dramatically improving work-life "
                "harmony. From an employer's perspective, telecommuting dramatically lowers commercial real estate overhead and utility expenses, while "
                "democratizing recruitment by allowing companies to source elite global talent unrestricted by geographic boundaries. Empirical studies consistently "
                "reveal that remote workers, free from open-plan office distractions, achieve superior focus and quantitative output on deep analytical tasks.\n\n"
                "In conclusion, while organizations must actively manage the risks of worker isolation and digital burnout, the liberation from daily commuting "
                "and the gains in personal autonomy make full-time remote work an overwhelmingly advantageous evolution of contemporary labor."
            ),
            "bandRubricHighlights": {
                "taskAchievement": "Comprehensive analysis of modern organizational dynamics; clear, well-supported conclusion.",
                "coherenceCohesion": "Cohesive paragraph structure with sophisticated discourse markers and balanced evaluation.",
                "lexicalResource": "Advanced business and psychological vocabulary: 'telecommuting', 'serendipitous creativity', 'democratizing recruitment', 'insidious blurring'.",
                "grammaticalRange": "Flawless sentence structures showing wide syntactic variety and natural fluency."
            }
        }
    }
]
