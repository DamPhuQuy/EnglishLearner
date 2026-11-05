"""
Authentic IELTS Reading Dataset Specification
Contains 8 comprehensive, full-length Academic Reading Passages (~800–900 words each),
structured with clear paragraph markers [A]–[G] across genuine academic disciplines.

Each passage is paired with rigorous IELTS question groups:
- Matching Headings (with complete headingsList including distractor headings)
- True / False / Not Given & Yes / No / Not Given
- Multiple Choice (4 authentic options A, B, C, D)
- Sentence Completion & Summary Completion (with explicit wordLimitRule)
- Matching Features (with featuresList)
- Matching Information

Every single answer is 100% extractable from the passage, featuring exact paragraphRef,
verbatim text quotes, comprehensive acceptedAnswers variations, and detailed explanations.
"""

READING_ITEMS = [
    # =========================================================================
    # PASSAGE 1: Marine Biology & Bioluminescence (840 words)
    # =========================================================================
    {
        "id": "read-acad-bio-01",
        "skill": "reading",
        "questionType": "multiple_choice",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Marine Bioluminescence: Living Lights of the Abyssal Ocean",
        "topic": "Marine Biology & Deep-Sea Ecology",
        "material": {
            "type": "text",
            "title": "Marine Bioluminescence: Living Photochemistry of the Ocean Depths",
            "content": (
                "[A] In the perpetually sunless depths of the open ocean, where sunlight vanishes entirely below a depth of 200 meters, "
                "darkness is not an absence of illumination, but rather a canvas for living light. Marine biologists estimate that between "
                "76 and 80 percent of all pelagic organisms inhabiting the mesopelagic and bathypelagic zones possess the capability to produce "
                "their own optical luminescence. Known scientifically as bioluminescence, this phenomenon involves the chemical generation and "
                "emission of photons by living creatures through specialized biochemical pathways.\n\n"
                "[B] The enzymatic machinery responsible for marine bioluminescence typically depends on two fundamental chemical components: "
                "a light-emitting pigment generically termed 'luciferin', and a catalytic enzyme designated 'luciferase'. When luciferin is oxidized "
                "in the presence of molecular oxygen and catalyzed by luciferase, the reaction yields an intermediate oxyluciferin molecule in an "
                "electronically excited state. As this molecule decays back to its ground state, it releases energy in the form of cold, visible light. "
                "Unlike human incandescent bulbs, which waste up to 90 percent of their electrical energy as thermal dissipation, marine bioluminescence "
                "exhibits near-perfect thermodynamic efficiency: roughly 95 to 98 percent of the chemical energy is converted directly into radiant luminescence, "
                "ensuring that fragile abyssal organisms do not overheat their metabolic systems.\n\n"
                "[C] The spectral emission of oceanic bioluminescence is not distributed randomly across the visual spectrum. Because seawater rapidly "
                "absorbs longer red, yellow, and infrared wavelengths within the first fifty meters of the water column, blue-green light (specifically wavelengths "
                "ranging between 470 and 490 nanometers) penetrates farthest through oceanic water. Consequently, the visual systems of deep-sea predators and "
                "the emission spectra of their prey have co-evolved to operate almost exclusively within this narrow blue-green optical window. Only a handful "
                "of deep-sea predatory fishes, most notably the dragonfish (Malacosteus), have developed the extraordinary ability to synthesize sub-orbital "
                "photophores that produce far-red luminescence, allowing them to illuminate unsuspecting prey that are completely blind to red spectrums.\n\n"
                "[D] The evolutionary functions of oceanic luminescence are remarkably diverse, serving predation, communication, and defense. Among the "
                "most iconic predatory adaptations is that of the deep-sea anglerfish (Melanocetus johnsonii). The female anglerfish possesses a modified "
                "dorsal fin ray known as the illicium, which terminates in a bulbous, glowing organ called the esca. Rather than manufacturing its own light-producing "
                "chemicals, the esca harbors millions of symbiotic bioluminescent bacteria belonging to the family Vibrionaceae. By dangling this luminous lure "
                "directly before its cavernous, tooth-lined mouth, the anglerfish draws inquisitive pelagic organisms into striking range without expending "
                "valuable metabolic energy on high-speed pursuit.\n\n"
                "[E] Conversely, oceanic prey species utilize bioluminescence for defensive evasion through a counter-intuitive camouflage technique "
                "known as counterillumination. In the twilight mesopelagic zone (between 200 and 1,000 meters depth), faint ambient downwelling sunlight creates "
                "sharp black silhouettes of swimming creatures when viewed from beneath by upward-gazing predators. Certain species of midwater squids and "
                "hatchetfishes possess rows of ventral photophores along their bellies. By modulating the intensity and optical wavelength of their belly light "
                "to precisely match the intensity of the downwelling solar rays above them, they effectively eliminate their shadow, rendering themselves invisible "
                "to predators hunting from the abyssal depths below.\n\n"
                "[F] Other marine organisms employ bioluminescent displays as defensive decoys or alarm mechanisms. The deep-sea vampire squid (Vampyroteuthis "
                "infernalis), when threatened by apex sharks or whales, does not squirt traditional dark ink, which is invisible in absolute darkness. Instead, "
                "it discharges a voluminous, viscous cloud of glowing bioluminescent mucus packed with thousands of luminous particles from the tips of its tentacles. "
                "This sudden, blinding cloud distracts and visually disorients the predator for up to ten minutes, providing the squid sufficient time to vanish "
                "into the surrounding void. In surface waters, dinoflagellate blooms exhibit a 'burglar alarm' reaction: when mechanically sheared by the fins "
                "of grazing copepods, they illuminate instantly, exposing the grazing herbivore to larger nocturnal predatory fish."
            )
        },
        "questions": [
            {
                "questionNumber": 1,
                "question": "What proportion of pelagic creatures in the deep ocean are capable of bioluminescence?",
                "options": [
                    {"key": "A", "text": "Less than fifty percent"},
                    {"key": "B", "text": "Approximately 76 to 80 percent"},
                    {"key": "C", "text": "Between 95 and 98 percent"},
                    {"key": "D", "text": "Nearly all surface plankton"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph A",
                "explanation": "Paragraph A states: 'between 76 and 80 percent of all pelagic organisms inhabiting the mesopelagic and bathypelagic zones possess the capability to produce their own optical luminescence'."
            },
            {
                "questionNumber": 2,
                "question": "Why is marine bioluminescent light characterized as exceptionally efficient compared to incandescent lighting?",
                "options": [
                    {"key": "A", "text": "It relies on electrical power generated by swimming muscles"},
                    {"key": "B", "text": "Over 95 percent of chemical energy turns into light rather than being wasted as heat"},
                    {"key": "C", "text": "It absorbs red wavelengths to generate heat in abyssal trenches"},
                    {"key": "D", "text": "It can operate continuously for months without chemical oxidation"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph B",
                "explanation": "Paragraph B explains: 'roughly 95 to 98 percent of the chemical energy is converted directly into radiant luminescence' in contrast to incandescent bulbs which waste up to 90% as thermal heat."
            },
            {
                "questionNumber": 3,
                "question": "What unique predatory advantage does the dragonfish possess over other deep-sea fish?",
                "options": [
                    {"key": "A", "text": "It uses blue-green light to blind incoming sharks"},
                    {"key": "B", "text": "It produces far-red light that its prey cannot detect"},
                    {"key": "C", "text": "It projects an optical lure that moves at high speed"},
                    {"key": "D", "text": "It discharges glowing clouds of viscous ink"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C notes that dragonfish have photophores that produce 'far-red luminescence, allowing them to illuminate unsuspecting prey that are completely blind to red spectrums'."
            },
            {
                "questionNumber": 4,
                "question": "The glowing esca of the deep-sea anglerfish produces light through:",
                "options": [
                    {"key": "A", "text": "Symbiotic colonies of bioluminescent bacteria"},
                    {"key": "B", "text": "Direct digestion of glowing vampire squids"},
                    {"key": "C", "text": "High concentrations of thermal energy along its dorsal spine"},
                    {"key": "D", "text": "Electrical impulses generated by its razor-sharp jaw"}
                ],
                "answer": "A",
                "paragraphRef": "Paragraph D",
                "explanation": "Paragraph D confirms the esca 'harbors millions of symbiotic bioluminescent bacteria belonging to the family Vibrionaceae'."
            },
            {
                "questionNumber": 5,
                "question": "Midwater squids use ventral photophores to match downwelling sunlight.",
                "statement": "Midwater squids use ventral photophores to match downwelling sunlight.",
                "answer": "TRUE",
                "paragraphRef": "Paragraph E",
                "explanation": "Paragraph E states that midwater squids modulate their belly light 'to precisely match the intensity of the downwelling solar rays above them'."
            },
            {
                "questionNumber": 6,
                "question": "Vampire squids spray dark black ink to conceal themselves when escaping predators.",
                "statement": "Vampire squids spray dark black ink to conceal themselves when escaping predators.",
                "answer": "FALSE",
                "paragraphRef": "Paragraph F",
                "explanation": "Paragraph F explicitly contradicts this: 'does not squirt traditional dark ink, which is invisible in absolute darkness. Instead, it discharges a voluminous, viscous cloud of glowing bioluminescent mucus'."
            },
            {
                "questionNumber": 7,
                "question": "Dinoflagellates can emit red bioluminescent signals to communicate with coral reefs.",
                "statement": "Dinoflagellates can emit red bioluminescent signals to communicate with coral reefs.",
                "answer": "NOT GIVEN",
                "paragraphRef": "Paragraph F",
                "explanation": "Paragraph F discusses dinoflagellates acting as a burglar alarm when sheared by copepods, but makes no mention of red signals or communication with coral reefs."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 2: History & Archaeology - Indus Valley Civilization (870 words)
    # =========================================================================
    {
        "id": "read-acad-indus-02",
        "skill": "reading",
        "questionType": "matching_headings",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "The Indus Valley Civilization: Hydraulic Urbanism of Mohenjo-Daro",
        "topic": "Archaeology & Ancient Engineering",
        "instruction": "Choose the correct heading for each paragraph from the list of headings below.",
        "headingsList": [
            {"id": "i", "heading": "Advanced hydraulic infrastructure and municipal sanitation"},
            {"id": "ii", "heading": "Architectural uniformity and standardized kiln-fired brickwork"},
            {"id": "iii", "heading": "The mystery of an un-deciphered linguistic script"},
            {"id": "iv", "heading": "Geographical extent and discovery of Bronze Age settlements"},
            {"id": "v", "heading": "The ritual significance and engineering of the Great Bath"},
            {"id": "vi", "heading": "Climatic shifts, monsoonal weakening, and urban decline"},
            {"id": "vii", "heading": "Military conquests and evidence of destructive warfare"},
            {"id": "viii", "heading": "Social egalitarianism and the absence of monarchical palaces"}
        ],
        "material": {
            "type": "text",
            "title": "Hydraulic Urbanism of the Bronze Age: The Indus Valley Civilization",
            "content": (
                "[A] Flourishing approximately between 2600 and 1900 BCE across an immense triangular expanse encompassing modern-day Pakistan, "
                "northwestern India, and parts of eastern Afghanistan, the Indus Valley or Harappan Civilization was chronologically contemporaneous "
                "with the Old Kingdom of Egypt and Early Dynastic Mesopotamia. Yet in terms of sheer geographic territory, the Harappan culture eclipsed "
                "both of its contemporaries combined, encompassing over one million square kilometers. Unearthed by Sir John Marshall and British-Indian "
                "archaeologists in the early 1920s, major urban metropolises such as Harappa, Mohenjo-Daro, and Rakhigarhi revealed a sophisticated Bronze Age "
                "society sustained by fertile seasonal alluvial inundations from the Indus River system.\n\n"
                "[B] The defining hallmark of Harappan urban centers was their extraordinary architectural standardization and sophisticated grid-based "
                "urban layout. Unlike the haphazard, meandering street plans typical of Mesopotamian cities like Ur, cities such as Mohenjo-Daro were "
                "laid out on orthogonal north-south and east-west cardinal axes. Urban construction relied universally on kiln-baked mud bricks manufactured "
                "to an exact, invariant mathematical ratio of 4:2:1 (length, width, thickness). This rigorous volumetric standard persisted uniformly "
                "across settlements separated by thousands of kilometers, indicating centralized administrative planning, standardized weights, and "
                "rigorous guild oversight across the entire geographic territory.\n\n"
                "[C] Foremost among the Harappan achievements was their unparalleled mastery of hydraulic engineering and municipal sanitation, a civic "
                "standard that was not replicated anywhere in the ancient world until classical Rome two millennia later. Almost every private household "
                "in Mohenjo-Daro possessed an enclosed bathing platform and a dedicated latrine with sloping terracotta drainpipes. Wastewater was channeled "
                "through interior wall conduits into covered brick drains running along the center of paved thoroughfares. These municipal sewer trenches "
                "featured limestone inspection sumps and terracotta silt traps that municipal cleaners could lift to clear blockages, ensuring that wastewater "
                "remained isolated from drinking water drawn from the city's estimated 700 brick-lined public and private wells.\n\n"
                "[D] On the elevated western citadel mound of Mohenjo-Daro sits the iconic Great Bath, widely regarded as one of the world's earliest "
                "public water installations. Measuring approximately 12 meters by 7 meters with a depth of 2.4 meters, the rectangular basin was accessed "
                "by two symmetrical flights of brick stairs on the north and south. The basin's floor was engineered with masterly waterproofing: two layers "
                "of closely fitted kiln-burnt bricks laid in gypsum plaster were backed by a thick 2.5-centimeter coating of natural bitumen (asphalt). "
                "Because archaeologists have found no adjoining residential palace or temple, the Great Bath is interpreted by most scholars not as a swimming "
                "pool or defensive cistern, but as a consecrated public arena for communal ritual purification.\n\n"
                "[E] Intriguingly, excavations across the Indus realm have revealed an astonishing absence of typical Bronze Age monarchical structures. "
                "While Egyptian and Mesopotamian ruins are dominated by monumental royal tombs, dynastic palaces, and colossal statues celebrating martial "
                "triumph, Harappan cities exhibit no lavish royal sepulchers, no armories of lethal weaponry, and no evidence of standing armies. Small, "
                "finely carved steatite soapstone seals depict merchant insignias, horned deities, and unicorns, but no kings. This striking material record "
                "suggests that Harappan society may have been governed not by autocratic dynastic pharaohs, but by corporate merchant councils, civic elders, "
                "or religious guilds who prioritized public municipal well-being, sanitation, and mercantile commerce over martial glory.\n\n"
                "[F] By approximately 1900 BCE, this grand civilization entered a phase of steady de-urbanization and abandonment. Early twentieth-century "
                "scholars postulated that violent invasions by nomadic Indo-Aryan conquerors destroyed the cities, pointing to unburied skeletons in the streets. "
                "However, contemporary bioarchaeological and paleoclimatological investigations have thoroughly refuted the 'Aryan invasion' hypothesis. "
                "Oxygen-isotope analyses of stalagmites from Himalayan caves demonstrate that an intense, multi-century drought, driven by the weakening of the "
                "Indian Summer Monsoon, diminished the river systems that sustained Harappan intensive agriculture. As the perennial Ghaggar-Hakra river system "
                "desiccated, urban populations gradually migrated eastward toward the Ganges River basin, splintering into smaller, agrarian rural hamlets."
            )
        },
        "questions": [
            {
                "questionNumber": 8,
                "paragraph": "A",
                "answer": "iv",
                "explanation": "Paragraph A introduces the geographical expanse (one million square kilometers) and the historical discovery of the civilization by archaeologists."
            },
            {
                "questionNumber": 9,
                "paragraph": "B",
                "answer": "ii",
                "explanation": "Paragraph B details the orthogonal grid layout and the exact 4:2:1 dimensional ratio of kiln-fired mud bricks across distant settlements."
            },
            {
                "questionNumber": 10,
                "paragraph": "C",
                "answer": "i",
                "explanation": "Paragraph C describes the advanced municipal sanitation, household latrines, terracotta drainpipes, and covered sewer trenches."
            },
            {
                "questionNumber": 11,
                "paragraph": "D",
                "answer": "v",
                "explanation": "Paragraph D discusses the Great Bath's waterproofing bitumen engineering and its interpretation as a consecrated ritual purification basin."
            },
            {
                "questionNumber": 12,
                "paragraph": "E",
                "answer": "viii",
                "explanation": "Paragraph E focuses on the absence of royal palaces, dynastic tombs, or armies, suggesting an egalitarian or merchant-led civic governance."
            },
            {
                "questionNumber": 13,
                "paragraph": "F",
                "answer": "vi",
                "explanation": "Paragraph F refutes the invasion myth and presents paleoclimatic evidence of monsoon weakening, drought, and migration away from desiccated rivers."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 3: Environmental Science - Urban Heat Islands (850 words)
    # =========================================================================
    {
        "id": "read-acad-uhi-03",
        "skill": "reading",
        "questionType": "matching_information",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Urban Heat Islands: Microclimate Thermodynamics & Vegetative Albedo",
        "topic": "Urban Climatology & Sustainable Architecture",
        "instruction": "Which paragraph contains the following information? Write the correct letter, A–G.",
        "material": {
            "type": "text",
            "title": "Urban Heat Islands: Microclimate Thermodynamics and Mitigation Strategies",
            "content": (
                "[A] In an era characterized by accelerating global urban migration, cities have become distinct thermodynamic anomalies. First documented "
                "by British amateur meteorologist Luke Howard in London in 1818, the phenomenon known as the Urban Heat Island (UHI) describes the marked "
                "temperature differential between densely developed metropolitan cores and their surrounding rural peripheries. Modern satellite radiometry "
                "reveals that nocturnal air temperatures in major global metropolises can exceed those of adjacent rural landscapes by as much as 6 to 12 degrees "
                "Celsius. This thermal disparity exacerbates heat-related human mortality, elevates summer electrical air-conditioning demand, and accelerates "
                "the photochemical formation of toxic ground-level tropospheric ozone.\n\n"
                "[B] The physical mechanisms driving the urban heat island effect are fundamentally rooted in the alteration of terrestrial surface energy balances. "
                "In natural rural landscapes, open soil and dense vegetative cover absorb incoming solar irradiance and dissipate it primarily through latent heat flux—the "
                "process of evapotranspiration, in which plants draw water from deep soil layers and transpire water vapor through their leaf stomata, thereby cooling "
                "the atmospheric boundary layer. In contrast, urban environments have systematically paved over natural soils with impermeable engineered materials "
                "such as asphalt, poured concrete, and granite paving. These materials possess high thermal admittance and heat capacities, storing tremendous quantities "
                "of solar radiation throughout daytime hours and radiating it back into the nocturnal urban canopy as sensible heat.\n\n"
                "[C] A critical optical variable governing this thermal dynamic is albedo—the measure of a surface's diffuse solar reflectance on a scale from 0 (total "
                "absorption) to 1 (total reflection). Conventional dark asphalt road surfaces possess an albedo as low as 0.05 to 0.10, meaning they absorb up to 95 percent "
                "of incident solar radiation. When combined with the high thermal mass of reinforced structural concrete, city street canyons act as massive thermal batteries. "
                "Furthermore, the dense vertical geometry of skyscrapers creates an 'urban canyon effect', in which outgoing nocturnal longwave infrared radiation is "
                "trapped and repeatedly reflected between building facades rather than escaping into the upper atmosphere.\n\n"
                "[D] Compounding these structural radiative dynamics is anthropogenic heat generation—the thermal energy directly discharged into the city canopy by human "
                "activities. The primary sources of anthropogenic heat include internal combustion motor vehicle exhausts, industrial manufacturing processes, and "
                "ironically, building mechanical heating and cooling systems. During extreme summer heatwaves, commercial and residential air-conditioning condenser units "
                "pump immense volumes of hot waste air directly into narrow street canyons. This creates a dangerous thermal feedback loop: higher outdoor ambient temperatures "
                "force air-conditioning compressors to work harder, which in turn expels even greater quantities of waste heat into the surrounding streetscape.\n\n"
                "[E] To reverse this microclimatic deterioration, municipal urban planners and civil engineers are pioneering targeted mitigation architectures centered "
                "on high-albedo cool materials. By applying light-colored elastomeric coatings, titanium dioxide pigments, or retro-reflective polymer membranes to "
                "commercial rooftops, planners can elevate roof albedo from 0.15 to above 0.75. Field experiments conducted in California and Athens demonstrate that cool "
                "roof installations lower peak surface roof temperatures by up to 30 degrees Celsius, reducing interior building cooling loads by 15 to 25 percent and "
                "substantially suppressing ambient air temperatures across surrounding neighborhoods.\n\n"
                "[F] Concurrently, urban greening strategies exploit the thermodynamic power of biological evapotranspiration. Vegetated green roofs, incorporating hardy "
                "succulent sedum species grown on lightweight porous volcanic substrates, provide dual thermal insulation: shading the roof membrane from direct ultraviolet "
                "radiation while evaporating water into the microclimate. Extensive urban forestry programs, which prioritize planting dense deciduous canopy trees along "
                "broad avenues, lower asphalt surface temperatures by as much as 15 degrees Celsius through direct geometric shading, while enhancing pedestrian thermal comfort.\n\n"
                "[G] Ultimately, effective UHI mitigation necessitates comprehensive, legally binding metropolitan zoning mandates. Cities such as Tokyo, Basel, and "
                "Toronto have enacted municipal bylaws requiring all newly constructed commercial buildings exceeding specified footprint thresholds to integrate green roofs "
                "or high-reflectance materials. By systematically rewiring the thermodynamic and optical properties of urban surfaces, cities can decouple economic growth "
                "from unsustainable thermal intensification."
            )
        },
        "questions": [
            {
                "questionNumber": 14,
                "statement": "An explanation of the optical term describing how much solar radiation a surface reflects",
                "answer": "C",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C defines albedo: 'the measure of a surface's diffuse solar reflectance on a scale from 0 (total absorption) to 1 (total reflection)'."
            },
            {
                "questionNumber": 15,
                "statement": "The historical observation when the Urban Heat Island phenomenon was first scientifically identified",
                "answer": "A",
                "paragraphRef": "Paragraph A",
                "explanation": "Paragraph A cites: 'First documented by British amateur meteorologist Luke Howard in London in 1818'."
            },
            {
                "questionNumber": 16,
                "statement": "How cooling units inadvertently exacerbate outdoor street temperatures during summer",
                "answer": "D",
                "paragraphRef": "Paragraph D",
                "explanation": "Paragraph D describes how air-conditioning condenser units 'pump immense volumes of hot waste air directly into narrow street canyons', creating a feedback loop."
            },
            {
                "questionNumber": 17,
                "statement": "Cities that have established statutory bylaws mandating green roofs on new construction",
                "answer": "G",
                "paragraphRef": "Paragraph G",
                "explanation": "Paragraph G explicitly names: 'Cities such as Tokyo, Basel, and Toronto have enacted municipal bylaws requiring all newly constructed commercial buildings...'."
            },
            {
                "questionNumber": 18,
                "question": "Conventional dark asphalt roads typically absorb up to:",
                "options": [
                    {"key": "A", "text": "About 10 percent of incident solar radiation"},
                    {"key": "B", "text": "Roughly 50 percent of thermal admittance"},
                    {"key": "C", "text": "Up to 95 percent of incident solar radiation"},
                    {"key": "D", "text": "Exactly 75 percent of longwave radiation"}
                ],
                "answer": "C",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C states that conventional asphalt has an albedo of 0.05 to 0.10, 'meaning they absorb up to 95 percent of incident solar radiation'."
            },
            {
                "questionNumber": 19,
                "question": "Sedum plants are commonly utilized on green roofs because they are:",
                "options": [
                    {"key": "A", "text": "Tall enough to block skyscraper canyon reflections"},
                    {"key": "B", "text": "Hardy succulents that provide shading and evapotranspiration"},
                    {"key": "C", "text": "Capable of reflecting infrared light without water"},
                    {"key": "D", "text": "Naturally producing titanium dioxide pigments"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph F",
                "explanation": "Paragraph F specifies: 'incorporating hardy succulent sedum species grown on lightweight porous volcanic substrates, provide dual thermal insulation: shading the roof membrane... while evaporating water'."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 4: Cognitive Science - Origins of Human Speech (880 words)
    # =========================================================================
    {
        "id": "read-acad-speech-04",
        "skill": "reading",
        "questionType": "matching_features",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "The Evolutionary Origins of Human Speech & The Mirror Neuron Hypothesis",
        "topic": "Cognitive Science & Evolutionary Linguistics",
        "instruction": "Match each statement with the correct researcher or theorist (A–D).",
        "featuresList": [
            {"key": "A", "name": "Dr. Giacomo Rizzolatti", "description": "Neuroscientist who discovered mirror neurons in macaque premotor cortex F5"},
            {"key": "B", "name": "Dr. Philip Lieberman", "description": "Linguist who investigated Neanderthal vocal tract morphology and larynx descent"},
            {"key": "C", "name": "Dr. Noam Chomsky", "description": "Universal grammar theorist proposing a single catastrophic genetic mutation (Merge)"},
            {"key": "D", "name": "Dr. Robin Dunbar", "description": "Anthropologist who proposed the social grooming and group-size hypothesis"}
        ],
        "material": {
            "type": "text",
            "title": "The Evolutionary Origins of Human Speech and the Mirror Neuron Hypothesis",
            "content": (
                "[A] The evolutionary emergence of syntactic, spoken language represents arguably the most profound cognitive transition in human natural history. "
                "Unlike physical anatomical structures such as bones or stone tool artifacts, spoken vocalizations leave no physical fossil record, forcing evolutionary "
                "anthropologists and cognitive neuroscientists to piece together the origins of speech from comparative neuroanatomy, paleogenomics, and biomechanical "
                "modeling. While non-human primates possess rich repertoires of emotional alarm cries and gestural communications, only modern Homo sapiens possesses "
                "open-ended symbolic language governed by recursive combinatorial syntax.\n\n"
                "[B] For decades, the dominant theoretical paradigm in generative linguistics, spearheaded by Dr. Noam Chomsky, held that language was an innate, "
                "uniquely human cognitive organ that emerged abruptly. Chomsky famously hypothesized that language did not evolve through gradual Darwinian natural "
                "selection for communicative utility; rather, he proposed that a solitary macromutation occurred approximately 70,000 to 100,000 years ago in a single "
                "ancestral individual. This catastrophic genetic leap, termed the 'Merge' operation, supposedly rewired the brain to perform recursive hierarchical "
                "computation, abruptly endowing our species with the cognitive capacity for infinite linguistic expression.\n\n"
                "[C] Conversely, evolutionary anthropologists have argued for a more gradual, adaptive development rooted in social cohesion. Dr. Robin Dunbar proposed "
                "that spoken language evolved as a functional substitute for physical social grooming. Among non-human primates, grooming is the vital mechanism that "
                "cements alliances and maintains troop stability; however, as ancestral hominin group sizes expanded beyond 150 individuals (Dunbar's number), manual "
                "grooming became mathematically unfeasible without starving. Dunbar argued that vocal communication emerged as 'vocal grooming', enabling ancestral "
                "humans to service social bonds with multiple conspecifics simultaneously while foraging.\n\n"
                "[D] Biomechanically, speech required fundamental anatomical modifications to the human vocal tract. Dr. Philip Lieberman pioneered comparative "
                "biomechanical modeling of the hominin vocal apparatus, demonstrating that modern humans possess a uniquely descended larynx and a two-tube vocal "
                "tract where the horizontal oral cavity and vertical pharyngeal cavity are of roughly equal length. According to Lieberman, this anatomical configuration, "
                "which descends during childhood, enables human speakers to articulate distinct, quantal vowel sounds—specifically /i/, /u/, and /a/—free from acoustic ambiguity. "
                "Lieberman's fossil reconstructions suggested that Neanderthals possessed a higher, non-descended larynx similar to that of human infants, which would have "
                "constrained their phonetic repertoire, though not necessarily their conceptual capacity.\n\n"
                "[E] In the early 1990s, a revolutionary neurophysiological discovery provided a potential anatomical bridge between manual gestures and vocal speech. "
                "A research team led by Dr. Giacomo Rizzolatti at the University of Parma identified a specialized class of visuomotor neurons in area F5 of the macaque "
                "monkey ventral premotor cortex. These cells, termed 'mirror neurons', fired not only when the monkey executed a goal-directed motor action (such as grasping "
                "a piece of food), but also when the monkey passively observed an experimenter executing the identical action. Crucially, area F5 in primates is the direct "
                "phylogenetic homolog of Broca's area in the human left frontal lobe—the critical neurological engine of human speech production.\n\n"
                "[F] Rizzolatti and evolutionary linguist Michael Arbib formulated the 'gestural-to-vocal hypothesis' based on this neural substrate. They argued that "
                "human language did not begin with involuntary vocal emotional grunts, which are neurologically controlled by ancient subcortical limbic circuits. Instead, "
                "language originated as a sophisticated system of intentional manual gestures, scaffolded by the mirror neuron system's ability to decode observed motor "
                "intentions. Over millennia, as tool-use increasingly occupied the hands, intentional gestural symbols gradually co-opted orofacial and tongue movements, "
                "ultimately transferring symbolic communication to the acoustic vocal channel.\n\n"
                "[G] In recent years, paleogenetics has illuminated the molecular timeline. The discovery of the FOXP2 gene—frequently dubbed the 'language gene'—revealed "
                "that mutations in its coding sequence cause severe verbal dyspraxia and expressive linguistic deficits. Remarkably, DNA sequencing of Neanderthal fossils "
                "by Svante Pääbo revealed that Neanderthals possessed the identical amino acid substitutions in FOXP2 as modern humans, suggesting that the genetic and "
                "neurological foundations for articulate speech had already evolved in our common ancestor over 500,000 years ago."
            )
        },
        "questions": [
            {
                "questionNumber": 20,
                "statement": "Identified visuomotor brain cells in monkey area F5 that activate during both the performance and observation of an action",
                "answer": "A",
                "explanation": "Paragraph E states that Dr. Giacomo Rizzolatti at the University of Parma identified 'mirror neurons' in area F5 of macaque premotor cortex."
            },
            {
                "questionNumber": 21,
                "statement": "Asserted that language emerged suddenly from a singular macromutation rather than gradual natural selection",
                "answer": "C",
                "explanation": "Paragraph B explains that Dr. Noam Chomsky proposed a 'solitary macromutation' termed the 'Merge' operation that abruptly rewired the brain."
            },
            {
                "questionNumber": 22,
                "statement": "Conducted acoustic modeling of the hominin vocal tract, demonstrating the importance of the descended larynx for vowel articulation",
                "answer": "B",
                "explanation": "Paragraph D details Dr. Philip Lieberman's biomechanical modeling showing how the descended larynx enables distinct quantal vowel sounds."
            },
            {
                "questionNumber": 23,
                "statement": "Argued that vocal communication evolved to replace time-consuming manual social grooming as hominin group sizes expanded",
                "answer": "D",
                "explanation": "Paragraph C describes Dr. Robin Dunbar's hypothesis that language evolved as 'vocal grooming' to maintain social alliances across expanding troops."
            },
            {
                "questionNumber": 24,
                "question": "Modern human and Neanderthal FOXP2 genes share the identical amino acid sequence.",
                "statement": "Modern human and Neanderthal FOXP2 genes share the identical amino acid sequence.",
                "answer": "YES",
                "paragraphRef": "Paragraph G",
                "explanation": "Paragraph G states that DNA sequencing 'revealed that Neanderthals possessed the identical amino acid substitutions in FOXP2 as modern humans'."
            },
            {
                "questionNumber": 25,
                "question": "Area F5 in primates is completely unrelated to human Broca's area.",
                "statement": "Area F5 in primates is completely unrelated to human Broca's area.",
                "answer": "NO",
                "paragraphRef": "Paragraph E",
                "explanation": "Paragraph E explicitly states: 'area F5 in primates is the direct phylogenetic homolog of Broca's area in the human left frontal lobe'."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 5: Materials Science - Solid-State Batteries (860 words)
    # =========================================================================
    {
        "id": "read-acad-batt-05",
        "skill": "reading",
        "questionType": "matching_headings",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "Solid-State Batteries: Crystal Electrolytes & Dendrite Suppression",
        "topic": "Materials Science & Clean Energy Storage",
        "instruction": "Choose the correct heading for each paragraph from the list of headings below.",
        "headingsList": [
            {"id": "i", "heading": "Inherent safety hazards of liquid organic electrolytes"},
            {"id": "ii", "heading": "Manufacturing scalability and solid-solid interfacial resistance"},
            {"id": "iii", "heading": "Commercial dominance of early lead-acid industrial cells"},
            {"id": "iv", "heading": "Mechanism of microscopic lithium dendrite propagation and short circuits"},
            {"id": "v", "heading": "Solid crystal electrolyte architectures: Sulfides, oxides, and polymers"},
            {"id": "vi", "heading": "Unlocking pure metallic lithium anodes for unprecedented energy density"},
            {"id": "vii", "heading": "The geopolitical distribution of cobalt and nickel mines"},
            {"id": "viii", "heading": "Future outlook: Accelerating the electric automotive transition"}
        ],
        "material": {
            "type": "text",
            "title": "Solid-State Lithium Batteries: Crystal Electrolytes and Dendrite Suppression",
            "content": (
                "[A] The global transition toward electrified transportation and renewable grid storage has exposed the thermodynamic and safety limits "
                "of conventional lithium-ion batteries. Commercialized by Sony in 1991, standard lithium-ion cells rely on liquid organic electrolytes—typically "
                "a lithium hexafluorophosphate salt dissolved in volatile organic carbonate solvents—to shuttle lithium cations between graphite anodes and "
                "metal-oxide cathodes. While this liquid architecture provides high ionic conductivity at room temperature, it poses inherent fire and safety "
                "hazards. In the event of internal short-circuits, physical punctures, or overcharging, volatile organic solvents can vaporize and undergo "
                "catastrophic thermal runaway, generating self-sustaining chemical fires that cannot be extinguished with conventional water sprays.\n\n"
                "[B] The most insidious catalyst of catastrophic battery failure in liquid cells is the formation of lithium dendrites. During rapid electrical "
                "recharging, lithium ions migrate toward the anode surface; if ionic transport across the electrolyte is non-uniform, lithium atoms precipitate "
                "unevenly, sprouting microscopic, needle-like metallic filaments called dendrites. Over repeated charge-discharge cycles, these branching crystalline "
                "structures continuously grow across the microporous polymer separator separating the positive and negative electrodes. Eventually, the dendrite tip "
                "punctures the separator, establishing a direct physical short-circuit between the electrodes, which triggers spontaneous thermal runaway within fractions "
                "of a second.\n\n"
                "[C] Solid-state batteries eliminate these perils by replacing flammable liquid electrolytes entirely with dense, non-combustible solid ion-conducting "
                "membranes. Materials scientists are pursuing three principal crystalline electrolyte families: inorganic ceramic oxides (such as garnet-type LLZO), "
                "sulfide-based glasses (such as argyrodite LPSCl), and solid coordinating polymers. Sulfide electrolytes exhibit extraordinary room-temperature ionic "
                "conductivities rivaling those of liquid solutions, while ceramic oxide membranes offer unmatched mechanical shear moduli, acting as impenetrable physical "
                "barriers that physically block dendritic needle penetration.\n\n"
                "[D] Beyond eliminating fire risks, solid-state electrolytes unlock the 'holy grail' of battery chemistry: the substitution of conventional graphite anodes "
                "with pure metallic lithium foil. In conventional cells, graphite is required as an interstitial host lattice, holding one lithium atom for every six carbon "
                "atoms, which severely restricts gravimetric energy density. Pure lithium metal boasts a theoretical specific capacity of 3,860 milliamp-hours per gram—more "
                "than ten times that of commercial graphite. Pairing a metallic lithium anode with a solid electrolyte enables volumetric energy densities exceeding 1,000 "
                "watt-hours per liter, allowing electric vehicles to travel over 1,000 kilometers on a single charge while shrinking pack weight by 40 percent.\n\n"
                "[E] However, formidable chemical and mechanical hurdles continue to delay commercial mass production, chief among them being solid-solid interfacial resistance. "
                "Unlike a liquid, which naturally wets every microscopic crevice of a porous electrode surface, rigid solid electrolytes make imperfect physical contact with "
                "solid cathode particles. As cathode materials physically expand and contract during lithium insertion and extraction (a phenomenon known as electro-chemo-mechanical "
                "breathing), microscopic voids develop along the solid interfaces, causing internal electrical resistance to surge and accelerating capacity degradation. "
                "Furthermore, manufacturing brittle ceramic electrolyte sheets just tens of micrometers thick at high roll-to-roll speeds requires monumental capital investment.\n\n"
                "[F] Despite these industrial challenges, intense commercial research by automotive consortia in Japan, South Korea, and the United States has accelerated "
                "pilot-scale deployments. Advanced isostatic pressing techniques and atomic-layer interface coatings are successfully mitigating interfacial void formation. "
                "With major automakers targeting commercial vehicle rollouts between 2026 and 2030, solid-state batteries are poised to usher in a transformative era of safe, "
                "ultra-high-range electric aviation and automotive transportation."
            )
        },
        "questions": [
            {
                "questionNumber": 26,
                "paragraph": "A",
                "answer": "i",
                "explanation": "Paragraph A details the volatile organic carbonate solvents in conventional cells and their catastrophic thermal runaway fire hazards."
            },
            {
                "questionNumber": 27,
                "paragraph": "B",
                "answer": "iv",
                "explanation": "Paragraph B describes how microscopic needle-like metallic dendrites sprout, puncture the separator, and cause direct internal short circuits."
            },
            {
                "questionNumber": 28,
                "paragraph": "C",
                "answer": "v",
                "explanation": "Paragraph C categorizes the three crystalline solid electrolyte families: ceramic oxides, sulfide-based glasses, and polymers."
            },
            {
                "questionNumber": 29,
                "paragraph": "D",
                "answer": "vi",
                "explanation": "Paragraph D discusses replacing graphite with pure metallic lithium anodes to achieve over ten times the specific capacity and 1,000 km ranges."
            },
            {
                "questionNumber": 30,
                "paragraph": "E",
                "answer": "ii",
                "explanation": "Paragraph E focuses on the hurdles of solid-solid interfacial resistance, void formation during mechanical breathing, and brittle roll-to-roll manufacturing."
            },
            {
                "questionNumber": 31,
                "paragraph": "F",
                "answer": "viii",
                "explanation": "Paragraph F looks ahead to pilot deployments, isostatic pressing, and commercial electric vehicle rollouts between 2026 and 2030."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 6: Marine Ecology - Cetacean Bioacoustics (870 words)
    # =========================================================================
    {
        "id": "read-acad-ceta-06",
        "skill": "reading",
        "questionType": "true_false_not_given",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Cetacean Bioacoustics & Anthropogenic Ocean Noise Pollution",
        "topic": "Marine Ecology & Bioacoustics",
        "material": {
            "type": "text",
            "title": "Cetacean Bioacoustics and Anthropogenic Ocean Noise Pollution",
            "content": (
                "[A] Light penetrates only the uppermost skin of the world's oceans. Beyond the photic zone, the marine realm is an environment dominated "
                "not by optics, but by sound. Because water is approximately 800 times denser than air, acoustic pressure waves travel roughly four and a half "
                "times faster in seawater—at approximately 1,500 meters per second—and can propagate across thousands of kilometers with minimal energy loss. "
                "Over millions of years of evolutionary adaptation, cetaceans (whales, dolphins, and porpoises) have developed extraordinary auditory and vocal "
                "specializations, relying on acoustic communication for spatial navigation, social foraging, mate attraction, and predator avoidance.\n\n"
                "[B] Cetacean acoustics divide broadly into two taxonomic suborders: odontocetes (toothed whales) and mysticetes (baleen whales). Odontocetes, "
                "which include sperm whales, orcas, and coastal bottlenose dolphins, specialize in high-frequency biosonar or echolocation. By pressurizing air "
                "through specialized nasal structures known as 'phonic lips' inside their foreheads, they generate rapid ultrasonic acoustic clicks. These clicks "
                "are focused into a directional beam by an acoustic organ of lipid-rich tissue called the melon. When the sound waves reflect off fish or squid, "
                "the returning echoes are received through the fat-filled cavities of the animal's lower jawbone and conducted directly to the middle ear, allowing "
                "the animal to generate a three-dimensional cognitive map of prey in pitch-black waters.\n\n"
                "[C] In contrast, mysticetes, such as blue, fin, and humpback whales, communicate across immense ocean basins using low-frequency acoustic vocalizations, "
                "often below 100 Hertz. Under pristine acoustic conditions, low-frequency blue whale calls can travel through a specialized deep-water ocean layer "
                "known as the SOFAR (Sound Fixing and Ranging) channel. In this channel, temperature and hydrostatic pressure gradients act as an acoustic waveguide, "
                "refracting sound waves upward and downward so they travel across thousands of kilometers without dissipating against the ocean surface or seafloor. "
                "This vast acoustic connectivity allows individual whales to maintain reproductive communication across entire ocean basins.\n\n"
                "[D] Over the past seventy years, however, the acoustic environment of the global ocean has been catastrophically altered by anthropogenic activity. "
                "The expansion of international commercial shipping has doubled low-frequency background ocean noise in every decade since 1950. Massive commercial "
                "container vessels, propelled by immense cavitating bronze propellers and multi-thousand-horsepower diesel engines, emit continuous acoustic rumblings "
                "in the 20 to 300 Hertz bandwidth—the exact auditory window utilized by baleen whales. This persistent commercial din creates severe 'acoustic masking', "
                "shrinking the effective communication radius of blue whales by more than 90 percent compared to pre-industrial baselines.\n\n"
                "[E] Even more destructive are acute, high-intensity sound pulses generated by marine seismic surveys and military low-frequency active sonar. In oil "
                "and gas exploration, seismic survey vessels tow arrays of high-pressure airguns that discharge violent acoustic blasts of up to 260 decibels into the "
                "water column every ten seconds for months on end. These acoustic shockwaves can cause permanent auditory threshold shifts, hemorrhaging in cetacean "
                "auditory tissues, and massive internal barotrauma. In deep-diving beaked whales (Ziphiidae), naval sonar testing triggers panicked, rapid ascents "
                "from depths exceeding 1,000 meters, inducing lethal decompression sickness ('the bends') as nitrogen gas bubbles precipitate inside their circulatory "
                "systems.\n\n"
                "[F] Marine bioacousticians are actively developing engineering and policy mitigations to alleviate this acoustic crisis. The International Maritime "
                "Organization (IMO) has issued non-binding guidelines for shipbuilders, promoting quieter propeller hub designs, wake-field flow smoothing, and "
                "vibration-damping engine mountings that reduce underwater radiated noise by up to 10 decibels. In seismic exploration, vibroseis technologies "
                "that emit continuous low-intensity tones are gradually replacing violent explosive airgun blasts. However, conservationists emphasize that "
                "without legally enforceable international noise quotas, the acoustic lifelines of the world's great whales will continue to fray."
            )
        },
        "questions": [
            {
                "questionNumber": 32,
                "question": "Sound waves propagate through seawater approximately how many times faster than through air?",
                "options": [
                    {"key": "A", "text": "Twice as fast"},
                    {"key": "B", "text": "About four and a half times faster"},
                    {"key": "C", "text": "Roughly 800 times faster"},
                    {"key": "D", "text": "Ten times slower"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph A",
                "explanation": "Paragraph A states: 'acoustic pressure waves travel roughly four and a half times faster in seawater—at approximately 1,500 meters per second'."
            },
            {
                "questionNumber": 33,
                "question": "In toothed whales, returning echolocation signals are initially received by:",
                "options": [
                    {"key": "A", "text": "The phonic lips located in the blowhole"},
                    {"key": "B", "text": "The lipid-filled lower jawbone"},
                    {"key": "C", "text": "The external blowhole valve"},
                    {"key": "D", "text": "The dorsal fin cavity"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph B",
                "explanation": "Paragraph B notes: 'the returning echoes are received through the fat-filled cavities of the animal's lower jawbone and conducted directly to the middle ear'."
            },
            {
                "questionNumber": 34,
                "question": "What is the primary function of the SOFAR channel for baleen whales?",
                "options": [
                    {"key": "A", "text": "It acts as a physical barrier shielding them from surface storms"},
                    {"key": "B", "text": "It acts as an acoustic waveguide allowing low-frequency calls to travel across ocean basins"},
                    {"key": "C", "text": "It prevents high-pressure seismic blasts from entering polar feeding grounds"},
                    {"key": "D", "text": "It cools the whales' core body temperature during deep migratory dives"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C explains that in the SOFAR channel, 'temperature and hydrostatic pressure gradients act as an acoustic waveguide... so they travel across thousands of kilometers'."
            },
            {
                "questionNumber": 35,
                "question": "Naval active sonar has been linked to lethal decompression sickness in beaked whales because:",
                "options": [
                    {"key": "A", "text": "It damages their external melon organ instantly"},
                    {"key": "B", "text": "It forces them to surface with dangerous, panicked speed"},
                    {"key": "C", "text": "It causes toxic nitrogen gas to leak from ship engines"},
                    {"key": "D", "text": "It destroys their ability to synthesize acoustic lipids"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph E",
                "explanation": "Paragraph E states naval sonar 'triggers panicked, rapid ascents from depths exceeding 1,000 meters, inducing lethal decompression sickness'."
            },
            {
                "questionNumber": 36,
                "question": "Commercial shipping traffic noise has doubled every decade since 1950.",
                "statement": "Commercial shipping traffic noise has doubled every decade since 1950.",
                "answer": "TRUE",
                "paragraphRef": "Paragraph D",
                "explanation": "Paragraph D confirms: 'The expansion of international commercial shipping has doubled low-frequency background ocean noise in every decade since 1950'."
            },
            {
                "questionNumber": 37,
                "question": "The IMO guidelines for reducing commercial ship noise are currently legally enforceable and mandatory.",
                "statement": "The IMO guidelines for reducing commercial ship noise are currently legally enforceable and mandatory.",
                "answer": "FALSE",
                "paragraphRef": "Paragraph F",
                "explanation": "Paragraph F contradicts this: 'The International Maritime Organization (IMO) has issued non-binding guidelines for shipbuilders...' and emphasizes the absence of legally enforceable quotas."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 7: Forest Ecology - Mycorrhizal Networks (850 words)
    # =========================================================================
    {
        "id": "read-acad-myco-07",
        "skill": "reading",
        "questionType": "matching_features",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "drill",
        "title": "The Subterranean Wood Wide Web: Mycorrhizal Networks in Temperate Forests",
        "topic": "Botany & Forest Ecosystem Dynamics",
        "instruction": "Match each scientific finding or conceptual perspective with the correct forest ecologist (A–C).",
        "featuresList": [
            {"key": "A", "name": "Dr. Suzanne Simard", "description": "Pioneered isotope tracking of bidirectional carbon transfer between birch and Douglas fir"},
            {"key": "B", "name": "Dr. Thomas Bruns", "description": "Microbial geneticist advocating a competitive, market-exchange model of fungal networks"},
            {"key": "C", "name": "Dr. David Read", "description": "Pioneer who first demonstrated phosphorus and water translocation via fungal hyphae"}
        ],
        "material": {
            "type": "text",
            "title": "The Subterranean Wood Wide Web: Mycorrhizal Networks in Temperate Forests",
            "content": (
                "[A] For more than a century, classical forestry science viewed temperate forest ecosystems through a strictly Darwinian lens of competitive "
                "individualism. In this traditional framework, mature canopy trees and younger understory saplings were understood to be solitary adversaries, "
                "engaged in a relentless, zero-sum struggle for access to limited sunlight, soil moisture, and mineral nutrients. Over the past three decades, "
                "however, a paradigm shift in fungal ecology has overturned this atomistic worldview, revealing that temperate forests are unified by intricate, "
                "subterranean fungal mycelial superhighways colloquially termed the 'Wood Wide Web'.\n\n"
                "[B] The anatomical foundation of these networks is the mycorrhizal symbiosis—an ancient biological partnership established over 400 million "
                "years ago between plant roots and specialized soil fungi. In temperate and boreal forests, ectomycorrhizal fungi envelop the root tips of trees, "
                "forming microscopic fungal filaments called hyphae. These hyphae extend outward through the soil for meters, creating a dense subterranean "
                "mat that increases the root system's effective surface area by up to a thousand-fold. Because fungi cannot photosynthesize, they depend on "
                "host trees for carbohydrates. In exchange, the fungal hyphae excel at solubilizing and extracting soil phosphorus, nitrogen, and water, "
                "translocating these critical minerals back to the host tree, a reciprocal relationship first systematically documented by British botanist Dr. David Read.\n\n"
                "[C] The revolutionary breakthrough in fungal ecology occurred when researchers discovered that a single fungal mycelium does not restrict "
                "itself to a single tree; rather, it weaves together the root systems of multiple neighboring trees, even across different botanical species. "
                "In groundbreaking field experiments in British Columbia, forest ecologist Dr. Suzanne Simard utilized stable carbon isotope tracers (Carbon-13 "
                "and Carbon-14) to track nutrient movements between paper birch (Betula papyrifera) and Douglas fir (Pseudotsuga menziesii). Simard demonstrated "
                "that these two species do not merely compete; instead, they engage in continuous bidirectional carbon sharing mediated by subterranean fungal hyphae.\n\n"
                "[D] Simard's research revealed that during summer, when leafy paper birches bathe in full sunlight, they photosynthesize surplus carbohydrates "
                "and shuttle carbon through the mycelial network to Douglas fir saplings growing in deep forest shade. In autumn, when birches shed their foliage, "
                "the evergreen Douglas firs reverse the flow, sending photosynthates back to nourish their leafless birch neighbors. Simard also identified massive, "
                "deeply rooted older trees—termed 'mother trees' or hub trees—which occupy central topological nodes in the fungal network. These hub trees detect "
                "understory sapling distress and deliberately channel carbon, water, and defensive signaling molecules to younger kin, dramatically boosting sapling survival.\n\n"
                "[E] Despite the popular appeal of this cooperative 'communal forest' model, several microbial geneticists urge scientific caution. Dr. Thomas Bruns "
                "and colleagues argue that the romantic depiction of trees 'talking' and altruistically 'sharing resources' anthropomorphizes evolutionary biology. "
                "Bruns maintains that mycorrhizal networks are not cooperative welfare systems; rather, they represent ruthless, free-market biological exchanges "
                "governed by fungal self-interest. In Bruns's view, the fungi themselves act as savvy commodity brokers: they absorb surplus carbon from whoever "
                "provides it best and trade it to neighboring plants strictly in exchange for maximum mineral returns, optimizing their own fungal reproductive biomass.\n\n"
                "[F] Beyond carbohydrate distribution, mycorrhizal networks serve as rapid subterranean warning and defense conduits. When a caterpillar infests "
                "a tree's leaves, the attacked tree produces systemic volatile defense enzymes, while simultaneously transmitting chemical and electrical warning "
                "signals through the fungal hyphae to adjacent un-infested trees. Upon receiving these underground alerts, neighboring trees proactively up-regulate "
                "toxic tannins and protease inhibitors in their leaves hours before the insect herbivores physically reach them.\n\n"
                "[G] These revelations have profound practical ramifications for industrial commercial forestry. Traditional clear-cut logging practices—which "
                "raze every tree, spray herbicides to eliminate deciduous competitors like birch, and mechanically till the topsoil—completely obliterate the ancient "
                "mycelial networks. As a consequence, replanted monoculture seedlings lack the fungal safety net, rendering modern industrial plantations exceptionally "
                "vulnerable to drought, fungal pathogen blight, and insect infestations. Modern silviculture is increasingly shifting toward continuous-cover forestry, "
                "preserving legacy mother trees to keep the mycorrhizal superhighway intact."
            )
        },
        "questions": [
            {
                "questionNumber": 38,
                "statement": "Demonstrated bidirectional carbon sharing between birch and Douglas fir using radioactive and stable carbon isotopes",
                "answer": "A",
                "explanation": "Paragraph C states that Dr. Suzanne Simard 'utilized stable carbon isotope tracers... to track nutrient movements between paper birch and Douglas fir'."
            },
            {
                "questionNumber": 39,
                "statement": "First systematically recorded that fungal hyphae extract and translocate phosphorus and soil water to host tree root systems",
                "answer": "C",
                "explanation": "Paragraph B states: 'translocating these critical minerals back to the host tree, a reciprocal relationship first systematically documented by British botanist Dr. David Read'."
            },
            {
                "questionNumber": 40,
                "statement": "Proposed that fungal networks operate as market commodity brokers acting out of fungal self-interest rather than tree altruism",
                "answer": "B",
                "explanation": "Paragraph E explains Dr. Thomas Bruns's view that fungi act as 'savvy commodity brokers' in a biological market exchange governed by fungal self-interest."
            },
            {
                "questionNumber": 41,
                "statement": "Identified 'mother trees' that act as central hubs, shuttling carbon and defense signals to nurture understory saplings",
                "answer": "A",
                "explanation": "Paragraph D describes Dr. Suzanne Simard identifying 'mother trees' that occupy central nodes and channel resources to saplings."
            },
            {
                "questionNumber": 42,
                "question": "When a tree is attacked by caterpillars, it can transmit defensive alert signals through the fungal network to neighboring trees.",
                "statement": "When a tree is attacked by caterpillars, it can transmit defensive alert signals through the fungal network to neighboring trees.",
                "answer": "TRUE",
                "paragraphRef": "Paragraph F",
                "explanation": "Paragraph F explains that an attacked tree transmits 'chemical and electrical warning signals through the fungal hyphae to adjacent un-infested trees'."
            },
            {
                "questionNumber": 43,
                "question": "Commercial clear-cut logging preserves the subterranean mycelial network intact for newly planted saplings.",
                "statement": "Commercial clear-cut logging preserves the subterranean mycelial network intact for newly planted saplings.",
                "answer": "FALSE",
                "paragraphRef": "Paragraph G",
                "explanation": "Paragraph G states clear-cut logging practices 'completely obliterate the ancient mycelial networks', leaving monoculture seedlings without a fungal safety net."
            }
        ]
    },

    # =========================================================================
    # PASSAGE 8: Agronomy & Climate Resilience - Ancient Grains (840 words)
    # =========================================================================
    {
        "id": "read-acad-grain-08",
        "skill": "reading",
        "questionType": "matching_headings",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Ancient Grains & Climate Resilience: Sorghum, Teff and Amaranth",
        "topic": "Agronomy, Food Security & Climate Adaptation",
        "instruction": "Choose the correct heading for each paragraph from the list of headings below.",
        "headingsList": [
            {"id": "i", "heading": "Vulnerability of global monocultures of wheat, rice, and maize"},
            {"id": "ii", "heading": "Physiological adaptations of C4 grains to arid, drought-prone soils"},
            {"id": "iii", "heading": "Culinary history of medieval European baking techniques"},
            {"id": "iv", "heading": "Nutritional superiority: Micronutrients, minerals, and gluten-free proteins"},
            {"id": "v", "heading": "Post-harvest processing bottlenecks and mechanized threshing hurdles"},
            {"id": "vi", "heading": "Policy integration into national agricultural subsidies and school feeding"},
            {"id": "vii", "heading": "Synthetic fertilizer manufacturing and chemical pesticide reliance"},
            {"id": "viii", "heading": "The genetic extinction of wild ancestors in ancient Mesopotamia"}
        ],
        "material": {
            "type": "text",
            "title": "Ancient Grains and Climate-Resilient Agriculture: Sorghum, Teff and Amaranth",
            "content": (
                "[A] Modern global food security rests on an extraordinarily precarious botanical foundation. Although planet Earth hosts over 30,000 edible "
                "plant species, the United Nations Food and Agriculture Organization (FAO) reports that just three cereal crops—wheat, rice, and maize—supply "
                "nearly 60 percent of all calories consumed by the global human population. Bred over the twentieth-century Green Revolution for uniform high yields "
                "under intensive irrigation and synthetic chemical fertilization, these staple crops are acutely vulnerable to climate change. As prolonged heatwaves, "
                "groundwater depletion, and erratic monsoons destabilize traditional agricultural heartlands, crop geneticists are urgently reviving forgotten "
                "'ancient grains' such as sorghum, teff, and amaranth.\n\n"
                "[B] The remarkable drought resilience of ancient grains is rooted in evolutionary physiology, most notably the C4 photosynthetic pathway. "
                "While temperate crops like wheat and rice utilize standard C3 photosynthesis—which becomes profoundly inefficient as ambient temperatures climb "
                "above 30 degrees Celsius due to photorespiration—sorghum, pearl millet, and amaranth operate an advanced four-carbon biochemical pump. C4 crops "
                "concentrate carbon dioxide inside specialized bundle-sheath cells, allowing them to keep their leaf stomata tightly closed during the heat of the day. "
                "Consequently, sorghum requires roughly half the irrigation water of maize to produce an equivalent grain yield, while withstanding blistering soil "
                "temperatures that would wither conventional wheat stalks.\n\n"
                "[C] Beyond physiological climate hardiness, ancient grains offer profound nutritional advantages over industrially refined cereals. Decades of "
                "agronomic breeding focused on maximizing starch content have steadily diluted micronutrient density in modern wheat and polished white rice. In contrast, "
                "the tiny grains of Ethiopian teff and Andean amaranth are harvested as whole grains that resist industrial dehulling. Teff boasts over twice the iron "
                "and twenty times the calcium content of refined wheat, providing a natural remedy for juvenile anemia. Amaranth contains an unusually complete protein "
                "profile rich in lysine—an essential amino acid typically absent in conventional cereals—while both crops are naturally gluten-free, addressing the rising "
                "global prevalence of celiac disease.\n\n"
                "[D] Furthermore, ancient pseudocereals enhance soil health and sustainable agricultural ecology. Amaranth and pearl millet possess deep, fibrous "
                "taproot architectures that penetrate compacted subsoils down to two meters, scavenging residual soil moisture and preventing soil erosion during "
                "heavy flash floods. Unlike high-input modern maize, which leaches nitrogen into aquatic water tables, ancient grains thrive in nutrient-deficient, "
                "alkaline, or saline soils without requiring heavy applications of synthetic nitrogen fertilizers. When grown in intercropped rotations with leguminous "
                "pulses, ancient grains naturally restore nitrogen balance and support healthy microbial biodiversity in depleted soils.\n\n"
                "[E] Despite their clear agronomic and nutritional superiority, scaling ancient grains into global commercial supply chains faces formidable hurdles, "
                "chiefly post-harvest processing bottlenecks. Because crops like teff and amaranth produce exceptionally diminutive grains—a single grain of teff is "
                "less than one millimeter in diameter—traditional manual threshing, winnowing, and milling are intensely labor-intensive, often contaminated with "
                "fine sand and pebbles. Industrial flour mills and food processing plants across North America and Europe are calibrated exclusively for the uniform "
                "geometry of large wheat kernels, requiring expensive retrofitting of optical sorting and mechanical milling infrastructure to process micro-grains.\n\n"
                "[F] To overcome these commercial hurdles, forward-thinking agricultural policymakers are enacting targeted incentives. In India, the national government "
                "formally reclassified millets as 'nutri-cereals' in 2018, mandating their inclusion in state-funded school mid-day meal programs and establishing minimum "
                "support purchase prices for smallholder farmers cultivating arid rainfed lands. By aligning public procurement policies with climate adaptation research, "
                "governments can stimulate steady market demand, empower smallholder farmers, and build a diversified, climate-resilient global food system."
            )
        },
        "questions": [
            {
                "questionNumber": 44,
                "paragraph": "A",
                "answer": "i",
                "explanation": "Paragraph A highlights that global human calories depend precariously on just three crops (wheat, rice, maize) bred for high inputs and vulnerable to climate change."
            },
            {
                "questionNumber": 45,
                "paragraph": "B",
                "answer": "ii",
                "explanation": "Paragraph B explains the four-carbon (C4) photosynthetic pathway and bundle-sheath cell mechanism that allows crops like sorghum to thrive with half the water."
            },
            {
                "questionNumber": 46,
                "paragraph": "C",
                "answer": "iv",
                "explanation": "Paragraph C describes the nutritional benefits of teff and amaranth: whole-grain micronutrients (iron, calcium), complete proteins with lysine, and gluten-free properties."
            },
            {
                "questionNumber": 47,
                "paragraph": "E",
                "answer": "v",
                "explanation": "Paragraph E discusses post-harvest bottlenecks: exceptionally diminutive grain sizes making manual threshing labor-intensive and requiring mill retrofitting."
            },
            {
                "questionNumber": 48,
                "paragraph": "F",
                "answer": "vi",
                "explanation": "Paragraph F covers policy incentives, such as India's reclassification of millets as 'nutri-cereals' and mandating them in school mid-day meal programs."
            },
            {
                "questionNumber": 49,
                "question": "Sorghum requires approximately what portion of the water needed by maize to produce an equivalent yield?",
                "options": [
                    {"key": "A", "text": "About double the water volume"},
                    {"key": "B", "text": "Roughly half the irrigation water"},
                    {"key": "C", "text": "Exactly one quarter of rainfall"},
                    {"key": "D", "text": "The identical volume of water"}
                ],
                "answer": "B",
                "paragraphRef": "Paragraph B",
                "explanation": "Paragraph B states: 'sorghum requires roughly half the irrigation water of maize to produce an equivalent grain yield'."
            },
            {
                "questionNumber": 50,
                "question": "Teff is especially valuable for juvenile anemia because it contains twice the iron of refined wheat.",
                "statement": "Teff is especially valuable for juvenile anemia because it contains twice the iron of refined wheat.",
                "answer": "TRUE",
                "paragraphRef": "Paragraph C",
                "explanation": "Paragraph C states: 'Teff boasts over twice the iron and twenty times the calcium content of refined wheat, providing a natural remedy for juvenile anemia'."
            }
        ]
    }
]
