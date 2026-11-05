"""
Authentic IELTS Listening Dataset Specification
Contains 8 comprehensive Listening Sections across all 4 IELTS test formats:
- Test 1 (Questions 1–40):
  * Section 1: International Student Homestay & Accommodation Booking (Q1–Q10)
  * Section 2: Orientation Tour of the National Botanical Conservatory & Seed Vault (Q11–Q20)
  * Section 3: Environmental Science Research Project on Estuary Microplastics (Q21–Q30)
  * Section 4: University Lecture on Biomimetic Aerodynamics (Q31–Q40)
- Test 2 (Questions 1–40):
  * Section 1: Riverdale Community Sports Club Membership Registration (Q1–Q10)
  * Section 2: Greenfield Heritage River Walk & Community Volunteering (Q11–Q20)
  * Section 3: Architecture Seminar on Roman vs Byzantine Arch Construction (Q21–Q30)
  * Section 4: University Lecture on Maritime Silk Road & Spice Currency (Q31–Q40)

Total: 80 Authentic Listening Questions with real Edge-TTS multi-speaker audio scripts.
"""

LISTENING_SECTIONS = [
    # =========================================================================
    # TEST 1 - SECTION 1: Student Homestay Booking (Questions 1–10)
    # =========================================================================
    {
        "id": "list-sec1-home-01",
        "audioFilename": "section1_homestay_booking.mp3",
        "skill": "listening",
        "questionType": "form_completion",
        "difficulty": "easy",
        "band": "Band 5.5–6.5",
        "granularity": "section",
        "title": "Listening Section 1: International Student Homestay & Accommodation Booking",
        "topic": "Student Accommodation & Domestic Inquiries",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-SoniaNeural", "Mrs. Henderson", "Good morning. Overseas Student Accommodation Office, Mrs. Henderson speaking. How can I help you today?"),
            ("en-GB-RyanNeural", "Kenji Tanaka", "Good morning. My name is Kenji Tanaka. I'm arriving next month to begin my postgraduate engineering degree, and I'd like to arrange homestay accommodation with a local family."),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "Welcome to the university, Kenji! Let me open up our homestay registration form. Could I take your student identification number first, please?"),
            ("en-GB-RyanNeural", "Kenji Tanaka", "Yes, of course. It is capital E-N-G, followed by 9-0-4-2-7."),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "Got it: ENG-9-0-4-2-7. And what style of room are you looking for? We have single standard, shared twin, or single with a private balcony."),
            ("en-GB-RyanNeural", "Kenji Tanaka", "I'd really prefer a single room with a balcony if one is available, so I have good natural ventilation for studying."),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "A single room with a balcony. Yes, we have a match near the campus. Now, do you have any specific dietary requirements or food allergies we need to notify the host family about?"),
            ("en-GB-RyanNeural", "Kenji Tanaka", "I am strictly vegetarian, so no meat or seafood at all, please. Dairy and eggs are completely fine."),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "Strictly vegetarian, noted. And what is your expected date of arrival in the country?"),
            ("en-GB-RyanNeural", "Kenji Tanaka", "My flight arrives at Heathrow on the 18th of September in the early evening."),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "The 18th of September. Excellent. The host family assigned to your profile is Mrs. Miller, that is M-I-L-L-E-R."),
            ("en-GB-RyanNeural", "Kenji Tanaka", "Mrs. Miller, wonderful. What is their home address?"),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "Their residence is at 42 Oakfield Road. That's O-A-K-F-I-E-L-D Road."),
            ("en-GB-RyanNeural", "Kenji Tanaka", "42 Oakfield Road. And how long does it take to travel to the university engineering campus from there?"),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "It's exceptionally convenient: just 15 minutes by direct city bus. The number 14 bus stops right across the street."),
            ("en-GB-RyanNeural", "Kenji Tanaka", "Fifteen minutes by bus is fantastic. Does the family have any house rules I should be aware of?"),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "Yes, they maintain a strictly non-smoking household both indoors and throughout the garden. Also, could I take down your UK mobile contact number?"),
            ("en-GB-RyanNeural", "Kenji Tanaka", "Certainly, it is 07700 900412."),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "07700 900412. Lastly, to finalize and secure your placement, a refundable security deposit of 250 pounds is required today."),
            ("en-GB-RyanNeural", "Kenji Tanaka", "Two hundred and fifty pounds. I can transfer that by debit card immediately. Thank you so much, Mrs. Henderson!"),
            ("en-GB-SoniaNeural", "Mrs. Henderson", "You're very welcome, Kenji. I'll email you the formal confirmation shortly. Goodbye!")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec1-home-01",
                "type": "form_completion",
                "title": "Questions 1–10",
                "instruction": "Complete the form below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 1,
                        "prefix": "Student ID Number: ",
                        "answer": "ENG 90427",
                        "acceptedAnswers": ["ENG90427", "ENG 90427", "eng90427", "ENG-90427"],
                        "targetTurn": 3,
                        "explanation": "Kenji states his student ID is 'ENG 90427'."
                    },
                    {
                        "questionNumber": 2,
                        "prefix": "Requested Room Style: Single room with a ",
                        "answer": "balcony",
                        "acceptedAnswers": ["balcony", "private balcony"],
                        "targetTurn": 5,
                        "explanation": "Kenji specifies: 'I\'d really prefer a single room with a balcony'."
                    },
                    {
                        "questionNumber": 3,
                        "prefix": "Dietary Requirement: Strictly ",
                        "answer": "vegetarian",
                        "acceptedAnswers": ["vegetarian", "Vegetarian"],
                        "targetTurn": 7,
                        "explanation": "Kenji confirms: 'I am strictly vegetarian, so no meat or seafood at all'."
                    },
                    {
                        "questionNumber": 4,
                        "prefix": "Arrival Date: ",
                        "answer": "18th September",
                        "acceptedAnswers": ["18th September", "18 September", "September 18", "September 18th", "18th of September"],
                        "targetTurn": 9,
                        "explanation": "Kenji states his flight arrives on 'the 18th of September'."
                    },
                    {
                        "questionNumber": 5,
                        "prefix": "Host Family Surname: Mrs. ",
                        "answer": "Miller",
                        "acceptedAnswers": ["Miller", "miller"],
                        "targetTurn": 10,
                        "explanation": "Mrs. Henderson confirms the host family is 'Mrs. Miller, that is M-I-L-L-E-R'."
                    },
                    {
                        "questionNumber": 6,
                        "prefix": "Address: 42 ",
                        "suffix": " Road",
                        "answer": "Oakfield",
                        "acceptedAnswers": ["Oakfield", "oakfield"],
                        "targetTurn": 12,
                        "explanation": "Mrs. Henderson states: 'Their residence is at 42 Oakfield Road'."
                    },
                    {
                        "questionNumber": 7,
                        "prefix": "Commute time to campus by bus: ",
                        "suffix": " minutes",
                        "answer": "15",
                        "acceptedAnswers": ["15", "fifteen", "15 minutes"],
                        "targetTurn": 14,
                        "explanation": "Mrs. Henderson notes it is 'just 15 minutes by direct city bus'."
                    },
                    {
                        "questionNumber": 8,
                        "prefix": "Household Environment: strictly ",
                        "answer": "non-smoking",
                        "acceptedAnswers": ["non-smoking", "nonsmoking", "non smoking"],
                        "targetTurn": 16,
                        "explanation": "Mrs. Henderson confirms: 'they maintain a strictly non-smoking household'."
                    },
                    {
                        "questionNumber": 9,
                        "prefix": "Student Contact Phone: ",
                        "answer": "07700 900412",
                        "acceptedAnswers": ["07700 900412", "07700900412"],
                        "targetTurn": 17,
                        "explanation": "Kenji states his UK contact number is '07700 900412'."
                    },
                    {
                        "questionNumber": 10,
                        "prefix": "Refundable Security Deposit: £",
                        "answer": "250",
                        "acceptedAnswers": ["250", "250 pounds", "two hundred and fifty"],
                        "targetTurn": 18,
                        "explanation": "Mrs. Henderson confirms: 'a refundable security deposit of 250 pounds is required today'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 1 - SECTION 2: Botanical Conservatory & Seed Vault (Questions 11–20)
    # =========================================================================
    {
        "id": "list-sec2-map-03",
        "audioFilename": "section2_botanical_conservatory.mp3",
        "skill": "listening",
        "questionType": "plan_map_diagram_labelling",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "section",
        "title": "Listening Section 2: Orientation Tour of the National Botanical Conservatory & Seed Vault",
        "topic": "Public Facilities & Botanical Conservation",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "material": {
            "type": "image",
            "title": "Map of the National Botanical Conservatory Grounds",
            "imageDescription": (
                "Architectural layout map of the National Botanical Conservatory. "
                "Visitors enter through the South Main Gate. Facing north along the central pedestrian boulevard: "
                "To the immediate northwest (Point A) is the glass domed Orchid Pavilion. "
                "Directly to the north at the far end of the central walkway (Point B) is the soaring Tropical Rainforest Biome. "
                "To the northeast on high rocky ground (Point C) lies the Alpine Rockery. "
                "Underneath the northern complex down a flight of spiral stairs (Point D) is the subterranean Seed Vault Archive. "
                "To the southeast near the entrance gate (Point E) is the Visitors Cafe and Bookshop."
            ),
            "imageUrl": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 400' width='100%' height='260'><rect width='600' height='400' fill='%23f1f5f9'/><rect x='20' y='20' width='560' height='360' rx='12' fill='%23ffffff' stroke='%23cbd5e1' stroke-width='2'/><text x='300' y='45' text-anchor='middle' font-family='sans-serif' font-size='16' font-weight='bold' fill='%230f172a'>National Botanical Conservatory Grounds</text><circle cx='120' cy='120' r='45' fill='%23dcfce7' stroke='%2316a34a' stroke-width='2'/><text x='120' y='125' text-anchor='middle' font-family='sans-serif' font-size='18' font-weight='bold' fill='%23166534'>A</text><rect x='220' y='80' width='160' height='80' rx='8' fill='%23dbeafe' stroke='%232563eb' stroke-width='2'/><text x='300' y='125' text-anchor='middle' font-family='sans-serif' font-size='18' font-weight='bold' fill='%231e40af'>B</text><circle cx='480' cy='120' r='45' fill='%23fef3c7' stroke='%23d97706' stroke-width='2'/><text x='480' y='125' text-anchor='middle' font-family='sans-serif' font-size='18' font-weight='bold' fill='%2392400e'>C</text><rect x='240' y='200' width='120' height='60' rx='8' fill='%23f3e8ff' stroke='%239333ea' stroke-width='2'/><text x='300' y='235' text-anchor='middle' font-family='sans-serif' font-size='18' font-weight='bold' fill='%236b21a8'>D</text><rect x='440' y='260' width='110' height='70' rx='8' fill='%23fee2e2' stroke='%23dc2626' stroke-width='2'/><text x='495' y='300' text-anchor='middle' font-family='sans-serif' font-size='18' font-weight='bold' fill='%23991b1b'>E</text><path d='M300 370 L300 270' stroke='%2364748b' stroke-width='6' stroke-dasharray='8 4'/><rect x='250' y='345' width='100' height='35' rx='6' fill='%23334155'/><text x='300' y='368' text-anchor='middle' font-family='sans-serif' font-size='12' font-weight='bold' fill='%23ffffff'>South Entrance</text></svg>"
        },
        "turns": [
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Good morning and a very warm welcome to the National Botanical Conservatory and International Seed Bank. My name is Dr. Evelyn Vance, and as Director of Botanical Research, I am delighted to guide you through our historic conservation facility today."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Before we begin our walking tour, please refer to the visitor site plan in your tour brochures. We are currently standing at the South Entrance Gate, looking straight north up the main pedestrian avenue."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "If you look across to your left toward the northwest, marked with the letter A on your map, you will see our famous Victorian glass dome. This is the Orchid Pavilion, housing over 2,500 species of rare tropical epiphytes."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Continuing straight ahead along the central boulevard to the very northern terminus of the path, marked B, stands our largest glasshouse structure: the Tropical Rainforest Biome, featuring an 80-foot high canopy skywalk and authentic indoor waterfall."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Now, if you turn toward the northeast on the elevated terrace marked C, you will find our outdoor Alpine Rockery. Here, specialized cold-climate flora from the Himalayas and Andes thrive on limestone crevices."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Beneath the central complex, accessed via a spiral staircase down to area D, lies our state-of-the-art Subterranean Seed Vault Archive, where over one million indigenous wild seeds are preserved in cryo-storage at minus 20 degrees Celsius."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Finally, returning toward the entrance on your right-hand side in the southeast corner, labeled E, you will find the Botanical Cafe and Heritage Bookshop, where organic herbal teas and botanical reference guides are available."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Our guided walking tour will depart from the Orchid Pavilion in five minutes. Before we set off, please remember that flash photography is strictly prohibited inside all glasshouses, as intense light bursts disrupt photosensitive research specimens."),
            ("en-GB-SoniaNeural", "Dr. Evelyn Vance", "Lastly, students presenting a valid university identification card at the gift shop receive a generous 20 percent discount on all botanical publications and seeds. Please feel free to ask questions as we proceed!")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec2-map-03-p1",
                "type": "plan_map_diagram_labelling",
                "title": "Questions 11–15",
                "instruction": "Label the map below. Write the correct letter, A–E, next to Questions 11–15.",
                "questions": [
                    {
                        "questionNumber": 11,
                        "labelLocation": "Orchid Pavilion",
                        "answer": "A",
                        "targetTurn": 2,
                        "explanation": "Dr. Vance notes: 'to your left toward the northwest, marked with the letter A on your map... is the Orchid Pavilion'."
                    },
                    {
                        "questionNumber": 12,
                        "labelLocation": "Tropical Rainforest Biome",
                        "answer": "B",
                        "targetTurn": 3,
                        "explanation": "Dr. Vance states: 'straight ahead along the central boulevard to the very northern terminus... marked B, stands our largest glasshouse structure: the Tropical Rainforest Biome'."
                    },
                    {
                        "questionNumber": 13,
                        "labelLocation": "Alpine Rockery",
                        "answer": "C",
                        "targetTurn": 4,
                        "explanation": "Dr. Vance explains: 'toward the northeast on the elevated terrace marked C, you will find our outdoor Alpine Rockery'."
                    },
                    {
                        "questionNumber": 14,
                        "labelLocation": "Subterranean Seed Vault Archive",
                        "answer": "D",
                        "targetTurn": 5,
                        "explanation": "Dr. Vance notes: 'accessed via a spiral staircase down to area D, lies our state-of-the-art Subterranean Seed Vault Archive'."
                    },
                    {
                        "questionNumber": 15,
                        "labelLocation": "Botanical Cafe and Bookshop",
                        "answer": "E",
                        "targetTurn": 6,
                        "explanation": "Dr. Vance mentions: 'on your right-hand side in the southeast corner, labeled E, you will find the Botanical Cafe and Heritage Bookshop'."
                    }
                ]
            },
            {
                "id": "group-list-sec2-map-03-p2",
                "type": "note_completion",
                "title": "Questions 16–20",
                "instruction": "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 16,
                        "prefix": "The Orchid Pavilion houses more than ",
                        "suffix": " rare epiphyte species.",
                        "answer": "2,500",
                        "acceptedAnswers": ["2,500", "2500", "2500 species", "over 2500"],
                        "targetTurn": 2,
                        "explanation": "Dr. Vance specifies the pavilion houses 'over 2,500 species of rare tropical epiphytes'."
                    },
                    {
                        "questionNumber": 17,
                        "prefix": "Wild seeds in the subterranean vault are stored at ",
                        "suffix": " degrees Celsius.",
                        "answer": "minus 20",
                        "acceptedAnswers": ["minus 20", "-20", "minus twenty"],
                        "targetTurn": 5,
                        "explanation": "Dr. Vance confirms seeds are preserved 'in cryo-storage at minus 20 degrees Celsius'."
                    },
                    {
                        "questionNumber": 18,
                        "prefix": "The guided walking tour will depart in ",
                        "suffix": " minutes.",
                        "answer": "5",
                        "acceptedAnswers": ["5", "five"],
                        "targetTurn": 7,
                        "explanation": "Dr. Vance says: 'Our guided walking tour will depart from the Orchid Pavilion in five minutes'."
                    },
                    {
                        "questionNumber": 19,
                        "prefix": "Visitors are strictly forbidden from using ",
                        "suffix": " inside the glasshouses.",
                        "answer": "flash photography",
                        "acceptedAnswers": ["flash photography", "flash"],
                        "targetTurn": 7,
                        "explanation": "Dr. Vance announces: 'flash photography is strictly prohibited inside all glasshouses'."
                    },
                    {
                        "questionNumber": 20,
                        "prefix": "Students with valid ID receive a ",
                        "suffix": " percent discount at the gift shop.",
                        "answer": "20",
                        "acceptedAnswers": ["20", "twenty", "20%"],
                        "targetTurn": 8,
                        "explanation": "Dr. Vance confirms students 'receive a generous 20 percent discount'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 1 - SECTION 3: Estuary Microplastics Research (Questions 21–30)
    # =========================================================================
    {
        "id": "list-sec3-micro-05",
        "audioFilename": "section3_microplastic_research.mp3",
        "skill": "listening",
        "questionType": "multiple_choice",
        "difficulty": "advanced",
        "band": "Band 7.0–8.0",
        "granularity": "section",
        "title": "Listening Section 3: Environmental Science Research Project on Estuary Microplastics",
        "topic": "Academic Research Methodology & Estuarine Ecology",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-SoniaNeural", "Emma", "Dr. Jenkins, thanks so much for meeting with Liam and me today. We wanted to get your feedback on our joint field dissertation proposal."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "Of course, Emma. I've read your preliminary abstract on quantifying microplastic contamination in the Thames estuary sediment layers. It's a very timely research topic."),
            ("en-GB-RyanNeural", "Liam", "Thanks, Dr. Jenkins. We're planning to collect core sediment samples from six designated tidal zones between Greenwich and Southend-on-Sea."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "Good. But what specific density separation methodology are you planning to employ to isolate microplastic synthetic polymers from heavy mineral sediment?"),
            ("en-GB-SoniaNeural", "Emma", "We evaluated both sodium chloride and zinc chloride solutions. Although sodium chloride is much cheaper, its lower solution density of 1.2 grams per cubic centimeter fails to float dense plastics like PET and PVC. So we decided to use saturated zinc chloride with a density of 1.6 to ensure total particle recovery."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "That's an excellent technical decision, Emma. Zinc chloride will definitely prevent false negatives for heavy polymers. And what statistical software package will you use to execute the multi-factor analysis of variance on your sample clusters?"),
            ("en-GB-RyanNeural", "Liam", "We initially considered using standard Excel spreadsheets, but our departmental tutor advised us that R programming language or SPSS would provide far more robust ANOVA regression models. So Liam will be running the statistical modeling in R."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "Very sensible. And during laboratory filtration, what membrane filter pore diameter will you utilize?"),
            ("en-GB-SoniaNeural", "Emma", "We have ordered glass micro-fiber filter papers with a 0.45 micron pore size, which will reliably retain all fibrous and spherical particles down to sub-micrometer scales."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "Perfect. Now, when processing the raw cores, how deeply will you section them for depth stratification?"),
            ("en-GB-RyanNeural", "Liam", "We will slice each sediment core every 2 centimeters in the cold room, and then treat each slice with 30 percent hydrogen peroxide to chemically digest organic detritus before density flotation."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "Excellent protocol. And before heading onto the tidal mudflats next Monday, ensure you have both signed your mandatory risk assessment form. Lastly, how have you split the responsibilities for your final presentation in November?"),
            ("en-GB-SoniaNeural", "Emma", "I will deliver the literature review, sampling site rationale, and laboratory methodology. Liam will present the statistical data visualizations, ecological risk indices, and policy recommendations."),
            ("en-GB-ThomasNeural", "Dr. Jenkins", "That sounds like a fair, well-balanced division of labor. Best of luck in the field!")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec3-micro-05-p1",
                "type": "multiple_choice",
                "title": "Questions 21–25",
                "instruction": "Choose the correct letter, A, B, C or D.",
                "questions": [
                    {
                        "questionNumber": 21,
                        "question": "Why did the students choose saturated zinc chloride over sodium chloride for density separation?",
                        "options": [
                            {"key": "A", "text": "Zinc chloride is significantly less expensive than common salt"},
                            {"key": "B", "text": "Its higher density allows heavy plastics like PET and PVC to float"},
                            {"key": "C", "text": "It eliminates the need for laboratory chemical fume hoods"},
                            {"key": "D", "text": "It permanently dyes the microplastic fibers for microscopy"}
                        ],
                        "answer": "B",
                        "targetTurn": 4,
                        "explanation": "Emma explains that zinc chloride's higher density of 1.6 g/cm³ floats heavy polymers like PET and PVC that fail to float in salt solution."
                    },
                    {
                        "questionNumber": 22,
                        "question": "Which software will the students use to execute their multi-factor ANOVA statistical analysis?",
                        "options": [
                            {"key": "A", "text": "Microsoft Excel spreadsheets"},
                            {"key": "B", "text": "R statistical programming language"},
                            {"key": "C", "text": "Python Pandas library"},
                            {"key": "D", "text": "Manual hand calculations"}
                        ],
                        "answer": "B",
                        "targetTurn": 6,
                        "explanation": "Liam confirms: 'Liam will be running the statistical modeling in R'."
                    },
                    {
                        "questionNumber": 23,
                        "question": "What filter membrane pore size did the students order for particle recovery?",
                        "options": [
                            {"key": "A", "text": "5.0 microns"},
                            {"key": "B", "text": "0.45 microns"},
                            {"key": "C", "text": "1.2 millimeters"},
                            {"key": "D", "text": "100 nanometers"}
                        ],
                        "answer": "B",
                        "targetTurn": 8,
                        "explanation": "Emma specifies: 'glass micro-fiber filter papers with a 0.45 micron pore size'."
                    },
                    {
                        "questionNumber": 24,
                        "question": "What chemical reagent will be used to digest natural organic matter in the samples?",
                        "options": [
                            {"key": "A", "text": "Hydrochloric acid"},
                            {"key": "B", "text": "Hydrogen peroxide"},
                            {"key": "C", "text": "Ethanol alcohol"},
                            {"key": "D", "text": "Sodium hydroxide"}
                        ],
                        "answer": "B",
                        "targetTurn": 10,
                        "explanation": "Liam notes they will treat each slice with '30 percent hydrogen peroxide to chemically digest organic detritus'."
                    },
                    {
                        "questionNumber": 25,
                        "question": "During the final presentation, what will Liam specifically be responsible for presenting?",
                        "options": [
                            {"key": "A", "text": "The literature review and laboratory sampling methodology"},
                            {"key": "B", "text": "The historical background of the Thames estuary"},
                            {"key": "C", "text": "The statistical visualizations, risk indices, and policy recommendations"},
                            {"key": "D", "text": "The field safety risk assessment procedures"}
                        ],
                        "answer": "C",
                        "targetTurn": 12,
                        "explanation": "Emma states: 'Liam will present the statistical data visualizations, ecological risk indices, and policy recommendations'."
                    }
                ]
            },
            {
                "id": "group-list-sec3-micro-05-p2",
                "type": "sentence_completion",
                "title": "Questions 26–30",
                "instruction": "Complete the sentences below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 26,
                        "prefix": "Total number of designated tidal sampling zones: ",
                        "answer": "6",
                        "acceptedAnswers": ["6", "six"],
                        "targetTurn": 2,
                        "explanation": "Liam states: 'We\'re planning to collect core sediment samples from six designated tidal zones'."
                    },
                    {
                        "questionNumber": 27,
                        "prefix": "Sampling sites stretch along the Thames from Greenwich to ",
                        "answer": "Southend-on-Sea",
                        "acceptedAnswers": ["Southend-on-Sea", "Southend", "southend on sea"],
                        "targetTurn": 2,
                        "explanation": "Liam confirms sampling between 'Greenwich and Southend-on-Sea'."
                    },
                    {
                        "questionNumber": 28,
                        "prefix": "Sediment cores will be sliced every ",
                        "suffix": " in the cold room.",
                        "answer": "2 centimeters",
                        "acceptedAnswers": ["2 centimeters", "2 cm", "two centimeters"],
                        "targetTurn": 10,
                        "explanation": "Liam states: 'We will slice each sediment core every 2 centimeters in the cold room'."
                    },
                    {
                        "questionNumber": 29,
                        "prefix": "Before field work, students must sign a mandatory ",
                        "suffix": " form.",
                        "answer": "risk assessment",
                        "acceptedAnswers": ["risk assessment"],
                        "targetTurn": 11,
                        "explanation": "Dr. Jenkins emphasizes: 'ensure you have both signed your mandatory risk assessment form'."
                    },
                    {
                        "questionNumber": 30,
                        "prefix": "The final dissertation defense presentation will occur in the month of ",
                        "answer": "November",
                        "acceptedAnswers": ["November", "november"],
                        "targetTurn": 11,
                        "explanation": "Dr. Jenkins asks about their 'final presentation in November'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 1 - SECTION 4: Biomimetic Aerodynamics Lecture (Questions 31–40)
    # =========================================================================
    {
        "id": "list-sec4-biom-07",
        "audioFilename": "section4_biomimetic_aerodynamics.mp3",
        "skill": "listening",
        "questionType": "note_completion",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "section",
        "title": "Listening Section 4: University Lecture on Biomimetic Aerodynamics",
        "topic": "Aerospace Engineering & Biomimicry",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-ThomasNeural", "Prof. Finch", "Good morning, ladies and gentlemen. Today's lecture in our Advanced Fluid Dynamics series explores biomimetic aerodynamics—specifically, how evolutionary adaptations in predatory fauna are inspiring quieter, more energy-efficient aerospace and renewable energy systems."),
            ("en-GB-ThomasNeural", "Prof. Finch", "Our first biological case study focuses on the fast-swimming shortfin mako shark. For decades, naval architects assumed that hydrodynamic drag reduction required microscopically smooth hull surfaces. However, examination of shark skin under electron microscopy reveals that it is covered in millions of microscopic tooth-like scales called dermal denticles."),
            ("en-GB-ThomasNeural", "Prof. Finch", "These denticles feature longitudinal micro-grooves or 'riblets' aligned parallel to the flow of fluid. These riblets lift turbulent vortices away from the skin surface, preventing high-energy vortices from dissipating energy against the skin. Aeronautical engineers applying synthetic riblet films to commercial passenger aircraft wings have achieved up to an 8 percent reduction in aerodynamic parasitic drag."),
            ("en-GB-ThomasNeural", "Prof. Finch", "Our second case study examines the silent flight mechanisms of nocturnal barn owls, scientifically known as Tyto alba. While birds such as pigeons generate distinct acoustic flapping sounds, hunting owls can fly virtually undetected by small rodents. Acoustic analysis reveals three distinct plumage adaptations."),
            ("en-GB-ThomasNeural", "Prof. Finch", "First, the leading edge of the owl's primary flight feathers possesses a stiff, comb-like serration. This physical comb breaks up laminar airflow into micro-turbulence, preventing large acoustic sound waves from forming."),
            ("en-GB-ThomasNeural", "Prof. Finch", "Second, the trailing edge of the wing feathers terminates in a soft, flexible fringe, which smoothly mixes airflows and suppresses aerodynamic turbulence shedding."),
            ("en-GB-ThomasNeural", "Prof. Finch", "Wind turbine manufacturers are currently retrofitting massive offshore turbine blades with owl-inspired trailing edge serrations. Field trials indicate this biomimetic geometry reduces aerodynamic blade noise by approximately 3 decibels, allowing wind farms to operate closer to residential communities while generating up to 2 percent more electrical power."),
            ("en-GB-ThomasNeural", "Prof. Finch", "In next week's seminar, we will examine how humpback whale flipper tubercles enhance stall resistance on aerodynamic airfoils. Thank you for your attention.")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec4-biom-07",
                "type": "note_completion",
                "title": "Questions 31–40",
                "instruction": "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 31,
                        "prefix": "The lecture series is part of the university course in Advanced ",
                        "answer": "Fluid Dynamics",
                        "acceptedAnswers": ["Fluid Dynamics", "fluid dynamics"],
                        "targetTurn": 0,
                        "explanation": "Prof. Finch announces: 'Today\'s lecture in our Advanced Fluid Dynamics series'."
                    },
                    {
                        "questionNumber": 32,
                        "prefix": "The marine predator analyzed in the first case study is the shortfin ",
                        "suffix": " shark.",
                        "answer": "mako",
                        "acceptedAnswers": ["mako", "Mako"],
                        "targetTurn": 1,
                        "explanation": "Prof. Finch introduces 'the fast-swimming shortfin mako shark'."
                    },
                    {
                        "questionNumber": 33,
                        "prefix": "Microscopic tooth-like scales on shark skin are called dermal ",
                        "answer": "denticles",
                        "acceptedAnswers": ["denticles", "Denticles"],
                        "targetTurn": 1,
                        "explanation": "Prof. Finch states shark skin is covered in 'millions of microscopic tooth-like scales called dermal denticles'."
                    },
                    {
                        "questionNumber": 34,
                        "prefix": "Longitudinal micro-grooves on the scales are called ",
                        "answer": "riblets",
                        "acceptedAnswers": ["riblets", "Riblets"],
                        "targetTurn": 2,
                        "explanation": "Prof. Finch refers to 'longitudinal micro-grooves or \'riblets\' aligned parallel to the flow of fluid'."
                    },
                    {
                        "questionNumber": 35,
                        "prefix": "Applying synthetic riblet films to aircraft wings reduces aerodynamic drag by up to ",
                        "suffix": " percent.",
                        "answer": "8",
                        "acceptedAnswers": ["8", "eight", "8%"],
                        "targetTurn": 2,
                        "explanation": "Prof. Finch notes engineers 'have achieved up to an 8 percent reduction in aerodynamic parasitic drag'."
                    },
                    {
                        "questionNumber": 36,
                        "prefix": "Silent flight allows hunting barn owls to remain undetected by small ",
                        "answer": "rodents",
                        "acceptedAnswers": ["rodents", "Rodents"],
                        "targetTurn": 3,
                        "explanation": "Prof. Finch notes owls 'fly virtually undetected by small rodents'."
                    },
                    {
                        "questionNumber": 37,
                        "prefix": "The leading edge of owl flight feathers features a stiff, comb-like ",
                        "answer": "serration",
                        "acceptedAnswers": ["serration", "comb-like serration"],
                        "targetTurn": 4,
                        "explanation": "Prof. Finch states the feather leading edge possesses a 'stiff, comb-like serration'."
                    },
                    {
                        "questionNumber": 38,
                        "prefix": "The trailing edge of owl feathers terminates in a soft, flexible ",
                        "answer": "fringe",
                        "acceptedAnswers": ["fringe", "flexible fringe"],
                        "targetTurn": 5,
                        "explanation": "Prof. Finch states the trailing edge 'terminates in a soft, flexible fringe'."
                    },
                    {
                        "questionNumber": 39,
                        "prefix": "Retrofitted owl serrations reduce wind turbine blade noise by approximately ",
                        "suffix": " decibels.",
                        "answer": "3",
                        "acceptedAnswers": ["3", "three", "3 dB"],
                        "targetTurn": 6,
                        "explanation": "Prof. Finch confirms: 'reduces aerodynamic blade noise by approximately 3 decibels'."
                    },
                    {
                        "questionNumber": 40,
                        "prefix": "Next week's lecture will examine stall resistance inspired by humpback whale ",
                        "answer": "tubercles",
                        "acceptedAnswers": ["tubercles", "flipper tubercles"],
                        "targetTurn": 7,
                        "explanation": "Prof. Finch concludes: 'we will examine how humpback whale flipper tubercles enhance stall resistance'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 2 - SECTION 1: Sports Club Registration (Questions 1–10)
    # =========================================================================
    {
        "id": "list-sec1-sport-02",
        "audioFilename": "section1_sports_club.mp3",
        "skill": "listening",
        "questionType": "form_completion",
        "difficulty": "easy",
        "band": "Band 5.5–6.5",
        "granularity": "section",
        "title": "Listening Section 1: Riverdale Community Sports Club Membership Registration",
        "topic": "Community Recreation & Sports Facility Registration",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-SoniaNeural", "Karen", "Good afternoon, Riverdale Community Sports Club. Karen speaking. How may I assist you?"),
            ("en-GB-RyanNeural", "Mark Davis", "Hello Karen, my name is Mark Davis. I recently moved to Riverdale and I'd like to inquire about joining your fitness center and swimming facilities."),
            ("en-GB-SoniaNeural", "Karen", "Welcome to Riverdale, Mark! Let me take down your contact details. Could I have your mobile number first, please?"),
            ("en-GB-RyanNeural", "Mark Davis", "Yes, it is 07892 411503."),
            ("en-GB-SoniaNeural", "Karen", "Thank you: 07892 411503. Now, we offer three annual membership tiers: Bronze, Silver, and Gold. Bronze provides gym access only. Silver includes full gymnasium equipment plus unlimited access to our 50-meter heated Olympic pool. Gold includes tennis courts and personal training."),
            ("en-GB-RyanNeural", "Mark Davis", "Swimming is my main workout, so the Silver tier sounds absolutely ideal for my needs."),
            ("en-GB-SoniaNeural", "Karen", "Excellent choice. For the Silver package, standard peak membership is 65 pounds per month, but if you prefer our off-peak weekday option—valid Monday to Friday from 9:00 AM to 4:00 PM—the fee is reduced to just 42 pounds monthly."),
            ("en-GB-RyanNeural", "Mark Davis", "I work freelance from home, so off-peak weekdays at 42 pounds suits my schedule perfectly."),
            ("en-GB-SoniaNeural", "Karen", "Wonderful. We also offer private locker rentals in the changing suites. A small personal locker is an optional extra at 15 pounds for the full year."),
            ("en-GB-RyanNeural", "Mark Davis", "Yes, I'll definitely take a private locker for 15 pounds. That's very reasonable."),
            ("en-GB-SoniaNeural", "Karen", "Now, before using the Olympic pool, all new members must attend a compulsory 20-minute safety induction with our chief lifeguard. We run these sessions every Tuesday morning and Thursday evening."),
            ("en-GB-RyanNeural", "Mark Davis", "Thursday evening at 6:30 PM would work best for me. Could you book me in for that?"),
            ("en-GB-SoniaNeural", "Karen", "You're all booked for Thursday evening. Please remember to bring government photo ID and a towel to reception when you arrive."),
            ("en-GB-RyanNeural", "Mark Davis", "Photo ID and a towel, noted. Thanks so much for your help, Karen!"),
            ("en-GB-SoniaNeural", "Karen", "You're very welcome, Mark. See you on Thursday!")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec1-sport-02",
                "type": "form_completion",
                "title": "Questions 1–10",
                "instruction": "Complete the form below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 1,
                        "prefix": "Applicant Full Name: ",
                        "answer": "Mark Davis",
                        "acceptedAnswers": ["Mark Davis", "mark davis"],
                        "targetTurn": 1,
                        "explanation": "The applicant gives his name: 'my name is Mark Davis'."
                    },
                    {
                        "questionNumber": 2,
                        "prefix": "Contact Mobile Number: ",
                        "answer": "07892 411503",
                        "acceptedAnswers": ["07892 411503", "07892411503"],
                        "targetTurn": 3,
                        "explanation": "Mark states his mobile number is '07892 411503'."
                    },
                    {
                        "questionNumber": 3,
                        "prefix": "Selected Membership Tier: ",
                        "suffix": " tier",
                        "answer": "Silver",
                        "acceptedAnswers": ["Silver", "silver"],
                        "targetTurn": 5,
                        "explanation": "Mark chooses: 'the Silver tier sounds absolutely ideal for my needs'."
                    },
                    {
                        "questionNumber": 4,
                        "prefix": "Length of Heated Olympic Pool: ",
                        "suffix": " meters",
                        "answer": "50",
                        "acceptedAnswers": ["50", "fifty", "50m", "50 meters"],
                        "targetTurn": 4,
                        "explanation": "Karen mentions their '50-meter heated Olympic pool'."
                    },
                    {
                        "questionNumber": 5,
                        "prefix": "Off-Peak Weekday Monthly Fee: £",
                        "answer": "42",
                        "acceptedAnswers": ["42", "forty two", "42 pounds"],
                        "targetTurn": 6,
                        "explanation": "Karen states the off-peak fee is 'reduced to just 42 pounds monthly'."
                    },
                    {
                        "questionNumber": 6,
                        "prefix": "Off-Peak Hours: Monday to Friday until ",
                        "answer": "4:00 PM",
                        "acceptedAnswers": ["4:00 PM", "4pm", "4 PM", "4:00pm", "4.00 pm"],
                        "targetTurn": 6,
                        "explanation": "Karen states off-peak hours are 'from 9:00 AM to 4:00 PM'."
                    },
                    {
                        "questionNumber": 7,
                        "prefix": "Annual Fee for Private Changing Locker: £",
                        "answer": "15",
                        "acceptedAnswers": ["15", "fifteen", "15 pounds"],
                        "targetTurn": 8,
                        "explanation": "Karen states locker rental is '15 pounds for the full year'."
                    },
                    {
                        "questionNumber": 8,
                        "prefix": "Duration of Compulsory Pool Induction: ",
                        "suffix": " minutes",
                        "answer": "20",
                        "acceptedAnswers": ["20", "twenty", "20 minutes"],
                        "targetTurn": 10,
                        "explanation": "Karen mentions 'a compulsory 20-minute safety induction with our chief lifeguard'."
                    },
                    {
                        "questionNumber": 9,
                        "prefix": "Mark's Booked Induction Time: ",
                        "answer": "Thursday evening",
                        "acceptedAnswers": ["Thursday evening", "Thursday"],
                        "targetTurn": 11,
                        "explanation": "Mark confirms: 'Thursday evening at 6:30 PM would work best for me'."
                    },
                    {
                        "questionNumber": 10,
                        "prefix": "Items to Bring: Photo ID and a ",
                        "answer": "towel",
                        "acceptedAnswers": ["towel", "a towel"],
                        "targetTurn": 12,
                        "explanation": "Karen reminds Mark: 'bring government photo ID and a towel to reception'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 2 - SECTION 2: River Walk Volunteering (Questions 11–20)
    # =========================================================================
    {
        "id": "list-sec2-river-04",
        "audioFilename": "section2_river_walk.mp3",
        "skill": "listening",
        "questionType": "note_completion",
        "difficulty": "medium",
        "band": "Band 6.0–7.0",
        "granularity": "section",
        "title": "Listening Section 2: Greenfield Heritage River Walk & Community Volunteering",
        "topic": "Community Volunteer Projects & Ecological Trails",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-ThomasNeural", "Julian Barnes", "Good evening, everyone. My name is Julian Barnes, Coordinator for the Greenfield Heritage River Project. Thank you all for coming to tonight's informational session on our upcoming community volunteer campaign."),
            ("en-GB-ThomasNeural", "Julian Barnes", "The Greenfield River Trail stretches along 14 kilometers of historic riparian wetlands, originally established in 1892 as an industrial barge canal."),
            ("en-GB-ThomasNeural", "Julian Barnes", "Our primary environmental objective this autumn is clearing invasive Japanese knotweed and replanting 800 native willow trees along the riverbank to stabilize soil erosion."),
            ("en-GB-ThomasNeural", "Julian Barnes", "Volunteers will work in organized teams on Saturday mornings from 9:00 AM until 1:00 PM. All heavy-duty gardening gloves, shovels, and high-visibility safety vests will be provided free of charge by the municipal parks trust."),
            ("en-GB-ThomasNeural", "Julian Barnes", "However, all volunteers are strictly required to wear waterproof rubber boots, as several stretches along the marshland trail can become exceptionally muddy."),
            ("en-GB-ThomasNeural", "Julian Barnes", "At the conclusion of each Saturday session, a complimentary hot lunch prepared with organic local vegetables will be served at the community boat house."),
            ("en-GB-ThomasNeural", "Julian Barnes", "If you would like to register your participation, please complete the volunteer waiver form at the back of the hall before leaving tonight. We look forward to seeing you this Saturday!")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec2-river-04",
                "type": "note_completion",
                "title": "Questions 11–20",
                "instruction": "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 11,
                        "prefix": "The speaker, Julian Barnes, serves as the project ",
                        "answer": "Coordinator",
                        "acceptedAnswers": ["Coordinator", "coordinator"],
                        "targetTurn": 0,
                        "explanation": "Julian introduces himself as 'Coordinator for the Greenfield Heritage River Project'."
                    },
                    {
                        "questionNumber": 12,
                        "prefix": "Total length of the Greenfield River Trail: ",
                        "suffix": " kilometers",
                        "answer": "14",
                        "acceptedAnswers": ["14", "fourteen"],
                        "targetTurn": 1,
                        "explanation": "Julian states the trail 'stretches along 14 kilometers of historic riparian wetlands'."
                    },
                    {
                        "questionNumber": 13,
                        "prefix": "The original barge canal was established in the year ",
                        "answer": "1892",
                        "acceptedAnswers": ["1892"],
                        "targetTurn": 1,
                        "explanation": "Julian notes the canal was 'originally established in 1892'."
                    },
                    {
                        "questionNumber": 14,
                        "prefix": "Invasive plant species to be eradicated: Japanese ",
                        "answer": "knotweed",
                        "acceptedAnswers": ["knotweed", "Japanese knotweed"],
                        "targetTurn": 2,
                        "explanation": "Julian highlights 'clearing invasive Japanese knotweed'."
                    },
                    {
                        "questionNumber": 15,
                        "prefix": "Tree species to be planted along riverbanks: native ",
                        "answer": "willow",
                        "acceptedAnswers": ["willow", "native willow", "willow trees"],
                        "targetTurn": 2,
                        "explanation": "Julian specifies: 'replanting 800 native willow trees along the riverbank'."
                    },
                    {
                        "questionNumber": 16,
                        "prefix": "Total number of native trees to be replanted: ",
                        "answer": "800",
                        "acceptedAnswers": ["800", "eight hundred"],
                        "targetTurn": 2,
                        "explanation": "Julian confirms: 'replanting 800 native willow trees'."
                    },
                    {
                        "questionNumber": 17,
                        "prefix": "Saturday volunteer shifts conclude at ",
                        "answer": "1:00 PM",
                        "acceptedAnswers": ["1:00 PM", "1pm", "1 PM", "1:00pm"],
                        "targetTurn": 3,
                        "explanation": "Julian mentions working 'from 9:00 AM until 1:00 PM'."
                    },
                    {
                        "questionNumber": 18,
                        "prefix": "Protective equipment provided includes gloves, shovels, and safety ",
                        "answer": "vests",
                        "acceptedAnswers": ["vests", "safety vests"],
                        "targetTurn": 3,
                        "explanation": "Julian notes: 'high-visibility safety vests will be provided free of charge'."
                    },
                    {
                        "questionNumber": 19,
                        "prefix": "Essential personal footwear required: waterproof ",
                        "answer": "boots",
                        "acceptedAnswers": ["boots", "rubber boots", "waterproof boots"],
                        "targetTurn": 4,
                        "explanation": "Julian emphasizes: 'all volunteers are strictly required to wear waterproof rubber boots'."
                    },
                    {
                        "questionNumber": 20,
                        "prefix": "Complimentary hot lunch is provided at the community ",
                        "answer": "boat house",
                        "acceptedAnswers": ["boat house", "boathouse"],
                        "targetTurn": 5,
                        "explanation": "Julian confirms lunch 'will be served at the community boat house'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 2 - SECTION 3: Byzantine Arch Seminar (Questions 21–30)
    # =========================================================================
    {
        "id": "list-sec3-arch-06",
        "audioFilename": "section3_byzantine_arch.mp3",
        "skill": "listening",
        "questionType": "multiple_choice",
        "difficulty": "advanced",
        "band": "Band 7.0–8.0",
        "granularity": "section",
        "title": "Listening Section 3: Architecture Seminar on Roman vs Byzantine Arch Construction",
        "topic": "Architectural History & Structural Engineering",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-SoniaNeural", "Chloe", "Marcus, have you finalized our presentation slides for tomorrow's comparative architectural seminar?"),
            ("en-GB-RyanNeural", "Marcus", "Almost, Chloe. I've drafted our analysis comparing classical Roman semicircular barrel vaults with sixth-century Byzantine pendentive dome architecture, as seen in Hagia Sophia."),
            ("en-GB-SoniaNeural", "Chloe", "That's great. Let's make sure we clearly explain the structural breakthrough of the pendentive. In Roman architecture, a circular dome could only sit directly atop a cylindrical circular wall, like the Pantheon in Rome."),
            ("en-GB-RyanNeural", "Marcus", "Exactly. Whereas the Byzantine architects solved the geometric problem of placing a massive circular dome over a square room by inventing triangular curved masonry supports called pendentives."),
            ("en-GB-SoniaNeural", "Chloe", "Right. Pendentives transfer the massive downward and outward thrust of the dome down to four massive corner piers, which freed up the four side walls to be pierced with large arched windows."),
            ("en-GB-RyanNeural", "Marcus", "And regarding building materials: Roman architects relied heavily on pozzolanic volcanic concrete, which was cast over wooden temporary centering frameworks. In contrast, Byzantine masons primarily used thin kiln-fired bricks laid in thick beds of lime mortar with crushed brick dust."),
            ("en-GB-SoniaNeural", "Chloe", "Good point! And for our concluding slide, we should emphasize how this architectural system influenced later Ottoman imperial mosques, such as the Blue Mosque designed by Sedefkar Mehmed Agha."),
            ("en-GB-RyanNeural", "Marcus", "Agreed. I'll insert a high-resolution comparative cross-section diagram to illustrate the load paths right now.")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec3-arch-06-p1",
                "type": "multiple_choice",
                "title": "Questions 21–25",
                "instruction": "Choose the correct letter, A, B, C or D.",
                "questions": [
                    {
                        "questionNumber": 21,
                        "question": "Which historic sixth-century building did Chloe and Marcus choose as their primary case study?",
                        "options": [
                            {"key": "A", "text": "The Colosseum in Rome"},
                            {"key": "B", "text": "Hagia Sophia in Istanbul"},
                            {"key": "C", "text": "St. Peter's Basilica in Vatican City"},
                            {"key": "D", "text": "The Parthenon in Athens"}
                        ],
                        "answer": "B",
                        "targetTurn": 1,
                        "explanation": "Marcus mentions 'sixth-century Byzantine pendentive dome architecture, as seen in Hagia Sophia'."
                    },
                    {
                        "questionNumber": 22,
                        "question": "What structural dilemma was solved by the Byzantine invention of the pendentive?",
                        "options": [
                            {"key": "A", "text": "Erecting wooden roofs over wet marshes"},
                            {"key": "B", "text": "Placing a circular dome over a square room"},
                            {"key": "C", "text": "Waterproofing subterranean bathhouses"},
                            {"key": "D", "text": "Carving granite columns without heavy cranes"}
                        ],
                        "answer": "B",
                        "targetTurn": 3,
                        "explanation": "Marcus explains Byzantine architects 'solved the geometric problem of placing a massive circular dome over a square room by inventing triangular curved masonry supports called pendentives'."
                    },
                    {
                        "questionNumber": 23,
                        "question": "How did the use of pendentives affect the four exterior side walls of Byzantine churches?",
                        "options": [
                            {"key": "A", "text": "They had to be made solid without any doors"},
                            {"key": "B", "text": "They could be pierced with large arched windows to let in light"},
                            {"key": "C", "text": "They were constructed from imported Egyptian marble"},
                            {"key": "D", "text": "They were supported by external flying buttresses"}
                        ],
                        "answer": "B",
                        "targetTurn": 4,
                        "explanation": "Chloe explains: 'which freed up the four side walls to be pierced with large arched windows'."
                    },
                    {
                        "questionNumber": 24,
                        "question": "Unlike Roman concrete construction, Byzantine masons predominantly constructed arches using:",
                        "options": [
                            {"key": "A", "text": "Cast bronze beams"},
                            {"key": "B", "text": "Thin kiln-fired bricks set in thick lime mortar"},
                            {"key": "C", "text": "Hand-chiseled granite blocks without mortar"},
                            {"key": "D", "text": "Solid timber trusses filled with volcanic ash"}
                        ],
                        "answer": "B",
                        "targetTurn": 5,
                        "explanation": "Marcus specifies: 'Byzantine masons primarily used thin kiln-fired bricks laid in thick beds of lime mortar'."
                    },
                    {
                        "questionNumber": 25,
                        "question": "What famous 17th-century Ottoman building was directly influenced by Byzantine dome architecture?",
                        "options": [
                            {"key": "A", "text": "Topkapi Palace"},
                            {"key": "B", "text": "The Blue Mosque"},
                            {"key": "C", "text": "The Grand Bazaar"},
                            {"key": "D", "text": "Galata Tower"}
                        ],
                        "answer": "B",
                        "targetTurn": 6,
                        "explanation": "Chloe cites: 'such as the Blue Mosque designed by Sedefkar Mehmed Agha'."
                    }
                ]
            },
            {
                "id": "group-list-sec3-arch-06-p2",
                "type": "sentence_completion",
                "title": "Questions 26–30",
                "instruction": "Complete the sentences below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 26,
                        "prefix": "In Roman design, circular domes sat directly on a cylindrical ",
                        "answer": "circular wall",
                        "acceptedAnswers": ["circular wall"],
                        "targetTurn": 2,
                        "explanation": "Chloe notes: 'In Roman architecture, a circular dome could only sit directly atop a cylindrical circular wall'."
                    },
                    {
                        "questionNumber": 27,
                        "prefix": "Byzantine pendentives transfer dome thrust down to four corner ",
                        "answer": "piers",
                        "acceptedAnswers": ["piers", "corner piers"],
                        "targetTurn": 4,
                        "explanation": "Chloe states pendentives transfer thrust 'down to four massive corner piers'."
                    },
                    {
                        "questionNumber": 28,
                        "prefix": "Roman concrete vaults were cast over temporary wooden ",
                        "answer": "centering",
                        "acceptedAnswers": ["centering", "centering frameworks"],
                        "targetTurn": 5,
                        "explanation": "Marcus notes concrete was 'cast over wooden temporary centering frameworks'."
                    },
                    {
                        "questionNumber": 29,
                        "prefix": "Byzantine lime mortar was strengthened with crushed ",
                        "answer": "brick dust",
                        "acceptedAnswers": ["brick dust"],
                        "targetTurn": 5,
                        "explanation": "Marcus mentions mortar blended with 'crushed brick dust'."
                    },
                    {
                        "questionNumber": 30,
                        "prefix": "Marcus will illustrate load paths using a comparative ",
                        "answer": "cross-section diagram",
                        "acceptedAnswers": ["cross-section diagram", "cross-section", "diagram"],
                        "targetTurn": 7,
                        "explanation": "Marcus concludes: 'I\'ll insert a high-resolution comparative cross-section diagram'."
                    }
                ]
            }
        ],
        "questions": []
    },

    # =========================================================================
    # TEST 2 - SECTION 4: Maritime Silk Road Lecture (Questions 31–40)
    # =========================================================================
    {
        "id": "list-sec4-silk-08",
        "audioFilename": "section4_silk_road_spices.mp3",
        "skill": "listening",
        "questionType": "multiple_choice",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "section",
        "title": "Listening Section 4: University Lecture on the Maritime Silk Road & Medieval Spice Currency",
        "topic": "Economic History & Maritime Trade",
        "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
        "turns": [
            ("en-GB-SoniaNeural", "Dr. Davies", "Welcome back, students of Economic History. In today's session, we turn our attention from overland Eurasian caravan trails to the Maritime Silk Road—the vast nautical trading network that connected China, Southeast Asia, India, and the Mediterranean between the 7th and 15th centuries."),
            ("en-GB-SoniaNeural", "Dr. Davies", "While silk and porcelain were vital Chinese luxury exports, the true high-velocity currency of maritime commerce was spices: predominantly black pepper from the Malabar coast of India, and cloves, nutmeg, and mace from the remote Maluku islands of eastern Indonesia."),
            ("en-GB-SoniaNeural", "Dr. Davies", "In medieval Western Europe, spices were not merely culinary flavorings for elite banquets; they functioned as a store of value and international trade currency. Black pepper peppercorns were counted individually and accepted for land rents, court dowries, and customs duties. In medieval London, the Guild of Pepperers was granted statutory powers to inspect weights and settle commercial debts, giving rise to the legal phrase 'peppercorn rent'."),
            ("en-GB-SoniaNeural", "Dr. Davies", "The maritime voyage relied on seasonal climatic meteorological cycles known as the monsoon winds. Between May and September, the southwest monsoon propelled Arab and Persian dhows across the Indian Ocean toward the Strait of Malacca. Traders would winter in Southeast Asian ports for several months, trading textiles for cloves, before the northeast monsoon reversed direction between November and March, allowing them to sail safely home."),
            ("en-GB-SoniaNeural", "Dr. Davies", "The astronomical markup on spices was staggering. A sack of nutmeg purchased in the Banda Islands for a few copper coins could be sold in Venice or Antwerp for over a thousand times its original purchase price. This immense profit margin ultimately compelled European monarchs to finance the Age of Discovery, seeking direct oceanic routes to Asia and fundamentally shifting global geopolitical power.")
        ],
        "questionGroups": [
            {
                "id": "group-list-sec4-silk-08",
                "type": "note_completion",
                "title": "Questions 31–40",
                "instruction": "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
                "wordLimitRule": "NO MORE THAN TWO WORDS AND/OR A NUMBER",
                "questions": [
                    {
                        "questionNumber": 31,
                        "prefix": "The Maritime Silk Road flourished between the ",
                        "suffix": " centuries.",
                        "answer": "7th and 15th",
                        "acceptedAnswers": ["7th and 15th", "7th to 15th", "seventh and fifteenth"],
                        "targetTurn": 0,
                        "explanation": "Dr. Davies dates the network 'between the 7th and 15th centuries'."
                    },
                    {
                        "questionNumber": 32,
                        "prefix": "Black pepper was harvested primarily along the ",
                        "suffix": " coast of India.",
                        "answer": "Malabar",
                        "acceptedAnswers": ["Malabar", "malabar"],
                        "targetTurn": 1,
                        "explanation": "Dr. Davies notes pepper came from 'the Malabar coast of India'."
                    },
                    {
                        "questionNumber": 33,
                        "prefix": "Cloves and nutmeg originated from the ",
                        "suffix": " islands of Indonesia.",
                        "answer": "Maluku",
                        "acceptedAnswers": ["Maluku", "maluku"],
                        "targetTurn": 1,
                        "explanation": "Dr. Davies cites 'the remote Maluku islands of eastern Indonesia'."
                    },
                    {
                        "questionNumber": 34,
                        "prefix": "In medieval Western Europe, spices served as an international ",
                        "answer": "trade currency",
                        "acceptedAnswers": ["trade currency", "currency", "store of value"],
                        "targetTurn": 2,
                        "explanation": "Dr. Davies notes spices 'functioned as a store of value and international trade currency'."
                    },
                    {
                        "questionNumber": 35,
                        "prefix": "Black pepper was officially accepted for paying land rents, dowries, and customs ",
                        "answer": "duties",
                        "acceptedAnswers": ["duties", "customs duties"],
                        "targetTurn": 2,
                        "explanation": "Dr. Davies states pepper was accepted for 'land rents, court dowries, and customs duties'."
                    },
                    {
                        "questionNumber": 36,
                        "prefix": "The medieval London guild granted statutory weighing powers was the Guild of ",
                        "answer": "Pepperers",
                        "acceptedAnswers": ["Pepperers", "pepperers"],
                        "targetTurn": 2,
                        "explanation": "Dr. Davies cites 'the Guild of Pepperers was granted statutory powers to inspect weights'."
                    },
                    {
                        "questionNumber": 37,
                        "prefix": "Between May and September, ships sailed eastward propelled by the ",
                        "suffix": " monsoon.",
                        "answer": "southwest",
                        "acceptedAnswers": ["southwest", "south-west", "southwest monsoon"],
                        "targetTurn": 3,
                        "explanation": "Dr. Davies explains: 'Between May and September, the southwest monsoon propelled Arab and Persian dhows'."
                    },
                    {
                        "questionNumber": 38,
                        "prefix": "Traders returned westward between November and March using the ",
                        "suffix": " monsoon.",
                        "answer": "northeast",
                        "acceptedAnswers": ["northeast", "north-east", "northeast monsoon"],
                        "targetTurn": 3,
                        "explanation": "Dr. Davies states the 'northeast monsoon reversed direction between November and March, allowing them to sail safely home'."
                    },
                    {
                        "questionNumber": 39,
                        "prefix": "Nutmeg sacks purchased in the Banda Islands were sold for 1,000 times higher in Venice or ",
                        "answer": "Antwerp",
                        "acceptedAnswers": ["Antwerp", "antwerp"],
                        "targetTurn": 4,
                        "explanation": "Dr. Davies notes nutmeg 'could be sold in Venice or Antwerp for over a thousand times its original purchase price'."
                    },
                    {
                        "questionNumber": 40,
                        "prefix": "The enormous profit margin on spices prompted monarchs to finance the ",
                        "answer": "Age of Discovery",
                        "acceptedAnswers": ["Age of Discovery", "age of discovery"],
                        "targetTurn": 4,
                        "explanation": "Dr. Davies concludes: 'This immense profit margin ultimately compelled European monarchs to finance the Age of Discovery'."
                    }
                ]
            }
        ],
        "questions": []
    }
]

# Ensure item.questions is populated from questionGroups for backward compatibility
for sec in LISTENING_SECTIONS:
    if "questionGroups" in sec and sec["questionGroups"]:
        sec["questions"] = [q for g in sec["questionGroups"] for q in g.get("questions", [])]
