"""
Authentic IELTS Speaking Dataset Specification
Contains 20 high-caliber Speaking modules:
- 12 Part 1 Everyday Topic Modules (4 questions each = 48 questions)
- 8 Part 2 Cue Card + Part 3 In-depth Discussion Modules (with 1-min prep / 2-min speaking, 4 cue bullet points, rounding-off question, and 4-5 rigorous abstract Part 3 discussion questions)

All modules include authentic idioms with clear definitions and contextual examples,
alongside comprehensive band assessment criteria.
"""

SPEAKING_ITEMS = [
    # =========================================================================
    # PART 1 TOPIC MODULES (12 Modules, 48 Questions)
    # =========================================================================
    {
        "id": "spk-part1-01",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "easy",
        "band": "Band 6.0–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Hometown, Architecture & Local Amenities",
        "topic": "Hometown & Community Living",
        "speakingTask": {
            "part": 1,
            "topic": "Hometown & Architecture",
            "part1Questions": [
                {"questionNumber": 1, "question": "Where is your hometown situated, and what makes it notable or unique?"},
                {"questionNumber": 2, "question": "What kind of architectural styles are prominent in your neighborhood?"},
                {"questionNumber": 3, "question": "Has your hometown experienced substantial transformation over the past decade?"},
                {"questionNumber": 4, "question": "What public amenity would you introduce to enhance your hometown's livability?"}
            ],
            "recommendedIdioms": [
                {"phrase": "bustling metropolis", "meaning": "a very busy, dynamic, and energetic city", "example": "Over the last fifteen years, my quiet town has transformed into a bustling metropolis."},
                {"phrase": "on the outskirts", "meaning": "in the outer suburban districts of a city", "example": "I reside in a peaceful residential pocket on the outskirts of the capital."}
            ],
            "discourseMarkers": ["To be completely honest", "As a matter of fact", "In terms of architecture", "Looking back over the years"],
            "assessmentCriteria": {
                "fluencyCoherence": "Speak at a steady, natural tempo with minimal hesitation; expand on simple yes/no answers with concrete local examples.",
                "lexicalResource": "Incorporate descriptive urban terminology: 'sprawling residential enclave', 'historical heritage buildings', 'pedestrianized zones'.",
                "grammaticalRange": "Combine present perfect for changes with modal structures for future improvements.",
                "pronunciation": "Maintain natural sentence stress and clear intonation when contrasting past and present."
            }
        }
    },
    {
        "id": "spk-part1-02",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Work, Academic Studies & Career Ambitions",
        "topic": "Workplace & Higher Education",
        "speakingTask": {
            "part": 1,
            "topic": "Career Aspirations & Education",
            "part1Questions": [
                {"questionNumber": 5, "question": "Do you currently work or are you undertaking academic studies?"},
                {"questionNumber": 6, "question": "What originally motivated you to pursue this specific discipline or vocation?"},
                {"questionNumber": 7, "question": "What is the most intellectually demanding aspect of your current daily routine?"},
                {"questionNumber": 8, "question": "Where do you envision yourself professionally in five years' time?"}
            ],
            "recommendedIdioms": [
                {"phrase": "steep learning curve", "meaning": "a difficult and rapid process of acquiring new skills", "example": "When I first joined the engineering division, there was an incredibly steep learning curve."},
                {"phrase": "in the long run", "meaning": "over an extended period in the future", "example": "Although the postgraduate coursework is exhausting, it will pay dividends in the long run."}
            ],
            "discourseMarkers": ["Primarily because", "What drew me to this field was", "On a day-to-day basis", "Looking ahead professionally"],
            "assessmentCriteria": {
                "fluencyCoherence": "Provide smooth multi-sentence explanations detailing professional responsibilities and academic motivations.",
                "lexicalResource": "Utilize precise occupational vocabulary: 'cross-functional collaboration', 'analytical rigor', 'career progression'.",
                "grammaticalRange": "Employ varied future forms ('I intend to...', 'I envision myself transitioning toward...') and conditional clauses.",
                "pronunciation": "Clear enunciation of multisyllabic academic and technical terminology."
            }
        }
    },
    {
        "id": "spk-part1-03",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Digital Habits, Smart Devices & Screen Time",
        "topic": "Digital Habits & Technology",
        "speakingTask": {
            "part": 1,
            "topic": "Digital Habits & Artificial Intelligence",
            "part1Questions": [
                {"questionNumber": 9, "question": "How many hours a day do you typically spend interacting with digital screens?"},
                {"questionNumber": 10, "question": "Do you prefer reading books on electronic tablets or traditional printed paper?"},
                {"questionNumber": 11, "question": "What smartphone application could you not function without on a typical workday?"},
                {"questionNumber": 12, "question": "Do you feel digital notifications distract from sustained intellectual focus?"}
            ],
            "recommendedIdioms": [
                {"phrase": "double-edged sword", "meaning": "something possessing both advantageous and detrimental qualities", "example": "Smartphones are a double-edged sword; they provide instant knowledge but destroy deep concentration."},
                {"phrase": "at the touch of a button", "meaning": "instantly and effortlessly accessible", "example": "Virtually any academic research journal can now be retrieved at the touch of a button."}
            ],
            "discourseMarkers": ["Without a shadow of a doubt", "If I had to choose", "To put it mildly", "From my perspective"],
            "assessmentCriteria": {
                "fluencyCoherence": "Express personal habits smoothly while analyzing digital benefits and psychological pitfalls.",
                "lexicalResource": "Nuanced technological lexicon: 'information overload', 'algorithmic recommendations', 'tactile reading experience'.",
                "grammaticalRange": "Effective use of unreal conditionals ('If I didn't have my calendar app, I would probably fail to attend...') and contrastive clauses.",
                "pronunciation": "Natural rhythm and avoidance of robotic, monotone delivery."
            }
        }
    },
    {
        "id": "spk-part1-04",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "easy",
        "band": "Band 6.0–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Leisure Activities, Outdoor Recreation & Sport",
        "topic": "Recreation & Physical Health",
        "speakingTask": {
            "part": 1,
            "topic": "Leisure & Outdoor Recreation",
            "part1Questions": [
                {"questionNumber": 13, "question": "What outdoor recreational activities do you enjoy most during weekends?"},
                {"questionNumber": 14, "question": "Did you participate in organized team sports during your primary or secondary school years?"},
                {"questionNumber": 15, "question": "Do you prefer exercising individually or participating in collective group fitness?"},
                {"questionNumber": 16, "question": "Are there adequate public recreational parks in the vicinity of your home?"}
            ],
            "recommendedIdioms": [
                {"phrase": "blow off steam", "meaning": "release pent-up physical energy or mental stress", "example": "Going for an intense trail run on Saturday mornings is my favorite way to blow off steam."},
                {"phrase": "recharge my batteries", "meaning": "restore physical energy and mental clarity after exertion", "example": "Spending an afternoon hiking in the mountains completely recharges my batteries."}
            ],
            "discourseMarkers": ["Whenever I get the chance", "Back in my school days", "I'm definitely inclined toward", "Fortunately in my neighborhood"],
            "assessmentCriteria": {
                "fluencyCoherence": "Connect recreational preferences with lifestyle balance and physical wellness.",
                "lexicalResource": "Sporting and leisure phrases: 'cardiovascular endurance', 'team camaraderie', 'lush green open spaces'.",
                "grammaticalRange": "Contrast past habits ('I used to play competitive basketball...') with present preferences.",
                "pronunciation": "Vary pitch naturally to convey enthusiasm and personal enjoyment."
            }
        }
    },
    {
        "id": "spk-part1-05",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Reading Habits, Literature & Morning News",
        "topic": "Literature & Media Consumption",
        "speakingTask": {
            "part": 1,
            "topic": "Reading & Literature",
            "part1Questions": [
                {"questionNumber": 17, "question": "What genres of literature or non-fiction do you typically enjoy reading?"},
                {"questionNumber": 18, "question": "Do you prefer consuming daily current affairs news through podcasts, video, or written articles?"},
                {"questionNumber": 19, "question": "Did your parents or teachers encourage you to read books during early childhood?"},
                {"questionNumber": 20, "question": "Do you still visit physical public libraries or bookshops in your city?"}
            ],
            "recommendedIdioms": [
                {"phrase": "food for thought", "meaning": "stimulating ideas that encourage deep, careful contemplation", "example": "Historical non-fiction always gives me plenty of food for thought regarding contemporary politics."},
                {"phrase": "page-turner", "meaning": "a captivating and engrossing book that one cannot put down", "example": "That investigative journalism piece on economic reform was an absolute page-turner."}
            ],
            "discourseMarkers": ["Generally speaking", "As far as reading is concerned", "I find that", "Reflecting on my childhood"],
            "assessmentCriteria": {
                "fluencyCoherence": "Speak expansively without long pauses; give specific book titles, genres, or journalistic outlets.",
                "lexicalResource": "Literary and journalistic terms: 'investigative reporting', 'biographical memoirs', 'critical analysis'.",
                "grammaticalRange": "Fluid coordination using relative clauses ('...which really broadened my horizons') and concession.",
                "pronunciation": "Clear vowel length distinctions and natural elision between words."
            }
        }
    },
    {
        "id": "spk-part1-06",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "easy",
        "band": "Band 6.0–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Travel, Public Transportation & Daily Commuting",
        "topic": "Transportation & Urban Mobility",
        "speakingTask": {
            "part": 1,
            "topic": "Travel & Transportation",
            "part1Questions": [
                {"questionNumber": 21, "question": "What mode of transportation do you primarily rely on for your daily commute?"},
                {"questionNumber": 22, "question": "How reliable and punctual is the public transit network in your city?"},
                {"questionNumber": 23, "question": "Do you enjoy embarking on long-distance scenic railway journeys?"},
                {"questionNumber": 24, "question": "What is an international travel destination you are eager to explore in the future?"}
            ],
            "recommendedIdioms": [
                {"phrase": "hustle and bustle", "meaning": "energetic, noisy, and fast-paced activity in an urban area", "example": "Taking the subway during peak morning rush hour exposes you to the sheer hustle and bustle of the city."},
                {"phrase": "off the beaten track", "meaning": "isolated, rural, and distant from standard tourist trails", "example": "When I travel overseas, I always prefer exploring remote villages off the beaten track."}
            ],
            "discourseMarkers": ["For the most part", "During peak rush hour", "What appeals to me about trains is", "Given the opportunity"],
            "assessmentCriteria": {
                "fluencyCoherence": "Maintain smooth conversational flow when discussing transit infrastructure and dream destinations.",
                "lexicalResource": "Mobility and travel lexicon: 'subterranean metro network', 'punctuality index', 'panoramic landscape views'.",
                "grammaticalRange": "Accurate conditionals ('If the high-speed rail network were expanded, I would commute far more frequently').",
                "pronunciation": "Precise word stress on complex multisyllabic terms ('transportation', 'reliability', 'infrastructure')."
            }
        }
    },
    {
        "id": "spk-part1-07",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Domestic Environmental Habits & Recycling",
        "topic": "Environmental Stewardship & Domestic Habits",
        "speakingTask": {
            "part": 1,
            "topic": "Domestic Sustainability",
            "part1Questions": [
                {"questionNumber": 25, "question": "Do you systematically separate and recycle household waste materials at home?"},
                {"questionNumber": 26, "question": "What conscious steps do you take to curtail single-use plastic packaging?"},
                {"questionNumber": 27, "question": "Did your primary school incorporate practical environmental conservation lessons?"},
                {"questionNumber": 28, "question": "Have you ever participated in a collective neighborhood or coastal clean-up initiative?"}
            ],
            "recommendedIdioms": [
                {"phrase": "do my bit", "meaning": "make an individual personal contribution to a collective cause", "example": "Carrying a reusable canvas bag and stainless steel bottle is how I try to do my bit for the environment."},
                {"phrase": "drop in the ocean", "meaning": "a very tiny portion compared to what is truly needed", "example": "Sorting domestic cardboard sometimes feels like a drop in the ocean compared to industrial factory emissions."}
            ],
            "discourseMarkers": ["In our household", "To minimize waste", "Thinking back to my school days", "On a community level"],
            "assessmentCriteria": {
                "fluencyCoherence": "Elaborate with concrete daily examples (composting, canvas bags, recycling bins) without hesitating.",
                "lexicalResource": "Environmental terms: 'biodegradable packaging', 'waste segregation', 'carbon footprint mitigation'.",
                "grammaticalRange": "Balanced coordination using present continuous for ongoing actions and past simple for school memories.",
                "pronunciation": "Natural linking between consonants and vowels ('do my bit for the environment')."
            }
        }
    },
    {
        "id": "spk-part1-08",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "easy",
        "band": "Band 6.0–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Food Traditions, Cooking & Dining Out",
        "topic": "Gastronomy & Cultural Food Traditions",
        "speakingTask": {
            "part": 1,
            "topic": "Food Traditions & Culinary Habits",
            "part1Questions": [
                {"questionNumber": 29, "question": "Do you prefer preparing home-cooked meals or dining at restaurants?"},
                {"questionNumber": 30, "question": "What traditional culinary specialty is your hometown or region renowned for?"},
                {"questionNumber": 31, "question": "Did you learn how to cook from family members or through online tutorials?"},
                {"questionNumber": 32, "question": "Are you adventurous when it comes to sampling unfamiliar international cuisines?"}
            ],
            "recommendedIdioms": [
                {"phrase": "comfort food", "meaning": "traditional food that provides a nostalgic or emotional feeling of well-being", "example": "My grandmother's slow-simmered beef noodle soup is the ultimate comfort food after a tiring week."},
                {"phrase": "acquired taste", "meaning": "something that one learns to appreciate and enjoy only over time", "example": "Fermented soybean dishes are certainly an acquired taste, but I've grown to love them."}
            ],
            "discourseMarkers": ["Without hesitation", "In terms of local cuisine", "I learned primarily by", "When it comes to trying new dishes"],
            "assessmentCriteria": {
                "fluencyCoherence": "Describe aromas, flavors, and cooking procedures with rich adjectives and lively pacing.",
                "lexicalResource": "Sensory and culinary terms: 'savory broth', 'authentic regional seasoning', 'culinary heritage'.",
                "grammaticalRange": "Effective use of past continuous ('While watching my mother prepare...') and conditional structures.",
                "pronunciation": "Accurate stress on compound nouns and descriptive adjectives."
            }
        }
    },
    {
        "id": "spk-part1-09",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Photography, Visual Memories & Social Media",
        "topic": "Photography & Visual Culture",
        "speakingTask": {
            "part": 1,
            "topic": "Photography & Memory",
            "part1Questions": [
                {"questionNumber": 33, "question": "How frequently do you use your smartphone camera to capture everyday moments?"},
                {"questionNumber": 34, "question": "Do you prefer printing physical photograph albums or storing images on cloud servers?"},
                {"questionNumber": 35, "question": "Do you enjoy having your photograph taken by other people?"},
                {"questionNumber": 36, "question": "Do you feel people take too many photos of their food instead of savoring the meal?"}
            ],
            "recommendedIdioms": [
                {"phrase": "in the blink of an eye", "meaning": "occurring extremely rapidly in a split second", "example": "Life moves so quickly in the blink of an eye, so taking photos helps preserve precious memories."},
                {"phrase": "live in the moment", "meaning": "focus on enjoying present reality rather than recording it for later", "example": "Sometimes people become so obsessed with capturing Instagram clips that they forget to live in the moment."}
            ],
            "discourseMarkers": ["To be honest", "I'm the type of person who", "From a nostalgic standpoint", "That's a very common complaint"],
            "assessmentCriteria": {
                "fluencyCoherence": "Express balanced viewpoints on the psychology of modern smartphone photography smoothly.",
                "lexicalResource": "Photography terms: 'high-resolution digital sensors', 'tangible photo album', 'candid snapshot'.",
                "grammaticalRange": "Employ complex contrastive clauses ('While digital cloud storage is convenient, physical albums possess a unique warmth').",
                "pronunciation": "Natural phrasing and communicative pause placement."
            }
        }
    },
    {
        "id": "spk-part1-10",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "easy",
        "band": "Band 6.0–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Weather, Seasonal Cycles & Daily Productivity",
        "topic": "Meteorology & Personal Productivity",
        "speakingTask": {
            "part": 1,
            "topic": "Weather & Seasons",
            "part1Questions": [
                {"questionNumber": 37, "question": "What is your favorite season of the year, and what makes it special to you?"},
                {"questionNumber": 38, "question": "Does gloomy or rainy weather noticeably impact your mood and intellectual focus?"},
                {"questionNumber": 39, "question": "How do you cope with extreme summer heat or harsh winter cold in your city?"},
                {"questionNumber": 40, "question": "Have you noticed any noticeable shifts in regional weather patterns in recent years?"}
            ],
            "recommendedIdioms": [
                {"phrase": "under the weather", "meaning": "feeling slightly unwell, lethargic, or out of sorts", "example": "Prolonged gray and overcast winter days always make me feel a bit under the weather."},
                {"phrase": "breath of fresh air", "meaning": "something pleasantly new, invigorating, and refreshing", "example": "The crisp cool breeze of early autumn is an absolute breath of fresh air after a sweltering summer."}
            ],
            "discourseMarkers": ["Hands down, my favorite is", "It undeniably has a psychological effect", "To cope with the heat", "Over the past few years"],
            "assessmentCriteria": {
                "fluencyCoherence": "Provide cohesive multi-turn answers explaining sensory and psychological reactions to seasonal shifts.",
                "lexicalResource": "Weather and psychological vocabulary: 'sweltering humidity', 'crisp autumnal atmosphere', 'seasonal affective lethargy'.",
                "grammaticalRange": "Mastery of zero and first conditionals ('Whenever the weather turns gloomy, my productivity tends to dip').",
                "pronunciation": "Expressive intonation highlighting mood contrasts."
            }
        }
    },
    {
        "id": "spk-part1-11",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 6.5–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Music, Concert Experiences & Concentration",
        "topic": "Music & Performing Arts",
        "speakingTask": {
            "part": 1,
            "topic": "Music & Soundtracks",
            "part1Questions": [
                {"questionNumber": 41, "question": "What genres of music do you listen to most frequently during the day?"},
                {"questionNumber": 42, "question": "Can you listen to vocal music while studying, or do you require complete silence?"},
                {"questionNumber": 43, "question": "Have you ever attended a large-scale live concert or outdoor musical festival?"},
                {"questionNumber": 44, "question": "Did you ever learn to play a musical instrument during childhood?"}
            ],
            "recommendedIdioms": [
                {"phrase": "music to my ears", "meaning": "news or information that is extremely pleasant to hear", "example": "Hearing that my favorite indie band was touring my home city was absolute music to my ears."},
                {"phrase": "strike a chord", "meaning": "evoke a strong emotional reaction, sympathy, or connection", "example": "The melancholic melody of that acoustic cello piece really struck a chord with me."}
            ],
            "discourseMarkers": ["My musical tastes span", "When it comes to studying", "The live atmosphere was", "Looking back on my school years"],
            "assessmentCriteria": {
                "fluencyCoherence": "Speak fluidly with personalized anecdotes regarding concerts, instruments, or focus habits.",
                "lexicalResource": "Acoustic and performance vocabulary: 'instrumental ambient tracks', 'electric stadium atmosphere', 'rhythmic precision'.",
                "grammaticalRange": "Accurate past perfect constructions ('Before I entered high school, I had taken classical piano lessons for five years').",
                "pronunciation": "Rhythmic, confident delivery with natural word stress."
            }
        }
    },
    {
        "id": "spk-part1-12",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "easy",
        "band": "Band 6.0–7.5",
        "granularity": "drill",
        "title": "Speaking Part 1: Social Life, Friendships & Maintaining Contact",
        "topic": "Interpersonal Relationships & Social Networks",
        "speakingTask": {
            "part": 1,
            "topic": "Friendship & Social Connections",
            "part1Questions": [
                {"questionNumber": 45, "question": "Do you prefer maintaining a large social circle or a small group of intimate friends?"},
                {"questionNumber": 46, "question": "How do you stay in touch with childhood friends who reside in different cities?"},
                {"questionNumber": 47, "question": "What qualities do you value most deeply in a genuine friendship?"},
                {"questionNumber": 48, "question": "Do you find it effortless or challenging to forge new friendships in adult life?"}
            ],
            "recommendedIdioms": [
                {"phrase": "through thick and thin", "meaning": "supporting someone through both favorable and extremely challenging times", "example": "My closest university friends have stood by me through thick and thin over the past decade."},
                {"phrase": "see eye to eye", "meaning": "agree completely with someone on foundational values", "example": "Even if we don't see eye to eye on every minor detail, our core ethical principles are identical."}
            ],
            "discourseMarkers": ["I'm definitely inclined toward", "Even though distance separates us", "Above all else, I value", "In adult life, it's certainly more"],
            "assessmentCriteria": {
                "fluencyCoherence": "Articulate interpersonal values thoughtfully without hesitation or search for basic words.",
                "lexicalResource": "Psychological and social lexicon: 'unwavering loyalty', 'reciprocal emotional support', 'superficial acquaintances'.",
                "grammaticalRange": "Skilled use of comparative structures and participial clauses.",
                "pronunciation": "Warm, authentic conversational cadence."
            }
        }
    },

    # =========================================================================
    # PART 2 CUE CARDS + PART 3 IN-DEPTH DISCUSSION (8 Test Modules)
    # =========================================================================
    {
        "id": "spk-full-01",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 7.0–8.5",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: Community Environmental Initiative & Climate Action",
        "topic": "Environmental Stewardship & Civic Responsibility",
        "speakingTask": {
            "part": 2,
            "topic": "Environmental Project & Climate Responsibility",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe an environmental initiative or project in your community that you know about or participated in.",
                "bulletPoints": [
                    "What this environmental initiative or project was",
                    "Who organized and participated in the activities",
                    "What specific environmental actions were undertaken",
                    "And explain why you felt this initiative was beneficial or impactful"
                ],
                "roundingOffQuestion": "Do you believe more local residents will volunteer for similar projects in the future?"
            },
            "part3Questions": [
                {"questionNumber": 1, "question": "Should environmental protection be primarily enforced through government legislation or voluntary civic action?", "promptNote": "Consider legal penalties, corporate regulation vs grass-roots community culture."},
                {"questionNumber": 2, "question": "How effective are international climate accords when member nations fail to meet carbon reduction targets?", "promptNote": "Examine sovereignty, diplomatic pressure, and economic trade-offs."},
                {"questionNumber": 3, "question": "What practical methodologies can primary schools employ to cultivate lifelong ecological habits in children?", "promptNote": "Discuss hands-on composting, school gardens vs textbook theory."},
                {"questionNumber": 4, "question": "Do you believe commercial businesses promote sustainability out of genuine ethical concern or as a marketing tactic?", "promptNote": "Analyze corporate greenwashing versus authentic circular economy practices."}
            ],
            "recommendedIdioms": [
                {"phrase": "lead by example", "meaning": "influence others through one's own positive, ethical behavior", "example": "By organizing weekend mangrove planting drives, local youth leaders were able to lead by example."},
                {"phrase": "at the eleventh hour", "meaning": "at the very last possible moment before catastrophe", "example": "Global governments cannot afford to implement climate remediation at the eleventh hour."}
            ],
            "discourseMarkers": ["To delve into the specifics", "What struck me most was", "Looking at the macroeconomic picture", "Fundamentally speaking"],
            "assessmentCriteria": {
                "fluencyCoherence": "Structure the 2-minute cue card logically across all four bullet points; in Part 3, deliver balanced academic arguments examining contrasting viewpoints.",
                "lexicalResource": "Advanced environmental policy terms: 'grassroots mobilization', 'biodiversity restoration', 'corporate greenwashing', 'circular economy'.",
                "grammaticalRange": "Seamless integration of mixed conditionals, passive constructions, and complex relative clauses.",
                "pronunciation": "Accurate sentence stress highlighting key logical contrasts."
            }
        }
    },
    {
        "id": "spk-full-02",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: Resolving a Complex Problem & Critical Thinking",
        "topic": "Problem-Solving & Intellectual Resilience",
        "speakingTask": {
            "part": 2,
            "topic": "Intellectual Problem Solving & Critical Thinking",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe a challenging intellectual, academic, or technical problem that you managed to resolve.",
                "bulletPoints": [
                    "What the specific problem or dilemma was",
                    "When and where you encountered this challenge",
                    "What analytical steps or strategies you deployed to solve it",
                    "And explain why resolving this issue gave you a profound sense of satisfaction"
                ],
                "roundingOffQuestion": "Did you require assistance from colleagues or mentors during the process?"
            },
            "part3Questions": [
                {"questionNumber": 5, "question": "Why do educational institutions often struggle to teach lateral thinking and practical problem-solving?", "promptNote": "Contrast standardized testing and rote memorization with open-ended inquiry."},
                {"questionNumber": 6, "question": "To what extent will generative AI tools erode humans' organic capacity for deep critical thinking?", "promptNote": "Examine cognitive offloading versus augmented human analytical speed."},
                {"questionNumber": 7, "question": "How important is experiencing constructive failure during childhood in developing adult emotional resilience?", "promptNote": "Discuss overprotective parenting ('helicopter parenting') versus grit."},
                {"questionNumber": 8, "question": "Should high-stakes public policy decisions be governed purely by data-driven algorithms or human moral intuition?", "promptNote": "Weigh quantitative utilitarian optimization against human ethics and compassion."}
            ],
            "recommendedIdioms": [
                {"phrase": "think outside the box", "meaning": "approach problems from an unconventional, creative perspective", "example": "When conventional debugging methods failed, we had to think outside the box to trace the software memory leak."},
                {"phrase": "teething troubles", "meaning": "minor initial difficulties experienced when starting a new project", "example": "Despite some early teething troubles, the automated inventory pipeline was eventually a resounding success."}
            ],
            "discourseMarkers": ["Initially, the obstacle appeared insurmountable", "My breakthrough occurred when", "From an educational standpoint", "There is a profound distinction between"],
            "assessmentCriteria": {
                "fluencyCoherence": "Deliver an engaging chronological narrative for Part 2 and authoritative analytical responses in Part 3.",
                "lexicalResource": "Cognitive and analytical vocabulary: 'systematic root-cause analysis', 'cognitive offloading', 'heuristic approach', 'paradigmatic shift'.",
                "grammaticalRange": "Sophisticated deployment of past perfect continuous, cleft sentences ('What proved decisive was...'), and conditional inversions.",
                "pronunciation": "Flawless prosody with natural pauses between conceptual clauses."
            }
        }
    },
    {
        "id": "spk-full-03",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 7.0–8.5",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: Historic Architecture & Cultural Heritage Preservation",
        "topic": "Architecture, History & Urban Development",
        "speakingTask": {
            "part": 2,
            "topic": "Historic Monuments & Urban Heritage",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe an important historical building, monument, or architectural heritage site you have visited.",
                "bulletPoints": [
                    "Where the historic structure is situated and when you visited it",
                    "What architectural features and historic period it represents",
                    "What historical events or cultural traditions are associated with it",
                    "And explain what profound impression or feeling the site left on you"
                ],
                "roundingOffQuestion": "Is the monument well maintained by local conservation authorities?"
            },
            "part3Questions": [
                {"questionNumber": 9, "question": "How should municipal city planners balance historical architectural preservation against the demand for modern commercial skyscrapers?", "promptNote": "Discuss adaptive reuse of heritage buildings vs urban housing density."},
                {"questionNumber": 10, "question": "Does mass tourism generate sufficient revenue to maintain historic sites, or does it cause unsustainable physical degradation?", "promptNote": "Evaluate foot-traffic erosion, entry fees, and conservation quotas."},
                {"questionNumber": 11, "question": "Should national governments allocate substantial taxpayer funds to preserve ancient monuments during times of economic hardship?", "promptNote": "Examine national cultural identity vs immediate public services like healthcare."},
                {"questionNumber": 12, "question": "Why do younger generations often exhibit less interest in visiting traditional historical landmarks?", "promptNote": "Consider virtual interactive exhibits, gamified history vs passive plaques."}
            ],
            "recommendedIdioms": [
                {"phrase": "stand the test of time", "meaning": "remain durable, respected, and relevant over centuries", "example": "The medieval cathedral's gothic stonework has truly stood the test of time."},
                {"phrase": "steeped in history", "meaning": "permeated and surrounded by rich historical legacy", "example": "Walking through the cobblestone alleys of Kyoto felt like stepping into a realm steeped in history."}
            ],
            "discourseMarkers": ["Upon entering the sanctuary", "What caught my eye immediately", "In the realm of urban planning", "It boils down to the question of"],
            "assessmentCriteria": {
                "fluencyCoherence": "Evocative, descriptive narration in Part 2 coupled with balanced socio-economic debate in Part 3.",
                "lexicalResource": "Architectural and heritage terminology: 'soaring vaulted ceilings', 'adaptive reuse', 'cultural commodification', 'aesthetic legacy'.",
                "grammaticalRange": "Mastery of past continuous, passive constructions, and complex comparative clauses.",
                "pronunciation": "Rich, resonant intonation matching the grandeur of the architectural topic."
            }
        }
    },
    {
        "id": "spk-full-04",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 7.0–8.0",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: An Influential Educator & The Future of Teaching",
        "topic": "Pedagogy, Mentorship & Education Technology",
        "speakingTask": {
            "part": 2,
            "topic": "Mentorship & Educational Evolution",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe an influential teacher, lecturer, or mentor who had a profound impact on your academic or personal life.",
                "bulletPoints": [
                    "Who this educator was and what academic subject they taught",
                    "What specific pedagogical methods or personal qualities set them apart",
                    "How they supported or guided you during a challenging period",
                    "And explain why their mentorship exerted such a lasting influence on your development"
                ],
                "roundingOffQuestion": "Do you still maintain contact with this teacher today?"
            },
            "part3Questions": [
                {"questionNumber": 13, "question": "What pedagogical qualities distinguish truly inspirational educators from merely competent classroom instructors?", "promptNote": "Examine emotional empathy, passion for the subject, and individualized feedback."},
                {"questionNumber": 14, "question": "Can automated AI tutoring systems ever fully replicate the emotional mentorship provided by human teachers?", "promptNote": "Consider personalized pacing algorithms vs human pastoral care and moral encouragement."},
                {"questionNumber": 15, "question": "Why has the socioeconomic status and prestige of the teaching profession declined in many Western nations?", "promptNote": "Discuss wage stagnation, administrative burdens, and political polarization of curriculums."},
                {"questionNumber": 16, "question": "Should teachers' salaries be directly tied to their students' standardized examination test scores?", "promptNote": "Debate merit-based pay vs teaching to the test and penalizing teachers in disadvantaged schools."}
            ],
            "recommendedIdioms": [
                {"phrase": "go the extra mile", "meaning": "make an exceptional effort beyond what is strictly expected", "example": "Dr. Anderson would always go the extra mile, offering supplementary evening tutorials for struggling students."},
                {"phrase": "open doors", "meaning": "provide valuable opportunities that were previously inaccessible", "example": "Her recommendation letter truly opened doors for my postgraduate scholarship application."}
            ],
            "discourseMarkers": ["First and foremost", "What truly distinguished her was", "From a pedagogical perspective", "I would argue forcefully that"],
            "assessmentCriteria": {
                "fluencyCoherence": "Speak with genuine passion and smooth transitions during the cue card; argue educational policy cogently in Part 3.",
                "lexicalResource": "Pedagogical vocabulary: 'transformative mentorship', 'pastoral care', 'differentiated instruction', 'cognitive scaffold'.",
                "grammaticalRange": "Fluent use of past habits ('He would frequently challenge us to...'), non-restrictive relative clauses, and counterfactual conditionals.",
                "pronunciation": "Warm, engaging vocal modulation conveying personal gratitude and respect."
            }
        }
    },
    {
        "id": "spk-full-05",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 7.0–8.0",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: An Unexpected Travel Delay & Urban Commuting",
        "topic": "Transportation Networks & Work-Life Balance",
        "speakingTask": {
            "part": 2,
            "topic": "Travel Delays & Commuter Well-being",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe an unexpected journey or trip that took significantly longer than originally planned.",
                "bulletPoints": [
                    "Where you were traveling to and what mode of transport you were using",
                    "Why the delay, breakdown, or detour occurred",
                    "What you and other passengers did while waiting",
                    "And explain how you felt when you finally reached your destination"
                ],
                "roundingOffQuestion": "Did this incident alter how you plan future long-distance journeys?"
            },
            "part3Questions": [
                {"questionNumber": 17, "question": "How does excessive daily commuting time impact workers' psychological well-being and domestic family relationships?", "promptNote": "Examine chronic stress, sleep deprivation, and lost leisure time."},
                {"questionNumber": 18, "question": "Should national governments prioritize investing in high-speed rail corridors over expanding regional domestic aviation?", "promptNote": "Compare carbon footprint, door-to-door transit speed, and capital construction costs."},
                {"questionNumber": 19, "question": "To what extent can remote working arrangements resolve metropolitan traffic bottlenecks permanently?", "promptNote": "Analyze hybrid work models vs lingering delivery/service vehicle congestion."},
                {"questionNumber": 20, "question": "Why do many modern commuters experience severe anxiety when separated from smartphone connectivity during travel delays?", "promptNote": "Discuss smartphone dependency, FOMO (fear of missing out), and lack of real-time transit updates."}
            ],
            "recommendedIdioms": [
                {"phrase": "at a standstill", "meaning": "completely stopped with zero movement", "example": "Following the freight truck collision, highway traffic was brought to a complete standstill for four hours."},
                {"phrase": "silver lining", "meaning": "a comforting or beneficial aspect to an otherwise dismal situation", "example": "The silver lining of the train breakdown was that I ended up having a fascinating conversation with an elderly author."}
            ],
            "discourseMarkers": ["As luck would have it", "To make matters worse", "When looking at urban sociology", "The crux of the matter is"],
            "assessmentCriteria": {
                "fluencyCoherence": "Maintain narrative suspense during the delay recount; structure Part 3 responses around clear public transport economics.",
                "lexicalResource": "Transit terminology: 'severe mechanical fault', 'transit corridor', 'gridlock', 'psychological fatigue'.",
                "grammaticalRange": "Accurate coordination of narrative tenses (past simple, past continuous, past perfect).",
                "pronunciation": "Vocal pacing that accelerates during narrative tension and slows during calm reflection."
            }
        }
    },
    {
        "id": "spk-full-06",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "advanced",
        "band": "Band 7.5–8.5",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: Making a Difficult Decision & Ethical Judgment",
        "topic": "Ethics, Decision-Making & Life Choices",
        "speakingTask": {
            "part": 2,
            "topic": "Decision-Making & Ethical Dilemmas",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe a difficult personal, academic, or professional decision you had to make.",
                "bulletPoints": [
                    "What the decision was and what conflicting choices you weighed",
                    "When you had to make this choice and why it was challenging",
                    "Who you consulted for advice or guidance during your deliberation",
                    "And explain why you feel you made the right (or wrong) decision in hindsight"
                ],
                "roundingOffQuestion": "Do you generally find it easy or stressful to make major life choices?"
            },
            "part3Questions": [
                {"questionNumber": 21, "question": "Why do individuals in modern affluent societies suffer from acute 'decision fatigue'?", "promptNote": "Examine the paradox of choice, consumer abundance, and social media comparison."},
                {"questionNumber": 22, "question": "Should young adults make critical career decisions independently, or defer to their parents' traditional wishes?", "promptNote": "Contrast filial piety/familial expectations with personal passion and modern labor dynamics."},
                {"questionNumber": 23, "question": "What psychological strategies can leaders adopt to make sound decisions under extreme crisis conditions?", "promptNote": "Discuss emotional detachment, pre-mortem analysis, and consulting diverse advisory teams."},
                {"questionNumber": 24, "question": "In the future, will humans willingly outsource moral and ethical life decisions to algorithmic AI advisors?", "promptNote": "Weigh objective probabilistic optimization against human conscience and accountability."}
            ],
            "recommendedIdioms": [
                {"phrase": "at a crossroads", "meaning": "at a decisive turning point requiring a critical life choice", "example": "After completing my undergraduate degree, I found myself standing at a major career crossroads."},
                {"phrase": "weigh the pros and cons", "meaning": "carefully compare positive and negative attributes of opposing options", "example": "I spent several sleepless nights weighing the pros and cons of moving overseas for work."}
            ],
            "discourseMarkers": ["I was caught in two minds", "After much soul-searching", "From a psychological perspective", "When faced with ethical ambiguity"],
            "assessmentCriteria": {
                "fluencyCoherence": "Demonstrate mature, introspective reasoning in Part 2 and philosophical depth in Part 3.",
                "lexicalResource": "Psychological and philosophical lexicon: 'paradox of choice', 'filial expectations', 'pre-mortem analysis', 'cognitive dissonance'.",
                "grammaticalRange": "Proficient deployment of mixed counterfactual conditionals ('Had I not accepted that internship, my career would look entirely different today').",
                "pronunciation": "Thoughtful, measured delivery with natural emphatic pauses."
            }
        }
    },
    {
        "id": "spk-full-07",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 7.0–8.0",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: Cultural Festivals & Globalization",
        "topic": "Cultural Anthropology, Festivals & Globalization",
        "speakingTask": {
            "part": 2,
            "topic": "Cultural Festivals & Indigenous Heritage",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe a traditional cultural festival or communal celebration in your country that is meaningful to you.",
                "bulletPoints": [
                    "What the festival commemorates and when it takes place",
                    "What traditional foods, music, or rituals are central to the celebration",
                    "Who you usually celebrate this cultural occasion with",
                    "And explain why this festival holds enduring emotional or cultural significance for your community"
                ],
                "roundingOffQuestion": "Do many international tourists travel to your country to witness this celebration?"
            },
            "part3Questions": [
                {"questionNumber": 25, "question": "How is economic globalization eroding indigenous cultural festivals in non-Western societies?", "promptNote": "Discuss cultural homogenization, Western holiday adoption (Halloween/Christmas) vs local customs."},
                {"questionNumber": 26, "question": "Does commercial corporate sponsorship compromise the sacred or authentic meaning of traditional celebrations?", "promptNote": "Examine commercialization, retail sales spikes vs preserving authentic rituals."},
                {"questionNumber": 27, "question": "What innovative strategies can governments implement to inspire younger generations to embrace traditional folk heritage?", "promptNote": "Consider digital cultural storytelling, youth folk ensembles, and school holiday integration."},
                {"questionNumber": 28, "question": "Can experiencing foreign cultural festivals foster genuine diplomatic peace and intercultural empathy between nations?", "promptNote": "Evaluate cultural diplomacy, shared human values vs superficial tourist consumption."}
            ],
            "recommendedIdioms": [
                {"phrase": "pass the torch", "meaning": "transfer ancient traditions, knowledge, or responsibility to younger generations", "example": "During the harvest festival, elders ritually pass the torch by teaching ancient folk songs to local children."},
                {"phrase": "melt in your mouth", "meaning": "food that is extraordinarily tender, delicate, and flavorful", "example": "The traditional honey-glazed pastries served during the festival literally melt in your mouth."}
            ],
            "discourseMarkers": ["Dating back centuries", "The hallmark of the celebration is", "In an increasingly globalized world", "There is an inherent risk that"],
            "assessmentCriteria": {
                "fluencyCoherence": "Paint a vibrant sensory picture of communal rituals in Part 2; analyze cultural globalization critically in Part 3.",
                "lexicalResource": "Anthropological terms: 'communal solidarity', 'cultural homogenization', 'generational transmission', 'sacred heritage'.",
                "grammaticalRange": "Complex sentences combining participial phrases ('Having been celebrated for over five hundred years...') with passive forms.",
                "pronunciation": "Rhythmic, engaging delivery that conveys cultural pride and warmth."
            }
        }
    },
    {
        "id": "spk-full-08",
        "skill": "speaking",
        "questionType": "speaking_task",
        "difficulty": "medium",
        "band": "Band 7.0–8.0",
        "granularity": "section",
        "title": "Speaking Part 2 & 3: An Indispensable Smart Device & Digital Ethics",
        "topic": "Consumer Electronics, Digital Ethics & Privacy",
        "speakingTask": {
            "part": 2,
            "topic": "Smart Technology & Algorithmic Dependence",
            "preparationSeconds": 60,
            "speakingSeconds": 120,
            "cueCard": {
                "title": "Describe an electronic smart device, software application, or piece of technology that you find indispensable in everyday life.",
                "bulletPoints": [
                    "What this specific technological device or software tool is",
                    "How frequently you rely upon it throughout a typical day",
                    "What key functionalities or tasks it performs for you",
                    "And explain why your daily routine would be severely disrupted without it"
                ],
                "roundingOffQuestion": "Do you anticipate replacing or upgrading this technology in the near future?"
            },
            "part3Questions": [
                {"questionNumber": 29, "question": "How has algorithmic reliance on smartphones altered human memory retention and navigational spatial skills?", "promptNote": "Examine GPS dependency, digital amnesia ('Google effect') vs freeing mental bandwidth."},
                {"questionNumber": 30, "question": "What measures can societies adopt to prevent elderly citizens from being marginalized by rapid technological obsolescence?", "promptNote": "Discuss community digital literacy workshops, analog customer service mandates."},
                {"questionNumber": 31, "question": "Should tech conglomerates be legally prohibited from utilizing persuasive algorithmic designs that cultivate screen addiction in minors?", "promptNote": "Debate ethical technology design, infinite scrolling bans vs parental responsibility."},
                {"questionNumber": 32, "question": "Are modern consumers trading away too much biometric and personal data privacy in exchange for digital convenience?", "promptNote": "Weigh targeted algorithmic convenience against corporate surveillance capitalism."}
            ],
            "recommendedIdioms": [
                {"phrase": "second nature", "meaning": "something practiced so frequently that it is executed automatically without conscious effort", "example": "Navigating my productivity apps has become absolute second nature to me."},
                {"phrase": "at your fingertips", "meaning": "immediately accessible and ready for instant use", "example": "Having global satellite navigation right at your fingertips has fundamentally changed how we explore unfamiliar cities."}
            ],
            "discourseMarkers": ["I rely on it incessantly", "To be completely candid", "Looking at the cognitive ramifications", "It raises profound ethical questions regarding"],
            "assessmentCriteria": {
                "fluencyCoherence": "Demonstrate seamless transitions between daily practical usage (Part 2) and societal technology critiques (Part 3).",
                "lexicalResource": "Technological and ethical terminology: 'surveillance capitalism', 'digital amnesia', 'persuasive design algorithms', 'spatial awareness'.",
                "grammaticalRange": "Proficient use of cleft sentences ('What concerns me most is...'), modal verbs, and gerund subjects.",
                "pronunciation": "Crisp enunciation of technical jargon and natural connected speech."
            }
        }
    }
]
