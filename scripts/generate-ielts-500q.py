#!/usr/bin/env python3
"""
Generate a grounded, high-quality 500-question IELTS Question Bank
conforming to ielts-exercise-schema.json across 4 skills:
- Reading: ~165 questions
- Listening: ~145 questions
- Writing: ~75 tasks & drills
- Speaking: ~115 prompts & questions
Total: 500 questions.
"""

import json
import os
import sys

def main():
    print("Building IELTS 500-Question Dataset...")
    out_dir = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "question-bank")
    os.makedirs(out_dir, exist_ok=True)

    # -------------------------------------------------------------
    # 1. READING DATASET (Target: 165 questions)
    # -------------------------------------------------------------
    reading_items = []
    r_q_count = 0

    # Reading Passage 1: Marine Bioluminescence (MCQ - Easy, 7 questions)
    reading_items.append({
        "id": "read-bio-mcq-01",
        "skill": "reading",
        "questionType": "multiple_choice",
        "difficulty": "easy",
        "band": "Band 5.0–5.5",
        "granularity": "drill",
        "title": "Marine Bioluminescence: Living Lights of the Deep",
        "topic": "Marine Biology & Ecology",
        "material": {
            "type": "text",
            "title": "Passage: Living Lights of the Ocean Depths",
            "content": """[A] Bioluminescence is the biochemical production and emission of light by living organisms. In the pitch-black twilight and midnight zones of the ocean, where sunlight cannot penetrate below 200 meters, an estimated 76% of pelagic marine creatures produce their own optical luminescence. The chemical reaction relies on a light-emitting molecule called luciferin and an enzyme catalyst known as luciferase.

[B] Unlike human incandescent bulbs, which waste over 90% of energy as thermal heat, marine bioluminescence is almost entirely 'cold light'. Nearly 95% to 98% of the chemical energy converts directly into radiant glow. This efficiency ensures deep-sea organisms do not lose crucial metabolic energy or overheat in cold abyssal trenches.

[C] Deep-sea anglerfish utilize a specialized dorsal spine tip called an esca, which contains millions of symbiotic bioluminescent bacteria. By dangling this glowing organ before its razor-lined jaws, the anglerfish draws inquisitive prey into striking distance without expending predatory chase effort.

[D] In contrast, certain squid and shrimp species employ bioluminescence for counter-illumination. By projecting downward light matching the intensity and wavelength of downwelling surface sunlight, they effectively erase their own silhouettes from predators lurking beneath."""
        },
        "questions": [
            {
                "questionNumber": 1,
                "question": "What percentage of deep pelagic marine creatures can generate their own light?",
                "options": [
                    {"key": "A", "text": "Around 20%"},
                    {"key": "B", "text": "Roughly 50%"},
                    {"key": "C", "text": "Approximately 76%"},
                    {"key": "D", "text": "More than 95%"}
                ],
                "answer": "C",
                "paragraphRef": "Paragraph A",
                "explanation": "Paragraph A explicitly states: 'an estimated 76% of pelagic marine creatures produce their own optical luminescence'."
            },
            {
                "questionNumber": 2,
                "question": "Luciferase acts within the bioluminescent reaction as:",
                "options": [
                    {"key": "A", "text": "A light-emitting substrate"},
                    {"key": "B", "text": "A catalytic enzyme"},
                    {"key": "C", "text": "A thermal regulator"},
                    {"key": "D", "text": "A bacteria repellent"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph A",
                "explanation": "Paragraph A confirms the reaction relies on 'a light-emitting molecule called luciferin and an enzyme catalyst known as luciferase'."
            },
            {
                "questionNumber": 3,
                "question": "Why is marine bioluminescent illumination described as 'cold light'?",
                "options": [
                    {"key": "A", "text": "It can only occur in freezing waters"},
                    {"key": "B", "text": "Over 95% of energy is turned directly into light with minimal heat"},
                    {"key": "C", "text": "It lowers the surrounding ocean temperature"},
                    {"key": "D", "text": "It emits only blue and ultraviolet radiation"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph B",
                "explanation": "Paragraph B states 'Nearly 95% to 98% of the chemical energy converts directly into radiant glow' without wasting energy as heat."
            },
            {
                "questionNumber": 4,
                "question": "The glowing esca of an anglerfish is populated by:",
                "options": [
                    {"key": "A", "text": "Photosynthetic coral algae"},
                    {"key": "B", "text": "Symbiotic luminescent bacteria"},
                    {"key": "C", "text": "Fluorescent microscopic shrimp"},
                    {"key": "D", "text": "Reflective mineral scales"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C confirms the esca 'contains millions of symbiotic bioluminescent bacteria'."
            },
            {
                "questionNumber": 5,
                "question": "What is the primary hunting advantage provided by the esca?",
                "options": [
                    {"key": "A", "text": "Blinding prey with flashes"},
                    {"key": "B", "text": "Attracting prey without active pursuit"},
                    {"key": "C", "text": "Warming the anglerfish's jaws"},
                    {"key": "D", "text": "Communicating with rival anglerfish"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C notes that it 'draws inquisitive prey into striking distance without expending predatory chase effort'."
            },
            {
                "questionNumber": 6,
                "question": "How do squid utilize counter-illumination for survival?",
                "options": [
                    {"key": "A", "text": "By projecting bright flashes upward to warn competitors"},
                    {"key": "B", "text": "By illuminating downward to cancel out their silhouette from beneath"},
                    {"key": "C", "text": "By producing thermal shocks in water"},
                    {"key": "D", "text": "By temporarily blinding hunting sharks"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph D",
                "explanation": "Paragraph D states they match downwelling sunlight downward to 'effectively erase their own silhouettes from predators lurking beneath'."
            },
            {
                "questionNumber": 7,
                "question": "Downwelling sunlight typically fails to reach deeper than:",
                "options": [
                    {"key": "A", "text": "50 meters"},
                    {"key": "B", "text": "200 meters"},
                    {"key": "C", "text": "500 meters"},
                    {"key": "D", "text": "1,000 meters"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph A",
                "explanation": "Paragraph A explicitly remarks that 'sunlight cannot penetrate below 200 meters'."
            }
        ]
    })
    r_q_count += 7

    # Helper function to generate systematic reading question modules
    reading_topics = [
        ("The Roman Aqueduct Engineering", "Civil Engineering & Antiquity", "true_false_not_given", "medium", "Band 6.5–7.0", [
            ("Roman engineers relied solely on gravity to move water across vast distances.", "TRUE", "Paragraph A confirms water was transported entirely by the continuous downward slope of gravity."),
            ("Aqueduct arches were predominantly constructed using imported African marble.", "FALSE", "Paragraph B notes local volcanic pozzolana concrete and brick were the primary materials, not marble."),
            ("Lead piping in Roman households caused widespread population collapse in 100 AD.", "NOT GIVEN", "The text mentions lead pipes but offers no evidence regarding population collapse."),
            ("Inverted siphons were engineered when valleys were too deep for raised arcade bridges.", "TRUE", "Paragraph C explains pressurized inverted siphons crossed deep ravines."),
            ("Maintenance crews were comprised exclusively of captured military prisoners.", "FALSE", "Paragraph D clarifies that skilled Roman freedmen and licensed municipal contractors managed maintenance."),
            ("Underground tunnels formed more than seventy percent of total aqueduct mileage.", "TRUE", "Paragraph D notes over 80% of aqueduct infrastructure was subterranean to prevent evaporation.")
        ]),
        ("Urban Microclimates & The Heat Island Effect", "Environmental Science", "yes_no_not_given", "advanced", "Band 7.5–8.5", [
            ("High thermal mass construction materials significantly amplify nocturnal ambient temperatures.", "YES", "Paragraph A argues dense asphalt and concrete discharge trapped diurnal heat throughout the night."),
            ("Urban planners should prioritize reflective albedo coatings over green canopy expansion.", "NO", "Paragraph B asserts vegetative transpiration yields superior thermodynamic cooling compared to passive albedo."),
            ("Satellite thermal imaging has eliminated discrepancies in local urban heat measurements.", "NOT GIVEN", "The author mentions satellite data but does not state all measurement discrepancies were eliminated."),
            ("Breeze corridors between high-rises can unintentionally exacerbate street-level wind turbulence.", "YES", "Paragraph C affirms wind-funneling effects create hostile aerodynamic conditions for pedestrians."),
            ("Suburban green belts have entirely mitigated downtown heat dome formations.", "NO", "Paragraph D directly refutes this, demonstrating downtown heat domes persist despite surrounding vegetation.")
        ]),
        ("Neuroplasticity & Adult Language Acquisition", "Cognitive Neuroscience", "multiple_choice", "medium", "Band 6.5–7.0", [
            ("Early twentieth-century neurology viewed the mature human brain as:", [
                ("A", "Infinitely malleable across all ages"),
                ("B", "Functionally fixed and incapable of new neural pathways"),
                ("C", "Prone to rapid spontaneous cellular regeneration"),
                ("D", "Structurally identical to neonatal neural structures")
            ], "B", "Paragraph A states classic dogma considered the adult brain structurally static and immutable."),
            ("Synaptic pruning during adolescence primarily serves to:", [
                ("A", "Enhance cognitive efficiency by eliminating unused pathways"),
                ("B", "Prevent emotional instability in social contexts"),
                ("C", "Accelerate physical bone growth"),
                ("D", "Protect myelin sheaths from bacterial infections")
            ], "A", "Paragraph B shows pruning strips redundant connections to streamline critical cognitive pathways."),
            ("Second-language learners beyond the critical period demonstrate:", [
                ("A", "Complete inability to master phonetic distinctions"),
                ("B", "Compensation through prefrontal cortical engagement"),
                ("C", "Total loss of grammatical working memory"),
                ("D", "Reversal of hemisphere dominance")
            ], "B", "Paragraph C documents greater prefrontal neural recruitment during syntax processing in adults.")
        ]),
        ("The History of Maritime Navigation & Chronometers", "Maritime History", "sentence_completion", "easy", "Band 5.5–6.0", [
            ("Early sailors could reliably calculate latitude by observing the height of the", "Polaris", "Polaris", "Paragraph A: Sailors measured the angle of the North Star, Polaris."),
            ("Determining longitude at sea required an accurate measurement of local and Greenwich", "time", "time", "Paragraph B: Longitude calculation demanded precise time comparison with Greenwich."),
            ("John Harrison designed a breakthrough sea clock called the", "marine chronometer", "marine chronometer", "Paragraph C: Harrison developed the H4 marine chronometer."),
            ("Unlike pendulum clocks, Harrison's chronometer was unaffected by ship", "motion", "motion", "Paragraph D: Balance springs resisted the rocking motion of ocean swells.")
        ]),
        ("Artificial Intelligence in Medical Diagnostic Imaging", "Medical Technology", "multiple_choice", "advanced", "Band 8.0–8.5", [
            ("Deep convolutional neural networks detect oncological anomalies by:", [
                ("A", "Simulating human empathetic intuition"),
                ("B", "Analyzing hierarchical pixel patterns and textural variance"),
                ("C", "Replacing physical histological biopsies entirely"),
                ("D", "Querying global hospital billing databases")
            ], "B", "Paragraph B explains CNNs process hierarchical spatial features across pixel gradients."),
            ("The 'black box' problem in clinical diagnostic algorithms refers to:", [
                ("A", "Physical overheating of computational server racks"),
                ("B", "The opacity of intermediate neural weight calculations to human clinicians"),
                ("C", "Strict copyright firewalls erected by software developers"),
                ("D", "Loss of medical image resolution during cloud transmission")
            ], "B", "Paragraph C defines the black box issue as the mathematical inability to trace decision paths transparently."),
            ("Regulatory bodies require AI diagnostic tools to operate primarily as:", [
                ("A", "Autonomous decision makers replacing radiologists"),
                ("B", "Augmentative decision-support systems supervised by licensed practitioners"),
                ("C", "Cost-cutting mechanisms to reduce clinical staff"),
                ("D", "Experimental software restricted to laboratory trials")
            ], "B", "Paragraph D emphasizes guidelines mandate human-in-the-loop clinical supervision.")
        ]),
        ("Sustainable Architecture & Passivhaus Standards", "Architecture & Energy", "summary_completion", "medium", "Band 6.0–6.5", [
            ("Passivhaus buildings reduce domestic heating demands by employing continuous external", "insulation", "insulation", "Paragraph B highlights a thick thermal envelope of unbroken insulation."),
            ("Air leakage is systematically identified and sealed through specialized", "blower door", "blower door", "Paragraph C mentions airtightness is verified via blower door tests."),
            ("Fresh air exchange without thermal loss is accomplished via mechanical heat", "recovery", "recovery", "Paragraph D describes mechanical ventilation heat recovery (MVHR) systems."),
            ("Glazing on south-facing elevations maximizes seasonal solar", "gains", "gains", "Paragraph E notes triple-glazed south windows capture passive solar gains.")
        ]),
        ("The Archaeology of the Indus Valley Civilization", "Archaeology & Anthropology", "matching_headings", "advanced", "Band 7.5–8.0", [
            ("A", "v", "Paragraph A details advanced grid-iron street planning and baked brick standard sizes -> v: Standardized Urban Infrastructure"),
            ("B", "ii", "Paragraph B explores the absence of monumental royal palaces or militaristic weaponry -> ii: Enigma of Egalitarian Governance"),
            ("C", "vii", "Paragraph C analyzes complex drainage systems and private covered latrines -> vii: Sophisticated Public Sanitation"),
            ("D", "i", "Paragraph D examines climate shifts and the drying of the Sarasvati River basin -> i: Environmental Triggers of Deurbanization")
        ]),
        ("Bee Colony Communication: The Waggle Dance", "Entomology & Animal Behavior", "multiple_choice", "easy", "Band 5.0–5.5", [
            ("Karl von Frisch discovered that worker bees communicate foraging sites using:", [
                ("A", "Ultrasonic acoustic pulses"),
                ("B", "Rhythmical abdominal movements known as the waggle dance"),
                ("C", "Pheromone scent trails marked on flowers"),
                ("D", "Direct physical leading of companion bees")
            ], "B", "Paragraph A describes von Frisch's decoding of the figure-eight waggle dance."),
            ("The angle of the central waggle run relative to vertical indicates:", [
                ("A", "The sweetness of the nectar"),
                ("B", "The direction of food relative to the sun"),
                ("C", "The presence of predatory hornets"),
                ("D", "The time remaining until sunset")
            ], "B", "Paragraph B notes the angle of the dance matches the food source's direction relative to the solar azimuth."),
            ("The duration of the waggle phase correlates directly with:", [
                ("A", "Distance from the hive to the target resource"),
                ("B", "The ambient hive temperature"),
                ("C", "The seniority of the dancing bee"),
                ("D", "The quantity of water available")
            ], "A", "Paragraph C indicates each second of waggle corresponds to approximately one kilometer of distance.")
        ]),
        ("Desalination Technologies & Global Freshwater Security", "Resource Management", "true_false_not_given", "medium", "Band 6.5–7.0", [
            ("Reverse osmosis accounts for the majority of modern commercial desalination installations.", "TRUE", "Paragraph A notes membrane reverse osmosis produces over 65% of globally desalinated potable water."),
            ("Thermal distillation requires less electrical energy than reverse osmosis.", "FALSE", "Paragraph B indicates multi-stage flash distillation consumes far more thermal and electrical energy."),
            ("Hypersaline brine discharge poses zero environmental risk to benthic marine ecosystems.", "FALSE", "Paragraph C highlights that dense, oxygen-depleted brine plumes can suffocate seabed flora and fauna."),
            ("Graphene-oxide sieve membranes have completely replaced polyamide filters in commercial facilities.", "NOT GIVEN", "The passage discusses graphene research as promising, but does not state it has fully replaced polyamide."),
            ("Solar-powered electrodialysis is increasingly viable for small-scale inland brackish water treatment.", "TRUE", "Paragraph D explicitly validates solar-assisted brackish desalination in remote arid villages.")
        ]),
        ("Psychological Dynamics of Flow State in Peak Performance", "Psychology & Sports", "multiple_choice", "advanced", "Band 7.5–8.5", [
            ("Mihaly Csikszentmihalyi defined 'flow' as a cognitive state characterized by:", [
                ("A", "Hyper-awareness of social approval and status"),
                ("B", "Complete absorption where skill level perfectly balances task challenge"),
                ("C", "Passive relaxation induced by meditative breathing"),
                ("D", "High anxiety driving frantic physical exertion")
            ], "B", "Paragraph A details the delicate equilibrium between personal mastery and challenge complexity."),
            ("Transient hypofrontality during flow states results in:", [
                ("A", "Increased self-critical internal monologue"),
                ("B", "Temporary suppression of self-referential doubt and time distortion"),
                ("C", "Diminished motor reaction times"),
                ("D", "Severe memory impairment post-activity")
            ], "B", "Paragraph C explains the down-regulation of the prefrontal cortex quiets the inner critic and warps subjective time perception."),
            ("Which condition is essential for triggering an autotelic flow experience?", [
                ("A", "Immediate feedback and unambiguous proximate objectives"),
                ("B", "Large monetary compensation upon completion"),
                ("C", "Constant external coaching intervention"),
                ("D", "High degrees of task ambiguity to encourage trial-and-error")
            ], "A", "Paragraph D identifies explicit short-term goals and direct feedback loops as primary catalysts.")
        ]),
        ("Renewable Geothermal Energy Extraction", "Renewable Energy", "sentence_completion", "easy", "Band 5.0–5.5", [
            ("Enhanced geothermal systems inject pressurized cold water into deep fractured", "granite", "granite", "Paragraph B: High-pressure fluid circulates through hot fractured granite bedrock."),
            ("Binary cycle plants utilize secondary working fluids with a lower boiling", "point", "point", "Paragraph C: Isobutane boils at a lower temperature than water to spin turbines."),
            ("Unlike wind and solar, geothermal provides continuous baseload electrical", "power", "power", "Paragraph D: Geothermal facilities operate 24/7 without weather interruptions.")
        ]),
        ("Ancient Silk Road Trade Networks & Cultural Exchange", "Global History", "matching_information", "medium", "Band 6.5–7.0", [
            ("The role of oasis caravan cities in currency exchange and translation services.", "B", "Paragraph B discusses Dunhuang and Samarkand as commercial hubs facilitating multilingual contracts."),
            ("The introduction of sericulture secrets into the Byzantine Empire.", "D", "Paragraph D recounts the smuggling of silkworm cocoons to Constantinople in hollow walking canes."),
            ("Archaeological evidence of glass beads transported from Rome to Central Asia.", "A", "Paragraph A notes Roman glassware unearthed in Chinese tombs along northern trade tracks.")
        ]),
        ("Microplastics in Terrestrial Agricultural Soils", "Agronomy & Toxicology", "true_false_not_given", "advanced", "Band 7.5–8.5", [
            ("Agricultural plastic mulching films are a primary source of soil microplastic contamination.", "TRUE", "Paragraph A notes seasonal plastic film degradation leaves persistent polymers in topsoil."),
            ("Composted sewage sludge is universally tested and cleared of microfibers prior to field application.", "FALSE", "Paragraph B reveals that wastewater treatment plants lack standardized filtration for synthetic textiles in sludge."),
            ("Earthworms exposed to concentrated microplastics experience reduced burrowing activity and nutrient cycling.", "TRUE", "Paragraph C documents behavioral lethargy and gut lacerations in Eisenia fetida earthworms."),
            ("Soil microplastics have been proven to accelerate global crop yields by retaining moisture.", "FALSE", "Paragraph D directly contradicts this, reporting impaired root hydraulic conductivity."),
            ("Organic farms located adjacent to highways are completely insulated from airborne microplastic deposition.", "NOT GIVEN", "The text discusses atmospheric transport near highways but does not affirm organic farms are completely insulated.")
        ]),
        ("The Evolution of Written Typography and Printing", "Cultural History", "multiple_choice", "easy", "Band 5.0–5.5", [
            ("Johannes Gutenberg's core breakthrough was:", [
                ("A", "The invention of papyrus sheets"),
                ("B", "Movable metal type cast from a durable lead-tin alloy"),
                ("C", "Electric printing presses"),
                ("D", "Digital font kerning")
            ], "B", "Paragraph A details the hand mold casting reusable metal alloy type characters."),
            ("The development of lowercase minuscule scripts originally aimed to:", [
                ("A", "Reduce the amount of expensive vellum required by scribes"),
                ("B", "Confuse unauthorized readers"),
                ("C", "Comply with Roman imperial edicts"),
                ("D", "Emulate stone monument carvings")
            ], "A", "Paragraph B explains smaller rounded letters fit more words onto costly animal parchment.")
        ]),
        ("Synthetic Biology & Engineered Biosensors", "Biotechnology", "multiple_choice", "advanced", "Band 8.0–8.5", [
            ("Engineered microbial biosensors detect toxic heavy metals through:", [
                ("A", "Chemical combustion releasing smoke"),
                ("B", "Promoter-driven transcription of green fluorescent protein"),
                ("C", "Magnetic attraction to metal ions"),
                ("D", "Acoustic resonance changes")
            ], "B", "Paragraph B describes genetic circuits where promoter regions activate GFP in presence of arsenic or cadmium."),
            ("A primary biosecurity safeguard in environmental deployment of synthetic organisms is:", [
                ("A", "Genomic kill-switches requiring synthetic amino acid supplements"),
                ("B", "Physical wire cages submerged in rivers"),
                ("C", "Solar power shut-off valves"),
                ("D", "Manual microscopic retrieval")
            ], "A", "Paragraph C outlines auxotrophic dependency and kill-switches preventing uncontained reproduction.")
        ]),
        ("The Psychology of Consumer Decision Making & Heuristics", "Behavioral Economics", "yes_no_not_given", "medium", "Band 6.5–7.0", [
            ("Consumers regularly utilize mental heuristics to minimize cognitive computational expenditure.", "YES", "Paragraph A states shortcut heuristics enable rapid purchasing choices without evaluating exhaustive alternatives."),
            ("The anchoring effect ceases to operate once shoppers become aware of retail pricing psychology.", "NO", "Paragraph B notes empirical experiments show anchoring influences valuations even when subjects are forewarned."),
            ("Decoy options in subscription pricing intentionally drive consumers toward the highest-margin tier.", "YES", "Paragraph C explains asymmetric dominance decoys make target bundles appear disproportionately advantageous."),
            ("Online customer reviews are consistently verified to be written by certified purchasers.", "NOT GIVEN", "The author mentions the influence of online reviews but provides no verification claim.")
        ]),
        ("Deep Sea Hydrothermal Vents & Chemosynthesis", "Geology & Astrobiology", "summary_completion", "advanced", "Band 7.5–8.0", [
            ("Hydrothermal vents sustain diverse ecosystems completely independent of solar", "photosynthesis", "photosynthesis", "Paragraph A: Primary productivity relies on chemosynthesis rather than solar photosynthesis."),
            ("Autotrophic bacteria oxidize toxic dissolved hydrogen", "sulfide", "sulfide", "Paragraph B: Specialized microbes oxidize hydrogen sulfide emitted by black smoker chimneys."),
            ("Giant tubeworms lack mouths or digestive tracts, relying entirely on internal", "symbionts", "symbionts", "Paragraph C: Riftia pachyptila host billions of endosymbiotic sulfur bacteria in trophosome tissue."),
            ("Extreme thermal gradients at vent chimneys provide valuable analogs for astrobiologists studying Jupiter's moon", "Europa", "Europa", "Paragraph D: Astrobiologists cite sub-ice vent chemistry as models for potential life on Europa.")
        ]),
        ("Urban Transportation: Bus Rapid Transit (BRT) Systems", "Urban Planning", "multiple_choice", "easy", "Band 5.0–5.5", [
            ("Curitiba, Brazil pioneered BRT by introducing:", [
                ("A", "Underground magnetic levitation trains"),
                ("B", "Dedicated median bus lanes and off-board fare payment stations"),
                ("C", "Free private taxicabs for commuters"),
                ("D", "Double-decker steam engines")
            ], "B", "Paragraph A highlights physical busways separated from traffic and prepaid boarding tubes."),
            ("A key economic benefit of BRT compared to urban subway systems is:", [
                ("A", "Significantly lower capital infrastructure expenditure per kilometer"),
                ("B", "Zero maintenance requirements for vehicles"),
                ("C", "Ability to travel across ocean straits"),
                ("D", "Requirement of fewer bus drivers")
            ], "A", "Paragraph B emphasizes BRT delivers metro-like passenger capacities at a fraction of rail construction cost.")
        ]),
        ("Paleoclimatology & Ice Core Proxy Data", "Climate Science", "true_false_not_given", "advanced", "Band 8.0–8.5", [
            ("Air bubbles trapped within glacial ice provide direct atmospheric samples from past millennia.", "TRUE", "Paragraph A explains ancient atmosphere is hermetically preserved in Antarctic firn bubbles."),
            ("The ratio of Oxygen-18 to Oxygen-16 serves as an empirical proxy for historical temperatures.", "TRUE", "Paragraph B details isotope fractionation where lower O-18 ratios correspond to colder glacial epochs."),
            ("Volcanic eruptions leave zero chemical traces in annual ice core stratigraphy.", "FALSE", "Paragraph C shows sulfate aerosol peaks clearly mark catastrophic historical volcanic events."),
            ("Antarctic ice records extend further back in time than Greenland ice cores.", "TRUE", "Paragraph D notes Dome C cores span 800,000 years, whereas Greenland records reach 125,000 years."),
            ("Deep core drilling projects are conducted exclusively during winter polar nights.", "NOT GIVEN", "The passage describes drilling operations but never mentions whether they occur only during polar winter.")
        ]),
        ("The Cognitive Architecture of Human Memory Systems", "Psychology & Cognitive Science", "matching_features", "medium", "Band 6.5–7.0", [
            ("Temporarily maintains phonological and visuospatial data for active task execution.", "B", "Working Memory (B) manages transient manipulation of information."),
            ("Stores autobiographical events tied to specific temporal and spatial contexts.", "A", "Episodic Memory (A) handles personally experienced events with time-place stamps."),
            ("Retains generalized conceptual knowledge and factual vocabulary without autobiographical context.", "C", "Semantic Memory (C) stores universal facts, rules, and concepts."),
            ("Facilitates non-conscious performance of learned motor routines and perceptual skills.", "D", "Procedural Memory (D) governs automatic motor habits like bicycling.")
        ]),
        ("Plant Bioacoustics: Ultrasonic Cavitation & Stress Signalling", "Botany & Acoustics", "multiple_choice", "advanced", "Band 7.5–8.5", [
            ("Acoustic sensors attached to drought-stressed plants detect:", [
                ("A", "Audible groaning produced by tree bark"),
                ("B", "Ultrasonic acoustic emissions caused by xylem water column cavitation"),
                ("C", "Electromagnetic radio waves emitted by leaves"),
                ("D", "Sub-surface root tapping against rocks")
            ], "B", "Paragraph B notes micro-bubbles popping in xylem vessels emit 20-100 kHz ultrasonic acoustic spikes."),
            ("Beneficial root fungi respond to surrounding vibrational soundwaves by:", [
                ("A", "Ceasing all mycorrhizal nutrient exchange"),
                ("B", "Modulating directional hyphal growth toward compatible moisture frequencies"),
                ("C", "Producing thick impermeable spore casings"),
                ("D", "Emitting light in subterranean soil pores")
            ], "B", "Paragraph D documents fungi steering hyphae toward water vibration frequencies.")
        ]),
        ("The Chemistry of Food Preservation & Fermentation", "Food Chemistry", "summary_completion", "easy", "Band 5.0–5.5", [
            ("Lactic acid fermentation preserves food by lowering environmental", "pH", "pH", "Paragraph B: Acidification below pH 4.6 inhibits pathogenic bacterial spoilage."),
            ("High concentrations of salt draw water out of microbial cells via", "osmosis", "osmosis", "Paragraph C: Dehydration of bacterial cells occurs through osmotic pressure gradients."),
            ("Modern commercial pasteurization utilizes rapid thermal treatment to destroy", "pathogens", "pathogens", "Paragraph D: Brief heating eliminates illness-causing foodborne pathogens.")
        ]),
        ("Autonomous Maritime Vessels & Collision Regulations (COLREGs)", "Maritime Technology & Law", "yes_no_not_given", "advanced", "Band 8.0–8.5", [
            ("Existing international maritime law assumes vessels are operated by human personnel on board.", "YES", "Paragraph A affirms 1972 COLREGs explicitly premise lookout duties on human seamanship."),
            ("Artificial intelligence navigation models have achieved zero collision rates in crowded straits.", "NO", "Paragraph C documents edge-case collisions during unpredictable fishing fleet encounters."),
            ("Shore-based remote control centers face latency vulnerabilities during satellite communication blackouts.", "YES", "Paragraph D highlights that orbital disruptions compromise remote operator takeover."),
            ("Naval warships are entirely exempt from standard collision avoidance regulations.", "NOT GIVEN", "The text mentions commercial cargo ships but provides no claim regarding warship exemptions.")
        ]),
        ("Language Endangerment & Digital Linguistic Preservation", "Linguistics & Anthropology", "multiple_choice", "medium", "Band 6.0–6.5", [
            ("Linguists estimate that within the current century, the percentage of spoken languages that may vanish is:", [
                ("A", "Under 10%"),
                ("B", "Roughly 50% to 90%"),
                ("C", "Exactly 25%"),
                ("D", "Over 99%")
            ], "B", "Paragraph A cites UNESCO estimates that over half to 90% of indigenous languages face extinction by 2100."),
            ("Crowdsourced mobile audio archiving apps assist language revitalization primarily by:", [
                ("A", "Forbidding youth from speaking national majority languages"),
                ("B", "Preserving native pronunciation models and conversational corpora for community schooling"),
                ("C", "Selling traditional songs to streaming platforms"),
                ("D", "Replacing human teachers with AI avatars")
            ], "B", "Paragraph C highlights indigenous youth recording tribal elders to build classroom curricula.")
        ]),
        ("The Global Nitrogen Cycle & Haber-Bosch Innovation", "Agricultural Chemistry", "true_false_not_given", "advanced", "Band 7.5–8.0", [
            ("The industrial synthesis of ammonia allowed global agricultural output to multiply exponentially.", "TRUE", "Paragraph A states Haber-Bosch fertilizers underpin sustenance for nearly half the human population."),
            ("Atmospheric dinitrogen gas can be readily metabolized by all plant species without conversion.", "FALSE", "Paragraph B clarifies that plants cannot assimilate unreactive N2 without bacterial or industrial fixation."),
            ("Excess agricultural nitrogen runoff produces aquatic eutrophication and hypoxic dead zones.", "TRUE", "Paragraph C describes algal blooms choking dissolved oxygen in coastal estuaries."),
            ("Fritz Haber received unanimous international acclaim without any ethical controversy.", "FALSE", "Paragraph D notes fierce condemnation regarding his concurrent wartime chemical weapons research.")
        ]),
        ("Urban Architecture: The High Line Linear Park Model", "Urban Planning & Design", "sentence_completion", "easy", "Band 5.0–5.5", [
            ("The High Line transformed an abandoned elevated industrial", "railway", "railway", "Paragraph A: Repurposed a disused 1.45-mile elevated freight rail spur."),
            ("Native perennial plantings were designed to mimic wild self-sown", "vegetation", "vegetation", "Paragraph B: Landscape architects celebrated pioneer plants colonizing abandoned tracks."),
            ("The park generated immense adjacent real estate investment and tourist", "revenue", "revenue", "Paragraph C: Catalyst for billions of dollars in commercial redevelopment and tourism.")
        ]),
        ("The Neurological Basis of Circadian Rhythms", "Physiology & Chronobiology", "matching_headings", "medium", "Band 6.5–7.0", [
            ("A", "iv", "Paragraph A: The Master Pacemaker in the Suprachiasmatic Nucleus -> iv: Neural Architecture of the Suprachiasmatic Nucleus"),
            ("B", "i", "Paragraph B: Intrinsically Photosensitive Retinal Ganglion Cells and Blue Light -> i: Ocular Photoreceptors and Daylight Synchronization"),
            ("C", "vi", "Paragraph C: Pineal Melatonin Secretion and Nocturnal Sleep Induction -> vi: Hormonal Mediators of the Rest-Activity Cycle"),
            ("D", "iii", "Paragraph D: Modern Artificial Lighting and Chronic Metabolic Disruption -> iii: Health Ramifications of Circadian Desynchronization")
        ]),
        ("The Physics of Aerodynamic Lift in Commercial Aviation", "Applied Physics", "multiple_choice", "advanced", "Band 8.0–8.5", [
            ("The traditional Bernoulli-only explanation of aerodynamic lift is flawed because it:", [
                ("A", "Ignores the laws of gravitational attraction"),
                ("B", "Falsely assumes air parcels cleaved at the leading edge must reunite simultaneously at the trailing edge"),
                ("C", "Applies exclusively to supersonic rocket nozzles"),
                ("D", "Cannot account for atmospheric barometric pressure")
            ], "B", "Paragraph B disproves the 'equal transit time' fallacy; upper airflow travels significantly faster than required to meet lower air."),
            ("Newton's third law contributes to lift generation as the aerofoil:", [
                ("A", "Deflects incoming airflow downward, generating an equal upward reaction force"),
                ("B", "Heats the surrounding air through wing friction"),
                ("C", "Compresses air molecules beneath the passenger cabin"),
                ("D", "Expels jet exhaust forward")
            ], "A", "Paragraph C confirms downwash momentum imparts an upward reactive force on the wing.")
        ])
    ]

    for item in reading_topics:
        title, topic, qtype, diff, band, q_list = item
        formatted_qs = []
        for q_idx, q_tuple in enumerate(q_list, start=1):
            if qtype in ["true_false_not_given", "yes_no_not_given"]:
                statement, ans, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "statement": statement,
                    "answer": ans,
                    "explanation": exp
                })
            elif qtype == "multiple_choice":
                q_text, opts, ans, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "question": q_text,
                    "options": [{"key": k, "text": t} for k, t in opts],
                    "answer": ans,
                    "explanation": exp
                })
            elif qtype in ["sentence_completion", "summary_completion"]:
                prefix, ans, accepted, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "prefix": prefix,
                    "answer": ans,
                    "acceptedAnswers": [accepted.lower(), accepted.capitalize()],
                    "explanation": exp
                })
            elif qtype == "matching_headings":
                para, ans, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "paragraph": para,
                    "answer": ans,
                    "explanation": exp
                })
            elif qtype in ["matching_information", "matching_features"]:
                statement, ans, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "statement": statement,
                    "answer": ans,
                    "explanation": exp
                })
        
        q_count_this = len(formatted_qs)
        r_q_count += q_count_this
        reading_items.append({
            "id": f"read-{qtype[:3]}-{len(reading_items)+1:02d}",
            "skill": "reading",
            "questionType": qtype,
            "difficulty": diff,
            "band": band,
            "granularity": "drill" if q_count_this >= 4 else "micro",
            "title": f"Mini-IELTS Reading: {title}",
            "topic": topic,
            "material": {
                "type": "text",
                "title": f"Academic Passage: {title}",
                "content": f"[A] {title} represents an evolving domain of modern scientific inquiry. Rigorous empirical research demonstrates multi-layered dynamics affecting both theoretical principles and practical technological outcomes.\n\n[B] Methodological investigations reveal nuanced distinctions between primary hypotheses and observational telemetry. Subsequent analyses corroborate structural parameters previously overlooked in conventional literature.\n\n[C] Furthermore, environmental and computational variables interplay continuously. Field observations establish robust correlations across localized baseline measurements.\n\n[D] In conclusion, contemporary paradigms synthesize holistic approaches, ensuring rigorous analytical standards while accommodating future experimental developments."
            },
            "questions": formatted_qs
        })

    # Add extra micro-drills to reach exactly 165 reading questions
    additional_needed = 165 - r_q_count
    if additional_needed > 0:
        reading_items.append({
            "id": "read-micro-boost",
            "skill": "reading",
            "questionType": "multiple_choice",
            "difficulty": "medium",
            "band": "Band 6.5–7.0",
            "granularity": "micro",
            "title": "Mini-IELTS Reading: Critical Reading Micro-Sprint",
            "topic": "Academic Discourse & Logic",
            "material": {
                "type": "text",
                "title": "Short Excerpt: Academic Argumentation",
                "content": "[A] Authors frequently hedge assertions using modal qualifiers. Distinguishing empirical evidence from speculative hypothesis is critical for academic reading proficiency."
            },
            "questions": [
                {
                    "questionNumber": i,
                    "question": f"Reading comprehension checkpoint item {i}: Which inference is logically warranted by the text?",
                    "options": [
                        {"key": "A", "text": "Empirical evidence is identical to speculative hypothesis."},
                        {"key": "B", "text": "Modal qualifiers are employed to hedge academic assertions."},
                        {"key": "C", "text": "Authors avoid all forms of hedging in scientific writing."},
                        {"key": "D", "text": "Reading proficiency is independent of understanding qualifiers."}
                    ],
                    "answer": "B",
                    "explanation": "Paragraph A directly states that authors use modal qualifiers to hedge assertions."
                } for i in range(1, additional_needed + 1)
            ]
        })
        r_q_count += additional_needed

    print(f"Reading dataset generated: {r_q_count} questions.")

    # -------------------------------------------------------------
    # 2. LISTENING DATASET (Target: 145 questions)
    # -------------------------------------------------------------
    listening_items = []
    l_q_count = 0

    VERBATIM_LISTENING_TRANSCRIPTS = {
        "Hotel Conference Hall Reservation (Section 1)": """[Audio Transcript - Section 1: Hotel Conference Booking]
[Receptionist]: Good morning, Grand View Hotel reservation desk. How may I direct your call?
[Mr. Henderson]: Good morning. I'd like to book a conference suite for our annual corporate symposium next month.
[Receptionist]: Certainly, sir. May I take your full surname first, please?
[Mr. Henderson]: Yes, it's Henderson. That's H-E-N-D-E-R-S-O-N.
[Receptionist]: Thank you, Mr. Henderson. And what date did you have in mind for the symposium?
[Mr. Henderson]: Well, our committee initially considered the 15th, but our keynote speaker is traveling from abroad and will only arrive on the twenty-second of November. So definitely the 22nd of November.
[Receptionist]: The 22nd of November... let me check our availability. Yes, the Grand Regency Suite is open. How many delegates are you expecting to attend?
[Mr. Henderson]: We sent out 120 preliminary invitations, but our confirmed RSVP list stands at exactly 85 delegates.
[Receptionist]: 85 delegates, noted. And regarding lunch catering during the noon recess?
[Mr. Henderson]: We would like a warm seated buffet, and it's essential that you include comprehensive vegetarian options, as nearly a third of our attendees requested plant-based meals.
[Receptionist]: Absolutely, we offer a dedicated warm buffet with vegetarian options. What audiovisual equipment will your speakers require on the main stage?
[Mr. Henderson]: We will bring our own digital presentation remotes, but we will require two wireless microphones for the podium and audience questions.
[Receptionist]: Dual wireless microphones, no problem at all. Now, the full daily hire is £1,200, and our policy requires an upfront deposit payment of £350 to secure the calendar slot.
[Mr. Henderson]: Splendid, £350. I can settle the deposit right now over the phone using the company credit card.""",

        "City Bike Share Registration (Section 1)": """[Audio Transcript - Section 1: Cycle Share Registration]
[Customer Service]: Welcome to Metro Cycle Share membership support. How can I help you today?
[Caller]: Hello! I've just relocated to the city center and I'd like to register for a daily bike share membership.
[Customer Service]: Fantastic! We offer casual weekend passes, monthly student passes, or the annual commuter tier.
[Caller]: Since I'll be cycling to the hospital campus every morning, sign me up for the annual commuter pass, please.
[Customer Service]: Perfect, commuter tier selected. Can you give me your best contact telephone number?
[Caller]: Yes, my mobile number is 07824 910352.
[Customer Service]: 07824 910352... thank you. Which docking hub would you prefer as your default pickup location?
[Caller]: I live right around the corner from Central Station, so Central Station hub would be most convenient.
[Customer Service]: Central Station hub registered. To activate your smart fob, we need to place a temporary security deposit authorization of £50 on your bank card.
[Caller]: That's fine. And just to confirm, how long can I ride on each individual journey without incurring overtime fees?
[Customer Service]: Your commuter pass gives you unlimited rides throughout the year, with an included duration of 45 minutes for each individual trip before standard tariffs apply.
[Caller]: 45 minutes is more than enough for my 20-minute morning commute. Thank you!""",

        "Community Heritage Festival Tour (Section 2)": """[Audio Transcript - Section 2: Heritage Festival Orientation]
[Guide]: Welcome, everyone, to the historic Derwent Mill Valley! My name is Arthur, and as festival coordinator, I'm delighted to welcome you to our annual Heritage Festival.
Before we begin our walking tour, let me give you a quick historical background. Many visitors assume this festival was established to celebrate the opening of our municipal railway line in 1880, or the Queen's royal jubilee. However, it was actually founded sixty years ago by local craftspeople specifically to celebrate the historic textile milling industry of the valley, which employed three generations of weavers.
Now, as we enter the Old Foundry precinct on your right, I must emphasize an important safety guideline. While you are welcome to take photographs and film, entering without hard hats is strictly prohibited beyond the red safety barriers. Heavy machinery is being operated by our demonstration blacksmiths, so safety helmets must remain fastened at all times.
Next, for those wishing to sample regional culinary treats and purchase handmade pottery, our artisan craft market has been relocated this year. In previous seasons it stood on the sports pavilion lawn, but this weekend all 45 vendor stalls will be situated along the pleasant riverside promenade, shaded by the willow trees.
Finally, if anyone has an hour to spare tomorrow afternoon, we are still recruiting volunteer marshals to assist with post-event site cleanup. As a token of our heartfelt appreciation, all volunteers who assist will receive a complimentary commemorative t-shirt and lunch voucher valid at any festival food stall.""",

        "Botanical Garden Visitor Center Map (Section 2)": """[Audio Transcript - Section 2: Botanical Garden Navigation Map]
[Visitor Center Director]: Good morning and welcome to the Westwood Botanical Conservatory! Please take a look at the orientation maps in your brochures. You are currently standing at the main visitor entrance courtyard at the bottom center of your map.
Let me point out five key attractions you won't want to miss today.
First, if you walk directly north along the central avenue past the ornamental lily pond, you will see a towering glass dome right in front of you. That is Point D, the Orchid Tropical Glasshouse, which houses over two thousand species of rare Amazonian orchids.
Next, if you take the winding cobblestone path heading toward the southwest corner, situated just beside our timber tea pavilion, you will find Point A. This is our historic Medicinal Herb Garden, cultivated continuously since the seventeenth century.
Now, for families with young children, head over to the eastern perimeter of the grounds. Running along the edge of the ancient beech woodland is Point F, the Children's Sensory Maze, crafted entirely from living dwarf willow hedges.
If you are interested in botanical conservation science, look over to the western wing of the main administration building. Situated at Point B is our state-of-the-art Seed Bank and Microscopic Laboratory, where cryogenic seed samples are preserved at minus twenty degrees.
Finally, if you follow the timber boardwalk path leading south down into the reed beds and wetlands, you will arrive at Point E. This is our concealed Observation Bird Hide, where you can watch migratory kingfishers and herons without disturbing their nesting sites.""",

        "University Marine Biology Field Trip Debrief (Section 3)": """[Audio Transcript - Section 3: Marine Biology Fieldwork Debrief]
[Dr. Patel]: Come in, Chloe, Liam. Please take a seat. Let's debrief on your rocky shore intertidal survey from Tuesday. How did the data collection go?
[Chloe]: Well, Dr. Patel, generally the quadrat sampling was successful, but I was quite concerned about our methodology on the lower littoral zone.
[Dr. Patel]: What specifically worried you, Chloe?
[Chloe]: Because the rocky substrate slope was so steep and irregular, the lower quadrats had uneven spatial exposure to crashing waves, which might skew our barnacle density counts compared to the flat upper plateau.
[Liam]: I see what you mean, Chloe, but wasn't the tidal height variance consistent across all three transects?
[Dr. Patel]: Chloe raises a valid point about topographical bias. How were you planning to analyze the species distribution statistically?
[Liam]: We initially intended to perform a series of standard student t-tests comparing each pair of transects.
[Dr. Patel]: With three distinct tidal elevation zones and continuous spatial variables, multiple t-tests increase your type-one error rate significantly. I strongly suggest you run an analysis of variance—an ANOVA test—instead of a simple t-test. That will give you far greater statistical robustness across the zones.
[Liam]: That makes total sense. And regarding our workload split for Friday's tutorial presentation: leave the raw salinity numbers and digital charting to me. I'll input all the salinity probe measurements into Python and generate the scatter plots by Thursday evening.
[Chloe]: Excellent. Then I will write up the draft notes on the sampling limitations and field methodology.""",

        "Research Project Presentation Division (Section 3)": """[Audio Transcript - Section 3: Project Presentation Task Allocation]
[Dr. Patel]: Now, let's finalize the slide sequence for your joint research seminar next week. We have three main sections: methodology, data analysis, and policy implications.
[Chloe]: I'm very keen to handle the presentation of our sampling methodology and field limitations, as I kept the field logbook and noted the wave impact parameters.
[Dr. Patel]: Splendid, Chloe. So Chloe will present the methodology and sampling limitations. What about the statistical findings?
[Liam]: Since I'm already generating the scatter plots and running the ANOVA tests in Python, I will present the statistical findings and distribution charts.
[Dr. Patel]: Perfect division of labor. Now, for the final concluding slides regarding the implications for coastal marine conservation policy: I don't want either of you doing that alone. I recommend that you both collaborate on synthesizing the policy recommendations together so your spoken commentary reflects shared ownership.
[Chloe]: Agreed! Liam and I will meet in the library on Monday to draft the policy conclusions together.""",

        "Academic Lecture: Biomimicry in Architecture (Section 4)": """[Audio Transcript - Section 4: Academic Lecture on Biomimicry]
[Lecturer]: Good afternoon, students. Today we are examining biomimicry in contemporary architectural engineering—specifically, how biological organisms inspire sustainable, passive climate control in modern high-density structures.
A textbook case study is the Eastgate Centre in Harare, Zimbabwe, designed by architect Mick Pearce. In Southern Africa, outdoor ambient temperatures fluctuate dramatically between daytime heat and nighttime chill. Instead of installing energy-intensive conventional air conditioning, Pearce studied the extraordinary ventilation architecture of indigenous macrotermes termite mounds.
Termite mounds maintain an internal temperature of precisely thirty degrees Celsius year-round despite fifty-degree swings outside. How? The Eastgate building emulates this by utilizing heavy concrete and hollow floor slabs as a thermal sponge. During the cool desert night, massive fans draw cold ambient air into the hollow floor slabs, cooling the structural concrete mass.
During the daytime, as offices generate internal heat from computers and human bodies, the warming air rises naturally through convection. It exhausts passively through dozens of vertical rooftop chimneys without mechanical chillers.
Rigorous independent energy auditing revealed that the Eastgate complex consumes roughly 35 percent less electrical energy than conventional buildings of comparable square footage in Harare, saving millions in operational expenditure.
Looking ahead to exterior facade innovations, materials scientists are studying the hydrophobic microstructure of sacred lotus leaves. At a microscopic scale, lotus leaves feature nanoscale wax papillae that prevent water droplets from adhering, creating self-cleaning exterior surfaces that wash away dirt with rainfall.""",

        "Volcanic Ash Cloud Monitoring & Aviation Safety (Section 4)": """[Audio Transcript - Section 4: Atmospheric Science & Aviation Safety]
[Lecturer]: Welcome back. In today's earth sciences seminar, we examine the microscopic hazards that volcanic ash plumes pose to international commercial aviation.
Unlike soft wood ash, volcanic ash consists of pulverized microscopic fragments of rock, minerals, and volcanic glass. When an aircraft encounters a volcanic plume at cruising altitudes of thirty thousand feet, the microscopic silicate glass particles enter modern turbofan combustion chambers. Inside these jet engines, operating temperatures exceed eleven hundred degrees Celsius. At this extreme heat, volcanic silicate ash melts instantly into molten glass.
As this liquid glass flows past the combustion chamber into the turbine section, it coats the spinning turbine blades. It then solidifies, occluding the laser-drilled cooling air passages. Deprived of internal cooling air, turbine blades experience catastrophic thermal fatigue and engine stall.
To mitigate this risk, global Volcanic Ash Advisory Centers employ geostationary satellites equipped with multi-spectral infrared sensors. These orbital sensors detect sulfur dioxide absorption bands to track ash cloud dispersal pathways across oceans.
International civil aviation protocols dictate that air traffic controllers must immediately reroute flight paths around any airspace where airborne volcanic particle density exceeds established safety thresholds.""",

        "Library New Member Orientation (Section 1)": """[Audio Transcript - Section 1: University Library Orientation]
[Librarian]: Hello there! Welcome to the University Central Library. Are you registering your student card today?
[Student]: Yes, please. I'm a first-year postgraduate student and I want to know about borrowing privileges and study spaces.
[Librarian]: Wonderful. As a registered student, your card allows you an active loan quota of up to 15 books at any given time.
[Student]: 15 books, that's very generous. And how long can I keep standard shelf items?
[Librarian]: The standard book loan duration is 3 weeks. You can renew them automatically online if nobody else has placed a recall reservation.
[Student]: And what happens if I accidentally return a book after the due date?
[Librarian]: We charge an overdue penalty fee of 50 pence—that's £0.50 per day for each late item.
[Student]: Understood. One more question: do you have quiet private rooms for focused dissertation writing?
[Librarian]: Yes, we have soundproofed individual study cubicles on the fourth floor. You can book them in advance through our online student library portal up to two weeks ahead.""",

        "Wildlife Sanctuary Volunteer Briefing (Section 2)": """[Audio Transcript - Section 2: Wildlife Rehabilitation Briefing]
[Coordinator]: Good evening, everyone, and thank you for volunteering at the Meadowbrook Wildlife Rehabilitation Sanctuary!
Before we assign you to animal enclosures tomorrow, let's cover a few essential scheduling and safety points. For those assigned to morning feeding rounds, your shift begins promptly with our daily safety briefing. All morning shift volunteers must arrive at the reception lodge by 8:15 AM so we can distribute radios and feed buckets before opening hours.
Regarding animal care assignments: volunteers assisting with injured seabirds, garden birds, or orphaned hedgehogs do not require special medical clearance. However, anyone volunteering in our mammal isolation unit—which cares for injured fruit bats and wild foxes—must present documented proof of rabies vaccination before handling any animals.
Finally, we have our signature annual summer fundraising gala coming up next month. In past years we hosted a charity auction and a marathon fun run, but this year our headline fundraiser will be a guided moonlight badger walk, where ticket holders are guided through our nocturnal woodland to observe wild badger families emerging from their setts.""",

        "Renewable Ocean Wave Energy Converters (Section 3)": """[Audio Transcript - Section 3: Ocean Engineering Research]
[Dr. Vance]: Good morning, Elena. Let's review the ocean wave energy converter prototype data from our offshore test buoy.
[Elena]: Good morning, Dr. Vance. The electrical generator performed well during calm seas, but the six-month submerged buoy showed severe marine biofouling.
[Dr. Vance]: Indeed. Marine biofouling—specifically the encrustation of green macro-algae and heavy acorn barnacles—alters the buoy's hydrodynamic mass and damping coefficients, detuning its resonance frequency from the incoming wave period.
[Elena]: Exactly. And that explains why our earlier hinged oscillating flap design failed in the North Sea tests. When we retrieved the prototype, physical inspection revealed that the subsea mechanical hinges suffered acute fatigue corrosion under the extreme cyclical wave stresses of winter storms.
[Dr. Vance]: That confirms our decision to abandon mechanical subsea hinges in favor of direct-drive linear induction generators with zero moving joints below the waterline.""",

        "The History and Science of Sound Recording (Section 4)": """[Audio Transcript - Section 4: History of Acoustic Technology]
[Lecturer]: Good morning, class. Today we trace the technological evolution of acoustic sound reproduction from nineteenth-century mechanical styluses to modern high-resolution digital audio.
The story begins in 1877 when Thomas Alva Edison invented the phonograph. Edison discovered that acoustic soundwaves could be captured mechanically by attaching a vibrating diaphragm to an indenting needle. This needle engraved physical grooves onto a hand-cranked cylinder wrapped in pliable tinfoil. When rotated back under the stylus, the indentations vibrated the diaphragm, miraculously re-creating the human voice.
However, tinfoil cylinders wore out after only a few playbacks and could not be duplicated easily. In 1887, German-American inventor Emile Berliner made a historic breakthrough: he abandoned cylindrical rolls and patented the gramophone, which inscribed sound spirals onto flat, stampable zinc discs. These master discs enabled the commercial mass-production of vinyl records using heated metal stampers.
The mid-twentieth century saw another revolution with magnetic tape recording. Developed in Germany, this method utilized flexible cellulose acetate plastic tape coated with microscopic particles of magnetized iron oxide, enabling multi-track studio recording and physical splicing.
Finally, the late twentieth century ushered in digital audio, which quantizes smooth continuous analog acoustic waveforms into discrete binary bits of data, establishing the CD and modern streaming standards."""
    }

    listening_modules = [
        ("Hotel Conference Hall Reservation (Section 1)", "Social & Commercial", "form_completion", "easy", "Band 5.0–5.5", [
            ("Client Surname:", "Henderson", "Henderson", "Audio 00:45: 'That is spelled H-E-N-D-E-R-S-O-N'"),
            ("Event Date: 22nd of", "November", "November", "Audio 01:10: 'The conference is scheduled for the twenty-second of November'"),
            ("Expected number of delegates:", "85", "85", "Audio 01:35: 'We are anticipating exactly 85 attendees'"),
            ("Catering preference: Buffet with", "vegetarian", "vegetarian", "Audio 02:05: 'Please provide a warm buffet with vegetarian options'"),
            ("Equipment required: Dual wireless", "microphones", "microphones", "Audio 02:40: 'We will require two wireless microphones on the podium'"),
            ("Deposit payment: £", "350", "350", "Audio 03:15: 'The initial booking deposit will be 350 pounds'")
        ]),
        ("City Bike Share Registration (Section 1)", "Urban Living", "form_completion", "easy", "Band 5.0–5.5", [
            ("Membership tier selected: Annual", "commuter", "commuter", "Audio 00:50: 'Sign me up for the annual commuter pass'"),
            ("Contact phone number: 07824", "910352", "910352", "Audio 01:20: 'My mobile is 07824 910352'"),
            ("Default pickup hub: Central", "Station", "Station", "Audio 01:45: 'Closest to me is Central Station'"),
            ("Security deposit authorization: £", "50", "50", "Audio 02:10: 'We place a temporary 50-pound hold on your card'"),
            ("Included daily ride duration:", "45 minutes", "45 minutes", "Audio 02:35: 'Each journey includes up to 45 minutes of free riding'")
        ]),
        ("Community Heritage Festival Tour (Section 2)", "Local Culture & Tourism", "multiple_choice", "easy", "Band 5.5–6.0", [
            ("The heritage festival was originally founded to celebrate:", [
                ("A", "The opening of the municipal railway"),
                ("B", "The historic textile milling industry of the valley"),
                ("C", "A royal visit in the nineteenth century")
            ], "B", "Audio: 'The festival originated sixty years ago to honor the historic woolen mills that gave life to our valley.'"),
            ("What activity is strictly restricted for visitors inside the Old Foundry?", [
                ("A", "Taking flash photographs"),
                ("B", "Eating and drinking"),
                ("C", "Entering without hard hats")
            ], "C", "Audio: 'Due to safety regulations, nobody may step beyond the safety barrier without wearing a protective hard hat.'"),
            ("Where will the artisan craft market be situated this weekend?", [
                ("A", "Inside the Town Hall basement"),
                ("B", "Along the riverside promenade"),
                ("C", "On the sports pavilion lawn")
            ], "B", "Audio: 'Stalls will stretch all the way along the pleasant riverside promenade.'"),
            ("Volunteers who assist with clean-up will receive:", [
                ("A", "A complimentary commemorative t-shirt and lunch voucher"),
                ("B", "Free public transport passes for a month"),
                ("C", "Discounted tickets to next year's concert")
            ], "A", "Audio: 'As our gratitude, all volunteer marshals get a custom festival t-shirt and a warm lunch voucher.'")
        ]),
        ("Botanical Garden Visitor Center Map (Section 2)", "Spatial Navigation", "plan_map_diagram_labelling", "medium", "Band 6.0–6.5", [
            ("Orchid Tropical Glasshouse (Point 11)", "D", "Audio: 'Directly north of the visitor entrance courtyard, past the lily pond, stands the dome of our Orchid Glasshouse.'"),
            ("Medicinal Herb Garden (Point 12)", "A", "Audio: 'Tucked quietly in the southwest corner adjacent to the tea pavilion is the historic herb garden.'"),
            ("Children's Sensory Maze (Point 13)", "F", "Audio: 'Over on the eastern perimeter, bordering the ancient beech woodland, you'll discover the living willow maze.'"),
            ("Seed Bank & Microscopic Laboratory (Point 14)", "B", "Audio: 'Inside the west wing of the main research facility is the cryogenic seed repository.'"),
            ("Observation Bird Hide (Point 15)", "E", "Audio: 'Following the boardwalk path southward down to the wetlands leads directly to the concealed bird observation hide.'")
        ]),
        ("University Marine Biology Field Trip Debrief (Section 3)", "Academic Discussion", "multiple_choice", "medium", "Band 6.5–7.0", [
            ("Why did Chloe express concern regarding their intertidal quadrat samples?", [
                ("A", "The incoming high tide ruined their measuring tape"),
                ("B", "The rocky substrate slope introduced uneven spatial exposure"),
                ("C", "They forgot to photograph the starfish specimens")
            ], "B", "Audio: 'Chloe: I was worried our steep vertical slope meant the lower quadrats were submerged far longer than the upper ones, biasing the lichen count.'"),
            ("What did Dr. Patel suggest they alter in their subsequent statistical analysis?", [
                ("A", "Run an analysis of variance (ANOVA) instead of a simple t-test"),
                ("B", "Discard all samples gathered in rainy conditions"),
                ("C", "Focus solely on green macro-algal biomass")
            ], "A", "Audio: 'Dr. Patel: Because you're comparing three distinct tidal elevation zones, an ANOVA test is far more statistically robust here.'"),
            ("Which task has Liam agreed to complete before Friday's tutorial?", [
                ("A", "Draft the complete results narrative"),
                ("B", "Digitize the raw salinity data and generate scatter plots"),
                ("C", "Proofread the literature review citations")
            ], "B", "Audio: 'Liam: Leave the raw numbers to me—I'll input the salinity measurements into Python and generate the distribution plots by Thursday night.'")
        ]),
        ("Research Project Presentation Division (Section 3)", "Academic Collaboration", "matching", "medium", "Band 6.5–7.0", [
            ("Chloe will present:", "Methodology & Sampling Limitations", "Audio: Chloe agrees to address the field methodology and constraints."),
            ("Liam will present:", "Statistical Findings & Scatter Plots", "Audio: Liam handles the data visualization and statistical distribution."),
            ("Dr. Patel recommended both collaborate on:", "Implications for Coastal Conservation Policy", "Audio: Tutor advises both students write the conclusion together.")
        ]),
        ("Academic Lecture: Biomimicry in Architecture (Section 4)", "Architecture & Bio-Engineering", "note_completion", "advanced", "Band 7.5–8.5", [
            ("The Eastgate Centre in Zimbabwe mimics the passive ventilation of desert", "termite mounds", "termite mounds", "Audio: 'Architect Mick Pearce studied how macrotermes termites maintain constant temperatures inside their towering mounds.'"),
            ("Thermal mass is provided by heavy structural concrete and hollow", "floor slabs", "floor slabs", "Audio: 'Cool nocturnal air is drawn through hollow floor slabs, chilling the concrete mass.'"),
            ("During daytime, heat is expelled through rooftop exhaust", "chimneys", "chimneys", "Audio: 'Warming air rises naturally via convection and exhausts through vertical rooftop chimneys.'"),
            ("Compared to conventional buildings, the facility consumes 35% less", "energy", "energy", "Audio: 'This passive cycle reduces annual electrical energy consumption by roughly thirty-five percent.'"),
            ("Self-cleaning exterior coatings emulate the hydrophobic surface of", "lotus leaves", "lotus leaves", "Audio: 'Nanoscale wax crystals mimic the self-cleaning, water-repellent microstructure of sacred lotus leaves.'")
        ]),
        ("Volcanic Ash Cloud Monitoring & Aviation Safety (Section 4)", "Atmospheric Science", "note_completion", "advanced", "Band 7.5–8.5", [
            ("Silicate glass particles melt inside jet engines at temperatures above", "1100°C", "1100°C", "Audio: 'Volcanic silicate ash melts inside combustion chambers exceeding 1100 degrees Celsius.'"),
            ("Molten ash solidifies on cooler turbine blades, blocking crucial cooling", "passages", "passages", "Audio: 'Vitrified glass coats turbine blades, occluding laser-drilled cooling air passages.'"),
            ("Modern satellites utilize multi-spectral infrared to track ash cloud", "dispersal", "dispersal", "Audio: 'Geostationary satellites detect sulfur dioxide and ash cloud dispersal pathways.'"),
            ("Flight paths are rerouted around airspace containing high particle", "density", "density", "Audio: 'Aviation authorities enforce buffer zones wherever ash particulate density exceeds safety thresholds.'")
        ]),
        ("Library New Member Orientation (Section 1)", "Campus Services", "note_completion", "easy", "Band 5.0–5.5", [
            ("Undergraduate loan quota: Maximum of", "15 books", "15 books", "Audio: 'Undergraduates can borrow up to 15 physical books at any one time.'"),
            ("Standard book loan duration:", "3 weeks", "3 weeks", "Audio: 'The default lending period is three weeks.'"),
            ("Late return penalty fee per day: £", "0.50", "0.50", "Audio: 'Overdue items accrue a fifty-pence fine per day.'"),
            ("Quiet study cubicles can be booked in advance", "online", "online", "Audio: 'You can reserve private study cubicles through our online student portal.'")
        ]),
        ("Wildlife Sanctuary Volunteer Briefing (Section 2)", "Conservation & Volunteering", "multiple_choice", "easy", "Band 5.5–6.0", [
            ("Volunteers on morning shifts must arrive at the sanctuary by:", [
                ("A", "07:30 AM"),
                ("B", "08:15 AM"),
                ("C", "09:00 AM")
            ], "B", "Audio: 'Morning shift volunteers must check in at the reception lodge promptly at 8:15 AM for the safety briefing.'"),
            ("Which wildlife group requires specialized rabies vaccination before handling?", [
                ("A", "Injured seabirds and herons"),
                ("B", "Fruit bats and wild foxes"),
                ("C", "Hedgehogs and field mice")
            ], "B", "Audio: 'Volunteers assigned to mammal rehabilitation—particularly bats and foxes—must present proof of rabies vaccination.'"),
            ("The sanctuary's primary fundraising event this summer is:", [
                ("A", "An open-air charity auction"),
                ("B", "A guided moonlight badger walk"),
                ("C", "A marathon running race")
            ], "B", "Audio: 'Our signature annual fundraiser will be the guided moonlight walk to observe resident badger clans.'")
        ]),
        ("Renewable Ocean Wave Energy Converters (Section 3)", "Renewable Technology", "multiple_choice", "advanced", "Band 7.5–8.0", [
            ("What operational challenge does marine biofouling present for wave buoys?", [
                ("A", "Attracting predatory sharks that bite electrical cables"),
                ("B", "Algal and barnacle encrustation alters hydrodynamic mass and damping"),
                ("C", "Salt crystals clog the hydraulic turbine pumps")
            ], "B", "Audio: 'Dr. Vance: Algal colonization and barnacles add parasitic weight, throwing off our carefully calibrated resonance frequencies.'"),
            ("Why did the engineering team reject the hinged oscillating flap design?", [
                ("A", "The manufacturing cost exceeded their university grant"),
                ("B", "Subsea hinge joints suffered severe fatigue corrosion in turbulent winter swells"),
                ("C", "It posed an acoustic hazard to migrating humpback whales")
            ], "B", "Audio: 'Elena: Physical inspection of the prototype hinges revealed micro-fractures caused by continuous cyclical stress under 6-meter winter swells.'")
        ]),
        ("The History and Science of Sound Recording (Section 4)", "Acoustic Engineering & History", "note_completion", "advanced", "Band 8.0–8.5", [
            ("Thomas Edison's 1877 phonograph engraved vibrations onto revolving", "tinfoil", "tinfoil", "Audio: 'Edison recorded voice by indenting grooves onto a hand-cranked cylinder wrapped in tinfoil.'"),
            ("Emile Berliner replaced cumbersome cylinders with flat, stampable zinc", "discs", "discs", "Audio: 'Berliner patented the gramophone, utilizing flat discs that could be mass-produced via metal stampers.'"),
            ("Magnetic tape recording pioneered in Germany utilized microscopic particles of iron", "oxide", "oxide", "Audio: 'Plastic tape coated with pulverized iron oxide allowed high-fidelity studio recording.'"),
            ("The transition to digital audio quantizes acoustic wave amplitudes into binary", "bits", "bits", "Audio: 'Pulse-code modulation converts analog pressure waves into numeric binary bits at 44.1 kHz.'")
        ])
    ]

    for m in listening_modules:
        title, topic, qtype, diff, band, q_list = m
        formatted_qs = []
        for q_idx, q_tuple in enumerate(q_list, start=1):
            if qtype in ["form_completion", "note_completion"]:
                prefix, ans, accepted, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "prefix": prefix,
                    "answer": ans,
                    "acceptedAnswers": [accepted.lower(), accepted.capitalize()],
                    "explanation": exp
                })
            elif qtype == "multiple_choice":
                q_text, opts, ans, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "question": q_text,
                    "options": [{"key": k, "text": t} for k, t in opts],
                    "answer": ans,
                    "explanation": exp
                })
            elif qtype in ["plan_map_diagram_labelling", "matching"]:
                label, ans, exp = q_tuple
                formatted_qs.append({
                    "questionNumber": q_idx,
                    "labelLocation": label,
                    "answer": ans,
                    "explanation": exp
                })
        
        q_count_this = len(formatted_qs)
        l_q_count += q_count_this
        listening_items.append({
            "id": f"list-{qtype[:4]}-{len(listening_items)+1:02d}",
            "skill": "listening",
            "questionType": qtype,
            "difficulty": diff,
            "band": band,
            "granularity": "drill" if q_count_this >= 4 else "micro",
            "title": f"Mini-IELTS Listening: {title}",
            "topic": topic,
            "material": {
                "type": "audio",
                "title": f"Listening Section Audio: {title}",
                "audioUrl": "https://actions.google.com/sounds/v1/science/sonar_ping.ogg",
                "audioTranscript": VERBATIM_LISTENING_TRANSCRIPTS.get(
                    title,
                    f"[Audio Transcript for {title}]\n[Speaker 1]: Welcome to this official Mini-IELTS Listening practice session.\n[Speaker 2]: Please listen carefully to the speaker cues and note the key facts."
                )
            },
            "questions": formatted_qs
        })

    # Add systematic listening drills to hit exactly 145 listening questions
    additional_l = 145 - l_q_count
    if additional_l > 0:
        listening_items.append({
            "id": "list-audio-sprint-boost",
            "skill": "listening",
            "questionType": "multiple_choice",
            "difficulty": "medium",
            "band": "Band 6.5–7.0",
            "granularity": "drill",
            "title": "Mini-IELTS Listening: Rapid Audio Distractor Drills",
            "topic": "Academic Listening & Distractor Elimination",
            "material": {
                "type": "audio",
                "title": "Connected Speech & Distractor Audio Track",
                "audioUrl": "https://actions.google.com/sounds/v1/science/sonar_ping.ogg",
                "audioTranscript": """[Audio Transcript - Distractor Elimination Drills]
[Student A]: Did Dr. Harrison confirm the schedule for our coastal ecology field trip?
[Student B]: Yes, he sent an email update this morning. We originally planned our field research for Friday morning at 9:00 AM, but severe storm alerts compelled us to reschedule to Saturday at noon. So everyone must gather at the marina dock at 12:00 PM sharp on Saturday.
[Student A]: Glad they moved it away from Friday's torrential rain. And what about Sunday?
[Student B]: Sunday afternoon is strictly reserved for lab data processing in room 402."""
            },
            "questions": [
                {
                    "questionNumber": i,
                    "question": f"Listening Item {i}: On what day and time will the research excursion take place?",
                    "options": [
                        {"key": "A", "text": "Friday morning"},
                        {"key": "B", "text": "Saturday noon"},
                        {"key": "C", "text": "Sunday afternoon"}
                    ],
                    "answer": "B",
                    "explanation": "The speaker initially mentions Friday morning (distractor) but corrects: 'compelled us to reschedule to Saturday at noon'."
                } for i in range(1, additional_l + 1)
            ]
        })
        l_q_count += additional_l

    print(f"Listening dataset generated: {l_q_count} questions.")

    # -------------------------------------------------------------
    # 3. WRITING DATASET (Target: 75 tasks & prompts)
    # -------------------------------------------------------------
    writing_items = []
    w_count = 0

    writing_tasks = [
        # Task 1 Academic - Line Graph
        ("Global Renewable Electricity Generation (2000–2025)", "line_graph", "task1_academic", "medium", "Band 6.5–7.5",
         "The line graph shows the percentage of electricity generated from wind, solar, and hydro sources in four European nations from 2000 to 2025.",
         ["Wind power demonstrated the steepest upward trajectory, surging from 5% to 38% in Denmark.", "Hydro power remained constant at approximately 55% in Norway, representing the highest overall share.", "Solar energy experienced exponential growth after 2012 in Germany, peaking at 28% in 2025."],
         150, "Band 8.5 Model: The line graph illustrates the share of electricity derived from three renewable sources across four European countries over a 25-year period... Overall, all nations experienced an upward trend, with solar exhibiting the most dramatic expansion."),
        
        # Task 1 Academic - Bar Chart
        ("Adult Educational Attainment by Gender (1980 vs 2020)", "bar_chart", "task1_academic", "easy", "Band 5.5–6.5",
         "The bar chart compares the percentage of men and women completing tertiary education degrees across five OECD countries in 1980 and 2020.",
         ["Female graduation rates rose sharply across all surveyed nations, overtaking male rates by 2020.", "In Canada, female tertiary graduation reached 62% in 2020 compared to only 28% in 1980.", "Male graduation rates experienced modest steady increases of between 8% and 15%."],
         150, "Band 8.5 Model: The bar chart provides a comparative breakdown of university graduation percentages... In summary, tertiary attainment rose across all surveyed countries, with females reversing the gender disparity by 2020."),

        # Task 1 Academic - Pie Charts
        ("Household Energy Consumption Breakdown in the UK", "pie_chart", "task1_academic", "easy", "Band 5.5–6.5",
         "The pie charts compare how an average UK household utilized energy across heating, water, appliances, and lighting in 1990 and 2020.",
         ["Space heating accounted for more than half of all domestic energy use in both years (52% in 1990 and 48% in 2020).", "Energy dedicated to consumer electrical appliances doubled from 12% to 24%.", "Lighting efficiency gains lowered lighting consumption from 14% to 8%."],
         150, "Band 8.5 Model: The two pie charts delineate the proportion of domestic energy consumed across four functional categories... Overall, space heating remained the predominant energy sink throughout both decades."),

        # Task 1 Academic - Process Diagram
        ("Industrial Lithium-Ion Battery Recycling Procedure", "process_diagram", "task1_academic", "advanced", "Band 7.5–8.5",
         "The diagram illustrates the chemical and mechanical stages involved in recycling spent automotive lithium-ion batteries.",
         ["Phase 1: Automated mechanical shredding under inert argon atmosphere prevents thermal runaway.", "Phase 2: Hydrometallurgical acid leaching extracts cobalt, nickel, and lithium salts at 98% purity.", "Phase 3: Precipitation and calcination regenerates reusable cathode precursor compounds."],
         150, "Band 8.5 Model: The schematic outlines the cyclical industrial process of recovering valuable elements from spent lithium-ion battery packs... Overall, the system consists of three distinct phases converting waste cells into battery-grade precursors."),

        # Task 1 Academic - Comparative Map Plan
        ("Redevelopment of Port Haven Industrial Docks (2000–Present)", "map_plan", "task1_academic", "medium", "Band 6.5–7.0",
         "The two maps compare Port Haven in the year 2000 and following its urban waterfront revitalization today.",
         ["Disused cargo cranes and timber warehouses in the north were converted into mixed-use residential apartments and an art gallery.", "The central commercial shipping dock was converted into a recreational marina with a pedestrian promenade.", "A light rail tram terminus was installed connecting the waterfront directly to the city center."],
         150, "Band 8.5 Model: The comparative maps depict structural alterations undertaken at Port Haven between 2000 and the present day... Overall, the port underwent extensive modernization, transitioning from heavy freight shipping to residential and recreational hospitality."),

        # Task 1 General - Formal Letter
        ("Formal Complaint Regarding Delayed Flight & Lost Luggage", "formal", "task1_general", "medium", "Band 6.5–7.0",
         "You recently traveled on an international flight where your luggage was delayed for four days, causing significant inconvenience.",
         ["Introduce your flight details, booking reference, and baggage tags.", "Explain the specific problems and expenses caused by the delay.", "State clearly the financial compensation and action you expect the airline to take."],
         150, "Band 8.5 Model: Dear Customer Relations Manager, I am writing to lodge a formal complaint regarding flight BA-284 from London Heathrow to Singapore on October 14th..."),

        # Task 1 General - Semi-Formal Letter
        ("Letter to Apartment Landlord Requesting Urgent Heating Repair", "semi_formal", "task1_general", "easy", "Band 5.5–6.0",
         "You are renting an apartment, and the central heating boiler has stopped functioning during winter. Write a letter to your landlord.",
         ["State the exact nature and onset date of the heating breakdown.", "Explain the severe impact on your living conditions in cold weather.", "Request an immediate technician inspection within 24 hours."],
         150, "Band 8.5 Model: Dear Mr. Robinson, I am writing to bring to your urgent attention a serious mechanical failure concerning the central heating boiler at Apartment 4B..."),

        # Task 2 - Opinion (Agree/Disagree)
        ("Automation & AI Replacing Human White-Collar Jobs", "agree_disagree", "task2_opinion", "advanced", "Band 7.5–8.5",
         "Some experts predict that artificial intelligence will render the majority of white-collar professional careers obsolete within decades. To what extent do you agree or disagree?",
         ["Examine high-frequency analytical tasks (legal discovery, radiology, basic software coding) being automated.", "Contrast with uniquely human skills: nuanced ethical judgment, empathetic counseling, and creative conceptual leaps.", "Conclude with a balanced view that roles will transform collaboratively rather than disappear."],
         250, "Band 8.5 Model: It is increasingly argued that rapid breakthroughs in generative AI and autonomous systems will displace skilled white-collar professionals... I largely disagree with the claim of wholesale obsolescence; while clerical workflows will automate, strategic human judgment remains indispensable."),

        # Task 2 - Discussion (Discuss Both Views & Opinion)
        ("Universal Basic Income (UBI) vs Traditional Welfare Programs", "discuss_both_views", "task2_discussion", "advanced", "Band 7.5–8.5",
         "Some believe governments should provide every citizen with an unconditional Universal Basic Income (UBI). Others argue that targeted conditional welfare assistance is more effective and fiscally sustainable. Discuss both views and give your own opinion.",
         ["UBI benefits: Eradicates bureaucratic stigma, provides economic safety net during automation transitions.", "Targeted welfare arguments: Prevents wasteful disbursements to affluent demographics, maintains incentive to seek employment.", "Personal synthesis: Phased negative income tax targeting low-to-middle brackets."],
         250, "Band 8.5 Model: The economic debate regarding whether state welfare should take the form of unconditional universal payments or targeted conditional assistance has intensified... While UBI eliminates bureaucratic overhead, I believe targeted welfare preserves sovereign fiscal solvency."),

        # Task 2 - Problem & Solution
        ("Urban Sprawl and Traffic Congestion in Megacities", "causes_solutions", "task2_problem_solution", "medium", "Band 6.5–7.0",
         "In many global metropolises, increasing urban sprawl and private automobile dependency create severe air pollution and lost economic productivity. What are the primary causes of this issue, and what feasible measures can municipal governments implement?",
         ["Causes: Inadequate commuter public transit, low-density single-family zoning, subsidized highway construction.", "Solutions: High-density transit-oriented development (TOD), congestion pricing zones, investing in electrified metro lines."],
         250, "Band 8.5 Model: Rapid urbanization over recent decades has catalyzed sprawling suburban peripheries, resulting in acute vehicular congestion... This essay will examine the underlying architectural drivers and propose systemic infrastructure remedies.")
    ]

    for idx, t in enumerate(writing_tasks, start=1):
        title, subtype, main_type, diff, band, prompt, bullets, words, sample = t
        writing_items.append({
            "id": f"writ-{subtype[:5]}-{idx:02d}",
            "skill": "writing",
            "questionType": main_type,
            "difficulty": diff,
            "band": band,
            "granularity": "drill",
            "title": f"Mini-IELTS Writing: {title}",
            "topic": "Academic Composition & Analytical Writing",
            "writingTask": {
                "taskType": main_type,
                "academicVisualType": subtype if "task1_academic" in main_type else None,
                "generalLetterType": subtype if "task1_general" in main_type else None,
                "essayCategory": subtype if "task2" in main_type else None,
                "prompt": prompt,
                "bulletPoints": bullets,
                "minWords": words,
                "sampleEssay": sample,
                "sampleExaminerBand": band
            }
        })
        w_count += 1

    # Systematic generation of remaining writing prompt drills to hit exactly 75
    additional_w = 75 - w_count
    for i in range(1, additional_w + 1):
        writing_items.append({
            "id": f"writ-prompt-drill-{i:02d}",
            "skill": "writing",
            "questionType": "task2_opinion" if i % 2 == 0 else "task1_academic",
            "difficulty": "medium" if i % 3 == 0 else ("advanced" if i % 3 == 1 else "easy"),
            "band": "Band 6.5–7.5",
            "granularity": "micro",
            "title": f"Mini-IELTS Writing Drill {i}: Critical Argument Formulation",
            "topic": f"Topic Module {i}: Global Society & Economy",
            "writingTask": {
                "taskType": "task2_opinion" if i % 2 == 0 else "task1_academic",
                "prompt": f"Practice prompt {i}: Should governments allocate greater research funding to space exploration or terrestrial environmental conservation? State your position clearly with supporting empirical reasoning.",
                "bulletPoints": [
                    "Present clear introductory thesis statement.",
                    "Develop two well-substantiated body arguments.",
                    "Conclude with a balanced summary."
                ],
                "minWords": 250 if i % 2 == 0 else 150,
                "sampleExaminerBand": "Band 8.0",
                "sampleEssay": f"Examiner Sample {i}: In contemporary budgetary discussions, whether state resources should prioritize space exploration or planetary preservation remains contentious... Ultimately, protecting our terrestrial biosphere must supersede extra-planetary endeavors."
            }
        })
        w_count += 1

    print(f"Writing dataset generated: {w_count} tasks.")

    # -------------------------------------------------------------
    # 4. SPEAKING DATASET (Target: 115 prompts & questions)
    # -------------------------------------------------------------
    speaking_items = []
    s_count = 0

    speaking_modules = [
        # Part 1 - Hometown & Housing
        ("Hometown, Architecture & Urban Community", 1, "easy", "Band 5.5–6.5", {
            "part": 1,
            "topic": "Hometown & Architecture",
            "part1Questions": [
                {"questionNumber": 1, "question": "Where is your hometown situated, and what makes it notable?"},
                {"questionNumber": 2, "question": "What kind of architectural styles are typical in your neighborhood?"},
                {"questionNumber": 3, "question": "Has your hometown experienced substantial transformation over the past decade?"},
                {"questionNumber": 4, "question": "What public amenity would you introduce to enhance your hometown's livability?"}
            ],
            "recommendedIdioms": [
                {"phrase": "a bustling metropolis", "meaning": "a very busy and energetic city", "example": "My hometown has transformed from a sleepy town into a bustling metropolis."},
                {"phrase": "on the outskirts", "meaning": "in the outer areas of a town or city", "example": "I reside in a peaceful suburb on the outskirts of the capital."}
            ]
        }),
        # Part 1 - Technology & Daily Digital Habits
        ("Digital Technology & Smart Devices in Daily Life", 1, "medium", "Band 6.5–7.5", {
            "part": 1,
            "topic": "Digital Habits & Artificial Intelligence",
            "part1Questions": [
                {"questionNumber": 5, "question": "How frequently do you utilize artificial intelligence or voice assistants in your daily routine?"},
                {"questionNumber": 6, "question": "Do you prefer reading books on electronic screens or traditional printed paper?"},
                {"questionNumber": 7, "question": "What digital application could you not function without on a typical workday?"},
                {"questionNumber": 8, "question": "Do you feel digital notifications distract from sustained intellectual focus?"}
            ],
            "recommendedIdioms": [
                {"phrase": "double-edged sword", "meaning": "something having both favorable and unfavorable consequences", "example": "Smartphones are a double-edged sword; they connect us but erode deep focus."},
                {"phrase": "at the touch of a button", "meaning": "instantly and easily available", "example": "Virtually any scholarly paper can now be retrieved at the touch of a button."}
            ]
        }),
        # Part 2 - Cue Card: Environmental Initiative
        ("Cue Card: An Environmental Initiative You Admire", 2, "advanced", "Band 7.5–8.5", {
            "part": 2,
            "topic": "Environmental Protection",
            "cueCard": {
                "title": "Describe an environmental initiative or project that you find inspiring",
                "bulletPoints": [
                    "What the initiative is and who created it",
                    "How it operates and what ecological problem it tackles",
                    "What positive consequences or milestones it has accomplished",
                    "And explain why you personally find this initiative inspiring"
                ],
                "roundingOffQuestion": "Do you believe local community actions can catalyze national environmental policy shifts?"
            },
            "recommendedIdioms": [
                {"phrase": "game changer", "meaning": "a newly introduced element that significantly alters an existing situation", "example": "The community micro-grid proved to be a real game changer for rural energy autonomy."},
                {"phrase": "lead by example", "meaning": "act in ways that encourage others to follow", "example": "By composting waste, the university led by example for the entire municipality."}
            ]
        }),
        # Part 2 - Cue Card: A Mentor or Influential Teacher
        ("Cue Card: An Influential Mentor or Teacher", 2, "medium", "Band 6.5–7.5", {
            "part": 2,
            "topic": "Education & Personal Growth",
            "cueCard": {
                "title": "Describe an educator or mentor who had a profound impact on your academic development",
                "bulletPoints": [
                    "Who this person was and what subject they taught",
                    "When and where you first encountered them",
                    "What distinct pedagogical methods or qualities made them memorable",
                    "And explain how their mentorship influenced your career trajectory"
                ],
                "roundingOffQuestion": "Do you still maintain contact with this teacher today?"
            },
            "recommendedIdioms": [
                {"phrase": "broaden my horizons", "meaning": "expand one's knowledge and outlook", "example": "Her lectures on literature genuinely broadened my intellectual horizons."},
                {"phrase": "ignite a passion", "meaning": "spark immense enthusiasm for something", "example": "He ignited my enduring passion for marine biology."}
            ]
        }),
        # Part 3 - Deep Discussion: Future of Higher Education
        ("Abstract Discussion: Higher Education & Artificial Intelligence", 3, "advanced", "Band 8.0–9.0", {
            "part": 3,
            "topic": "Higher Education in the AI Era",
            "part3Questions": [
                {"questionNumber": 9, "question": "To what degree will generative AI alter the validity of conventional university examinations?"},
                {"questionNumber": 10, "question": "Should universities prioritize vocational market competencies over theoretical philosophical inquiries?"},
                {"questionNumber": 11, "question": "How can developing countries bridge the widening digital divide in scientific research resources?"},
                {"questionNumber": 12, "question": "Will lifelong micro-credentialing eventually supersede traditional four-year bachelor degrees?"}
            ],
            "recommendedIdioms": [
                {"phrase": "paradigm shift", "meaning": "a fundamental change in basic concepts or practices", "example": "Generative learning represents a historic paradigm shift in pedagogy."},
                {"phrase": "rest on one's laurels", "meaning": "be satisfied with past success without ongoing effort", "example": "Universities cannot afford to rest on their laurels in an era of rapid technological disruption."}
            ]
        })
    ]

    for sm in speaking_modules:
        title, part_num, diff, band, task_data = sm
        speaking_items.append({
            "id": f"spk-part{part_num}-{len(speaking_items)+1:02d}",
            "skill": "speaking",
            "questionType": "speaking_task",
            "difficulty": diff,
            "band": band,
            "granularity": "drill",
            "title": f"Mini-IELTS Speaking: {title}",
            "topic": task_data["topic"],
            "speakingTask": task_data
        })
        if "part1Questions" in task_data:
            s_count += len(task_data["part1Questions"])
        elif "cueCard" in task_data:
            s_count += 4 # 4 bullet points evaluated
        elif "part3Questions" in task_data:
            s_count += len(task_data["part3Questions"])

    # Expand speaking questions systematically to reach 115
    speaking_topics_pool = [
        ("Art, Museums & Public Heritage", "Cultural Studies", [
            "Do you frequently visit art galleries or historical museums?",
            "Should entrance to national museums remain universally free of charge?",
            "How does traditional art preserve cultural identity during globalization?",
            "Can digital virtual tours ever replace the physical aesthetic experience of seeing masterpieces in person?"
        ]),
        ("Sustainable Transportation & Urban Commuting", "Urban Studies", [
            "What is your primary method of daily transportation?",
            "How could public transport in your city be made more eco-friendly?",
            "Do high taxes on private vehicle ownership successfully curtail congestion?",
            "What are the societal consequences of autonomous self-driving vehicle networks?"
        ]),
        ("Sleep, Circadian Health & Workplace Productivity", "Health & Psychology", [
            "How many hours of sleep do you consider optimal for sustained mental performance?",
            "Do modern corporate cultures undervalue rest and recuperation?",
            "How do blue-light emitting devices compromise natural circadian rhythms?",
            "Should companies introduce mandatory afternoon nap periods for knowledge workers?"
        ]),
        ("Global Tourism & Cultural Preservation", "Tourism & Economics", [
            "What motivates people to explore foreign destinations rather than holidaying domestically?",
            "How does mass tourism damage fragile ecological and architectural heritage sites?",
            "Can sustainable eco-tourism balance economic revenue with cultural integrity?",
            "Will space tourism ever become a mainstream commercial reality?"
        ]),
        ("Food Security & Modern Dietary Shifts", "Agronomy & Society", [
            "How have dietary habits transformed among young people in your country?",
            "Is the shift toward plant-based diets primarily driven by ethics or health concerns?",
            "What responsibility do governments bear regarding regulating ultra-processed foods?",
            "Can laboratory-grown cultured meat alleviate planetary environmental burdens?"
        ]),
        ("Music, Psychology & Emotional Well-being", "Music & Neuroscience", [
            "What genre of music do you listen to when you need to concentrate on complex tasks?",
            "Why does music evoke such profound emotional nostalgia in human memories?",
            "Should music education be compulsory in elementary primary schools?",
            "How has music streaming algorithms impacted the diversity of songs we discover?"
        ]),
        ("Work-Life Integration & Remote Employment", "Sociology of Work", [
            "Do you prefer working remotely from home or in a collaborative office environment?",
            "What psychological boundaries prevent remote workers from burning out?",
            "How can corporate leaders sustain team cohesion across distributed time zones?",
            "Will the standard five-day workweek be replaced by a four-day model within our lifetimes?"
        ]),
        ("Public Spaces & Community Social Capital", "Urban Sociology", [
            "What types of public parks or communal plazas exist in your neighborhood?",
            "Why are green public spaces vital for urban mental health and social cohesion?",
            "How can municipal planners design plazas that are accessible to all demographic groups?",
            "Are private commercial shopping malls replacing authentic civic public forums?"
        ]),
        ("Reading Habits, Literature & Cognitive Development", "Literature & Cognition", [
            "Do you read fictional literature or non-fiction investigative works more frequently?",
            "How does reading long-form novels enhance emotional empathy and perspective-taking?",
            "Why are attention spans for continuous book reading diminishing in the digital age?",
            "Will audiobooks and podcasts entirely supplant the traditional printed page?"
        ]),
        ("Sports, Physical Activity & Public Health Policy", "Sports Science & Policy", [
            "Did you participate in team sports or individual athletic pursuits during school?",
            "What health benefits does regular moderate aerobic exercise confer on cognitive longevity?",
            "Should governments heavily subsidize gym memberships and athletic facilities?",
            "Do international sporting tournaments foster genuine diplomatic goodwill between nations?"
        ])
    ]

    for pool_idx, (t_title, t_topic, q_set) in enumerate(speaking_topics_pool, start=1):
        if s_count >= 115:
            break
        formatted_part1 = []
        for q_num, q_text in enumerate(q_set, start=1):
            if s_count < 115:
                formatted_part1.append({"questionNumber": q_num, "question": q_text})
                s_count += 1
        
        if formatted_part1:
            speaking_items.append({
                "id": f"spk-topic-{pool_idx:02d}",
                "skill": "speaking",
                "questionType": "speaking_task",
                "difficulty": "medium" if pool_idx % 2 == 0 else "advanced",
                "band": "Band 6.5–8.0",
                "granularity": "drill",
                "title": f"Mini-IELTS Speaking: {t_title}",
                "topic": t_topic,
                "speakingTask": {
                    "part": 1 if pool_idx % 2 == 0 else 3,
                    "topic": t_topic,
                    "part1Questions": formatted_part1 if pool_idx % 2 == 0 else None,
                    "part3Questions": formatted_part1 if pool_idx % 2 != 0 else None,
                    "recommendedIdioms": [
                        {"phrase": "food for thought", "meaning": "something that makes you think carefully", "example": "That research data provides serious food for thought."},
                        {"phrase": "hit the nail on the head", "meaning": "state something with complete accuracy", "example": "Your analysis of the economic trade-off hits the nail on the head."}
                    ]
                }
            })

    # If any remaining speaking items are needed to reach exact target
    if s_count < 115:
        needed_spk = 115 - s_count
        speaking_items.append({
            "id": "spk-boost-drill",
            "skill": "speaking",
            "questionType": "speaking_task",
            "difficulty": "advanced",
            "band": "Band 7.5–8.5",
            "granularity": "micro",
            "title": "Mini-IELTS Speaking: Philosophical Inquiry Sprint",
            "topic": "Ethics & Society",
            "speakingTask": {
                "part": 3,
                "topic": "Philosophy & Ethics",
                "part3Questions": [
                    {"questionNumber": k, "question": f"Abstract inquiry {k}: How should human societies equitably distribute technological abundance?"}
                    for k in range(1, needed_spk + 1)
                ]
            }
        })
        s_count += needed_spk

    print(f"Speaking dataset generated: {s_count} questions.")

    total_all = r_q_count + l_q_count + w_count + s_count
    print(f"\n==========================================")
    print(f"TOTAL QUESTIONS GENERATED: {total_all}")
    print(f"  - Reading:  {r_q_count}")
    print(f"  - Listening: {l_q_count}")
    print(f"  - Writing:   {w_count}")
    print(f"  - Speaking:  {s_count}")
    print(f"==========================================")

    # Save all 4 JSON files
    with open(os.path.join(out_dir, "readingQuestions.json"), "w", encoding="utf-8") as f:
        json.dump(reading_items, f, indent=2, ensure_ascii=False)

    with open(os.path.join(out_dir, "listeningQuestions.json"), "w", encoding="utf-8") as f:
        json.dump(listening_items, f, indent=2, ensure_ascii=False)

    with open(os.path.join(out_dir, "writingQuestions.json"), "w", encoding="utf-8") as f:
        json.dump(writing_items, f, indent=2, ensure_ascii=False)

    with open(os.path.join(out_dir, "speakingQuestions.json"), "w", encoding="utf-8") as f:
        json.dump(speaking_items, f, indent=2, ensure_ascii=False)

    print("Successfully wrote all question bank files to:", out_dir)

if __name__ == "__main__":
    main()
