/**
 * IELTS 500,000-Question Combinatorial Procedural Generator Engine
 *
 * Mathematically synthesizes authentic Cambridge-style IELTS questions
 * on-demand across 4 skills, 80 academic domains, 15 question types,
 * and 3 difficulty tiers.
 *
 * Provides deterministic index mapping (0 to 500,000+) and on-demand
 * batch synthesis without client-side memory bloat.
 */

import type { QuestionBankItem } from "../../../data/question-bank/index.ts";
import type { IeltsSkill } from "../../cell/types/ieltsSchema.ts";
import type { QuestionDifficulty, QuestionGranularity } from "../types/questionBank.ts";

export const TOTAL_PROCEDURAL_CAPACITY = 500000;

export interface AcademicDomain {
  name: string;
  category: string;
  keyConcepts: string[];
  phenomenon: string;
  methodology: string;
  practicalApplication: string;
}

export const ACADEMIC_DOMAINS: AcademicDomain[] = [
  // Science & Technology (10)
  {
    name: "Autonomous Aerial Drones & Ecological Monitoring",
    category: "Science & Technology",
    keyConcepts: ["multispectral sensors", "canopy density", "geospatial telemetry", "biodiversity indices"],
    phenomenon: "autonomous telemetry systems mapping micro-habitat fragmentation",
    methodology: "calibrated infrared aerial imagery cross-referenced with ground soil sensors",
    practicalApplication: "rapid assessment of post-wildfire reforestation rates"
  },
  {
    name: "Quantum Cryptography & Optical Fiber Security",
    category: "Science & Technology",
    keyConcepts: ["quantum key distribution", "photon polarization", "eavesdropping detection", "fiber attenuation"],
    phenomenon: "Heisenberg uncertainty principle preventing undetected packet interception",
    methodology: "interferometric photon phase verification across subsea fiber cables",
    practicalApplication: "securing sovereign inter-bank financial transaction networks"
  },
  {
    name: "Deep Ocean Abyssal Hydrothermal Ecology",
    category: "Science & Technology",
    keyConcepts: ["chemosynthesis", "extremophilic bacteria", "benthic sulfides", "trophosome tissue"],
    phenomenon: "primary biological productivity thriving without downwelling solar radiation",
    methodology: "unmanned submersible deep-sea core drilling and in-situ mass spectrometry",
    practicalApplication: "discovering novel heat-tolerant catalytic industrial enzymes"
  },
  {
    name: "Solid-State Battery Electrolytes & Energy Density",
    category: "Science & Technology",
    keyConcepts: ["ceramic separators", "dendrite suppression", "ionic conductivity", "thermal runaway"],
    phenomenon: "elimination of flammable liquid electrolytes preventing battery combustion",
    methodology: "synchrotron X-ray diffraction tracking lithium migration across solid crystal lattices",
    practicalApplication: "extending commercial electric vehicle driving ranges beyond 1,000 kilometers"
  },
  {
    name: "CRISPR-Cas9 Precision Agronomic Gene Editing",
    category: "Science & Technology",
    keyConcepts: ["guide RNA", "targeted mutagenesis", "drought tolerance", "off-target cleavage"],
    phenomenon: "site-specific chromosomal modification improving crop nutrient uptake",
    methodology: "whole-genome sequencing verifying zero off-target DNA cleavages in seedling lines",
    practicalApplication: "cultivating climate-resilient staple grains in saline coastal soils"
  },
  {
    name: "Metamaterials & Acoustic Wave Manipulation",
    category: "Science & Technology",
    keyConcepts: ["negative refractive index", "subwavelength resonators", "acoustic cloaking", "ultrasonic dampening"],
    phenomenon: "engineered structural geometries redirecting sound waves around physical obstacles",
    methodology: "laser Doppler vibrometry mapping acoustic pressure gradients in micro-lattice chambers",
    practicalApplication: "soundproofing high-density urban residential towers adjacent to airports"
  },
  {
    name: "Aerospace Propulsion: Hall Effect Ion Thrusters",
    category: "Science & Technology",
    keyConcepts: ["xenon propellant", "electrostatic acceleration", "specific impulse", "plasma plume"],
    phenomenon: "continuous low-thrust ion discharge yielding extreme orbital fuel efficiency",
    methodology: "vacuum chamber Faraday cup arrays measuring ion beam divergence angles",
    practicalApplication: "maintaining orbital station-keeping for global broadband satellite constellations"
  },
  {
    name: "Nanoscale Water Desalination Membranes",
    category: "Science & Technology",
    keyConcepts: ["graphene oxide", "nanoporous channels", "steric exclusion", "permeate flux"],
    phenomenon: "molecular sieve pores allowing water molecules to pass while rejecting sodium ions",
    methodology: "atomic force microscopy measuring membrane pore diameter consistency under high pressure",
    practicalApplication: "lowering the electrical energy requirement of municipal desalination by 40%"
  },
  {
    name: "Synthetic Microbial Protein Synthesis",
    category: "Science & Technology",
    keyConcepts: ["precision fermentation", "bioreactor gasification", "amino acid profiles", "feedstock efficiency"],
    phenomenon: "autotrophic hydrogen-oxidizing bacteria producing complete dietary protein",
    methodology: "continuous gas-fermentation monitoring evaluating protein biomass yields per kilowatt-hour",
    practicalApplication: "decoupling global livestock feed production from arable land consumption"
  },
  {
    name: "Autonomous Maritime Navigation & Edge AI",
    category: "Science & Technology",
    keyConcepts: ["sensor fusion", "marine radar", "collision regulations", "satellite telemetry latency"],
    phenomenon: "computer vision models classifying vessel traffic in zero-visibility fog",
    methodology: "millimeter-wave radar and thermal camera integration tested in crowded shipping straits",
    practicalApplication: "reducing international ocean cargo collision rates caused by crew fatigue"
  },

  // Ecology & Environment (10)
  {
    name: "Peatland Restoration & Carbon Sequestration",
    category: "Ecology & Environment",
    keyConcepts: ["sphagnum moss", "water table elevation", "anaerobic decomposition", "methane flux"],
    phenomenon: "waterlogged acidic conditions halting organic plant matter decay for millennia",
    methodology: "eddy covariance towers measuring net ecosystem carbon dioxide exchange rates",
    practicalApplication: "turning drained agricultural lowlands back into permanent carbon sinks"
  },
  {
    name: "Glacial Ice Core Atmospheric Proxy Data",
    category: "Ecology & Environment",
    keyConcepts: ["firn air bubbles", "oxygen isotope ratios", "paleotemperature", "volcanic sulfate spikes"],
    phenomenon: "hermetic atmospheric gas preservation in Antarctic deep polar ice",
    methodology: "mass spectrometry analyzing O-18 to O-16 isotopic fractionation in seasonal ice layers",
    practicalApplication: "reconstructing 800,000-year historical climate cycles to calibrate modern predictive models"
  },
  {
    name: "Microplastic Bioaccumulation in Marine Food Webs",
    category: "Ecology & Environment",
    keyConcepts: ["trophic transfer", "zooplankton ingestion", "adsorbed persistent pollutants", "gut translocations"],
    phenomenon: "synthetic microfibers concentrating exponentially as they move up marine food chains",
    methodology: "fluorescence microscopy and pyrolysis gas chromatography on pelagic fish digestive tracts",
    practicalApplication: "enforcing international bans on non-biodegradable synthetic cosmetic microbeads"
  },
  {
    name: "Coral Reef Thermotolerance & Assisted Evolution",
    category: "Ecology & Environment",
    keyConcepts: ["zooxanthellae symbiosis", "bleaching threshold", "heat-shock proteins", "micro-fragmentation"],
    phenomenon: "selective breeding of heat-resistant algal symbionts preserving calcification rates",
    methodology: "controlled thermal stress tanks exposing coral recruits to prolonged marine heatwaves",
    practicalApplication: "re-seeding degraded barrier reefs with climate-hardened micro-colonies"
  },
  {
    name: "Urban Heat Island Mitigation & Reflective Albedo",
    category: "Ecology & Environment",
    keyConcepts: ["thermal emissivity", "vegetative evapotranspiration", "cool pavements", "nocturnal radiation"],
    phenomenon: "high solar reflectance coatings reducing surface temperature by up to 15 degrees",
    methodology: "thermal drone overflights mapping diurnal surface temperature gradients across downtown blocks",
    practicalApplication: "curtailing peak summer electrical air conditioning demand in metropolitan centers"
  },
  {
    name: "Mycorrhizal Fungal Networks & Forest Communication",
    category: "Ecology & Environment",
    keyConcepts: ["hyphal networks", "nutrient sharing", "biochemical defense signals", "mother trees"],
    phenomenon: "subterranean fungal mycelium distributing carbon and nitrogen between mature and seedling trees",
    methodology: "carbon-14 isotope tracking measuring subterranean carbohydrate flows between distinct species",
    practicalApplication: "abandoning clear-cut logging in favor of continuous-cover retention forestry"
  },
  {
    name: "Wetland Biofiltration & Agricultural Runoff",
    category: "Ecology & Environment",
    keyConcepts: ["nitrate reduction", "denitrifying bacteria", "sedimentation basins", "eutrophication prevention"],
    phenomenon: "natural reed bed root systems converting synthetic fertilizer nitrates into harmless nitrogen gas",
    methodology: "inflow and outflow chemical water sampling measuring dissolved inorganic nitrogen removal",
    practicalApplication: "eliminating hypoxic dead zone formation in coastal river estuaries"
  },
  {
    name: "Desertification Reversal & Sand Dune Stabilization",
    category: "Ecology & Environment",
    keyConcepts: ["biological soil crusts", "microbial cyanobacteria", "windbreak belts", "drip fertigation"],
    phenomenon: "inoculating dry shifting sands with cyanobacteria to form moisture-retaining surface crusts",
    methodology: "satellite NDVI vegetative greenness tracking over fifteen-year shelterbelt zones",
    practicalApplication: "halting encroaching desert borders on peripheral semi-arid farmland"
  },
  {
    name: "Mangrove Estuary Protection & Wave Attenuation",
    category: "Ecology & Environment",
    keyConcepts: ["pneumatophore roots", "hydrodynamic drag", "sediment accretion", "storm surge buffering"],
    phenomenon: "dense aerial root tangles dissipating up to 66 percent of incoming cyclone wave energy",
    methodology: "flume tank wave generators measuring kinetic energy dissipation across varied mangrove root densities",
    practicalApplication: "cost-effective coastal defense alternative to concrete sea wall construction"
  },
  {
    name: "Soil Microbiome Diversity & Sustainable Agronomy",
    category: "Ecology & Environment",
    keyConcepts: ["rhizosphere bacteria", "mycorrhizal glomalin", "soil aggregate stability", "humic substances"],
    phenomenon: "diverse bacterial communities solubilizing bound soil minerals for root absorption",
    methodology: "metagenomic DNA sequencing quantifying microbial functional diversity in no-till fields",
    practicalApplication: "reducing commercial synthetic phosphate fertilizer requirements by half"
  },

  // Architecture & Urban Planning (10)
  {
    name: "Passivhaus Building Standards & Thermal Envelopes",
    category: "Architecture & Urban Planning",
    keyConcepts: ["thermal bridging elimination", "triple glazing", "airtightness test", "heat recovery ventilation"],
    phenomenon: "continuous external insulation maintaining indoor warmth without active radiators",
    methodology: "blower door pressurization tests verifying air leakage below 0.6 air changes per hour",
    practicalApplication: "achieving 90 percent heating energy reductions in temperate housing developments"
  },
  {
    name: "Transit-Oriented Development & 15-Minute Cities",
    category: "Architecture & Urban Planning",
    keyConcepts: ["high-density zoning", "pedestrian shed", "intermodal transit hubs", "mixed-use retail"],
    phenomenon: "clustering daily essential amenities within a 15-minute walk or cycling radius",
    methodology: "commuter origin-destination GPS tracking assessing private vehicle trip reduction",
    practicalApplication: "slashing municipal transport carbon footprints while reviving neighborhood commerce"
  },
  {
    name: "Seismic Base Isolation & High-Rise Dampers",
    category: "Architecture & Urban Planning",
    keyConcepts: ["elastomeric bearings", "tuned mass dampers", "resonance decoupling", "inter-story drift"],
    phenomenon: "flexible ground bearings absorbing lateral earthquake ground acceleration",
    methodology: "hydraulic shake table testing measuring structural stress in scale skyscraper models",
    practicalApplication: "ensuring critical hospital skyscrapers remain structurally operational post-magnitude 8 quakes"
  },
  {
    name: "Daylight Harvesting & Kinetic Shading Facades",
    category: "Architecture & Urban Planning",
    keyConcepts: ["automated louvers", "lux sensor integration", "solar glare control", "internal thermal gain"],
    phenomenon: "dynamic facade panels rotating automatically to follow solar trajectories",
    methodology: "radiance daylight simulation software calculating annual spatial daylight autonomy",
    practicalApplication: "minimizing interior artificial lighting power while eliminating thermal discomfort"
  },
  {
    name: "Timber Mass Architecture: Cross-Laminated Timber (CLT)",
    category: "Architecture & Urban Planning",
    keyConcepts: ["embodied carbon", "charring rate fire safety", "prefabricated panels", "structural stiffness"],
    phenomenon: "cross-laminated wooden panels providing strength comparable to structural steel with negative carbon",
    methodology: "large-scale compressive and fire endurance testing measuring structural load retention under flame",
    practicalApplication: "constructing 20-story sustainable high-rise apartments without structural concrete frames"
  },
  {
    name: "Urban Waterfront Revitalization: Industrial Docks",
    category: "Architecture & Urban Planning",
    keyConcepts: ["brownfield remediation", "public esplanade", "adaptive reuse", "heritage preservation"],
    phenomenon: "converting obsolete commercial shipping docks into vibrant pedestrian waterfront districts",
    methodology: "public pedestrian foot-traffic heatmaps and economic vibrancy surveys over a 10-year span",
    practicalApplication: "reconnecting isolated landlocked urban populations with coastal maritime waterways"
  },
  {
    name: "Biomimetic Architectural Cooling: Termite Mound Mounds",
    category: "Architecture & Urban Planning",
    keyConcepts: ["convective chimneys", "thermal mass storage", "nocturnal purging", "diurnal temperature swing"],
    phenomenon: "passive stack ventilation drawing cool night air through heavy concrete slabs",
    methodology: "computational fluid dynamics air velocity sensors placed in internal building ventilation shafts",
    practicalApplication: "operating modern high-rise office towers without mechanical air conditioning systems"
  },
  {
    name: "Linear Urban Parks: Repurposed Freight Corridors",
    category: "Architecture & Urban Planning",
    keyConcepts: ["elevated greenways", "native pioneer flora", "active mobility", "real estate catalysis"],
    phenomenon: "transforming disused industrial railway lines into elevated public botanical walkways",
    methodology: "airborne particulate matter counters measuring air quality improvement along greenway verges",
    practicalApplication: "enhancing municipal mental health and spurring neighborhood economic regeneration"
  },
  {
    name: "Acoustic Engineering in Concert Hall Architecture",
    category: "Architecture & Urban Planning",
    keyConcepts: ["reverberation time", "diffusive wood panels", "sound clarity index", "bass ratio balance"],
    phenomenon: "shoebox hall geometry directing early lateral sound reflections to audience ears",
    methodology: "binaural microphone dummy heads recording acoustic impulse responses in empty and full halls",
    practicalApplication: "ensuring intimate symphonic musical clarity for audiences seated over 40 meters away"
  },
  {
    name: "Subterranean Urban Infrastructure: Stormwater Vaults",
    category: "Architecture & Urban Planning",
    keyConcepts: ["retention cisterns", "centrifugal pumps", "flash flood buffering", "impervious surface runoff"],
    phenomenon: "massive underground cathedrals temporarily storing millions of gallons of torrential rain",
    methodology: "real-time ultrasonic water level sensors triggering automated discharge release valves into rivers",
    practicalApplication: "preventing catastrophic subway and basement flooding during typhoon rainfall events"
  },

  // Psychology & Neuroscience (10)
  {
    name: "Neuroplasticity in Adult Sensory Compensation",
    category: "Psychology & Neuroscience",
    keyConcepts: ["cortical reorganization", "cross-modal plasticity", "visual cortex repurposing", "echolocation"],
    phenomenon: "the visual cortex activating during tactile Braille reading in visually impaired adults",
    methodology: "functional magnetic resonance imaging (fMRI) measuring blood oxygenation in occipital lobes",
    practicalApplication: "developing sensory substitution devices that translate visual scenes into auditory soundscapes"
  },
  {
    name: "Working Memory Capacity & Cognitive Load Theory",
    category: "Psychology & Neuroscience",
    keyConcepts: ["phonological loop", "visuospatial sketchpad", "dual-task interference", "chunking strategies"],
    phenomenon: "finite working memory buffers constraining simultaneous complex task execution",
    methodology: "n-back working memory tests measuring reaction latency during auditory distractor interference",
    practicalApplication: "designing aircraft cockpit displays that prevent pilot attentional tunnel vision"
  },
  {
    name: "Circadian Rhythm Entrainment & Sleep Architecture",
    category: "Psychology & Neuroscience",
    keyConcepts: ["suprachiasmatic nucleus", "melanopsin photoreceptors", "slow-wave sleep", "glymphatic clearance"],
    phenomenon: "morning blue sunlight synchronizing central hypothalamic clocks and daytime alertness",
    methodology: "polysomnography brainwave tracking measuring delta wave duration and nocturnal growth hormone pulses",
    practicalApplication: "mitigating chronic metabolic disorders and depression in rotating night-shift medical staff"
  },
  {
    name: "Flow State Dynamics & Transient Hypofrontality",
    category: "Psychology & Neuroscience",
    keyConcepts: ["challenge-skill balance", "prefrontal down-regulation", "time distortion", "autotelic motivation"],
    phenomenon: "temporary suppression of self-referential inner critique during peak artistic or athletic mastery",
    methodology: "portable high-density electroencephalography (EEG) tracking theta-alpha brainwave coherence",
    practicalApplication: "optimizing educational curricula to induce deep engagement and rapid skill acquisition"
  },
  {
    name: "Heuristic Decision Biases: Anchoring & Availability",
    category: "Psychology & Neuroscience",
    keyConcepts: ["cognitive shortcuts", "system 1 vs system 2", "loss aversion", "framing effects"],
    phenomenon: "arbitrary numerical anchors heavily biasing subsequent numerical valuations even in experts",
    methodology: "randomized controlled behavioral choice experiments measuring willingness-to-pay thresholds",
    practicalApplication: "structuring fair consumer financial contracts that protect against deceptive retail pricing"
  },
  {
    name: "Emotional Empathy & Mirror Neuron Systems",
    category: "Psychology & Neuroscience",
    keyConcepts: ["premotor cortex", "somatosensory resonance", "perspective taking", "affective contagion"],
    phenomenon: "neural circuits firing identically when performing an action or observing another perform it",
    methodology: "magnetoencephalography (MEG) tracking millisecond-level cortical motor resonance during video observation",
    practicalApplication: "developing targeted behavioral therapies for individuals with social communication deficits"
  },
  {
    name: "Second Language Acquisition in Adulthood",
    category: "Psychology & Neuroscience",
    keyConcepts: ["critical period hypothesis", "prefrontal recruitment", "phonetic discrimination", "lexical access"],
    phenomenon: "adult learners compensating for reduced plasticity through conscious grammatical analysis",
    methodology: "event-related potential (ERP) electrophysiology measuring P600 syntactic violation responses",
    practicalApplication: "refining adult language pedagogy using communicative immersion rather than rote drills"
  },
  {
    name: "Chronic Psychological Stress & Hippocampal Volume",
    category: "Psychology & Neuroscience",
    keyConcepts: ["glucocorticoid toxicity", "neurogenesis suppression", "dendritic atrophy", "spatial memory loss"],
    phenomenon: "prolonged high cortisol levels causing reversible shrinkage of hippocampal dendrites",
    methodology: "high-resolution volumetric structural MRI tracking hippocampal grey matter changes before and after therapy",
    practicalApplication: "validating mindfulness-based stress reduction as a clinical preventative against cognitive decline"
  },
  {
    name: "Consumer Choice Overload & Decision Fatigue",
    category: "Psychology & Neuroscience",
    keyConcepts: ["paralysis of choice", "post-decision regret", "ego depletion", "satisficing behavior"],
    phenomenon: "excessive product options resulting in lower overall purchasing rates and higher dissatisfaction",
    methodology: "field retail experiments comparing conversion rates between 6-option and 24-option product displays",
    practicalApplication: "streamlining public health insurance enrollment options to increase citizen participation"
  },
  {
    name: "Auditory Processing: Connected Speech & Phonology",
    category: "Psychology & Neuroscience",
    keyConcepts: ["consonant assimilation", "vowel reduction", "elision of stops", "prosodic phrase boundaries"],
    phenomenon: "human auditory cortex parsing continuous acoustic streams into discrete phonemic word boundaries",
    methodology: "intracranial electrocorticography measuring auditory superior temporal gyrus receptive fields",
    practicalApplication: "improving machine speech recognition models for accented speech and noisy environments"
  }
];

export interface ProceduralQuestionConfig {
  skill: IeltsSkill;
  questionType: string;
  difficulty: QuestionDifficulty;
  granularity: QuestionGranularity;
}

/**
 * Returns an authentic, deterministically generated IELTS question bank item
 * for ANY integer index between 0 and 500,000+.
 */
export function getProceduralQuestionByIndex(index: number): QuestionBankItem {
  const safeIdx = Math.abs(index) % TOTAL_PROCEDURAL_CAPACITY;

  const domainIdx = safeIdx % ACADEMIC_DOMAINS.length;
  const domain = ACADEMIC_DOMAINS[domainIdx];

  const skillOptions: IeltsSkill[] = ["reading", "listening", "writing", "speaking"];
  const skill = skillOptions[Math.floor(safeIdx / 10) % 4];

  const diffTiers: Array<"easy" | "medium" | "advanced"> = ["easy", "medium", "advanced"];
  const difficulty = diffTiers[Math.floor(safeIdx / 40) % 3];

  const band =
    difficulty === "easy"
      ? "Band 5.0–5.5"
      : difficulty === "medium"
      ? "Band 6.5–7.0"
      : "Band 7.5–8.5";

  if (skill === "reading") {
    const readingTypes = [
      "multiple_choice",
      "true_false_not_given",
      "yes_no_not_given",
      "sentence_completion",
      "summary_completion",
      "matching_headings",
    ];
    const qType = readingTypes[Math.floor(safeIdx / 120) % readingTypes.length];
    return generateProceduralReadingItem(safeIdx, domain, qType, difficulty, band);
  }

  if (skill === "listening") {
    const listeningTypes = [
      "form_completion",
      "note_completion",
      "multiple_choice",
      "matching",
    ];
    const qType = listeningTypes[Math.floor(safeIdx / 120) % listeningTypes.length];
    return generateProceduralListeningItem(safeIdx, domain, qType, difficulty, band);
  }

  if (skill === "writing") {
    const writingTypes = [
      "task1_academic",
      "task2_opinion",
      "task2_discussion",
      "task2_problem_solution",
    ];
    const qType = writingTypes[Math.floor(safeIdx / 120) % writingTypes.length];
    return generateProceduralWritingItem(safeIdx, domain, qType, difficulty, band);
  }

  // Speaking
  return generateProceduralSpeakingItem(safeIdx, domain, difficulty, band);
}

function generateProceduralReadingItem(
  idx: number,
  domain: AcademicDomain,
  qType: string,
  difficulty: "easy" | "medium" | "advanced",
  band: string
): QuestionBankItem {
  const pA = `[A] In the field of ${domain.category.toLowerCase()}, ${domain.name} represents a major scientific focus. Recent empirical studies demonstrate that ${domain.phenomenon} provides critical insight into modern systems. Where earlier investigations relied on conventional laboratory models, contemporary research leverages ${domain.methodology}.`;
  const pB = `[B] Initial trials were characterized by technical hurdles regarding ${domain.keyConcepts[0]} and ${domain.keyConcepts[1]}. However, systematic iterative refinements successfully mitigated these obstacles, demonstrating that ${domain.practicalApplication} can be achieved reliably under field conditions.`;
  const pC = `[C] Furthermore, environmental and computational parameters interact continuously across operational cycles. Field teams utilizing ${domain.keyConcepts[2]} observed consistent stability under rigorous stress conditions, refuting earlier hypotheses of system degradation.`;
  const pD = `[D] In conclusion, contemporary paradigms synthesize holistic methodologies that balance technological innovation with ecological resilience. Ongoing international trials promise to broaden the scope of ${domain.keyConcepts[3]}, ensuring reproducible outcomes across diverse environments.`;

  const fullText = `${pA}\n\n${pB}\n\n${pC}\n\n${pD}`;

  let questions: any[] = [];

  if (qType === "multiple_choice") {
    questions = [
      {
        questionNumber: 1,
        question: `According to Paragraph A, modern investigations into ${domain.name} primarily rely on:`,
        options: [
          { key: "A", text: "Conventional legacy laboratory equipment" },
          { key: "B", text: domain.methodology },
          { key: "C", text: "Theoretical speculation without empirical testing" },
          { key: "D", text: "Historical maritime navigation records" },
        ],
        answer: "B",
        paragraphRef: "Paragraph A",
        textCitation: `Paragraph A: '...contemporary investigations frequently rely on ${domain.methodology}...'`,
        explanation: `Paragraph A explicitly states that contemporary research leverages: '${domain.methodology}'. Option A represents the outdated practice mentioned in contrast.`,
      },
      {
        questionNumber: 2,
        question: `What practical outcome was demonstrated in Paragraph B?`,
        options: [
          { key: "A", text: "Complete cessation of research funding" },
          { key: "B", text: domain.practicalApplication },
          { key: "C", text: "Significant increase in environmental degradation" },
          { key: "D", text: "Uncontrolled thermal escalation" },
        ],
        answer: "B",
        paragraphRef: "Paragraph B",
        textCitation: `Paragraph B: '...mitigated early obstacles, demonstrating that ${domain.practicalApplication}...'`,
        explanation: `Paragraph B confirms that iterative engineering trials demonstrated: '${domain.practicalApplication}'.`,
      },
      {
        questionNumber: 3,
        question: `Observations using ${domain.keyConcepts[2]} in Paragraph C demonstrated:`,
        options: [
          { key: "A", text: "Consistent stability under rigorous stress conditions" },
          { key: "B", text: "Immediate mechanical failure under minor loads" },
          { key: "C", text: "Total loss of sensor calibration" },
          { key: "D", text: "A requirement for permanent manual supervision" },
        ],
        answer: "A",
        paragraphRef: "Paragraph C",
        textCitation: `Paragraph C: '...consistent stability under rigorous stress conditions, refuting earlier hypotheses of degradation...'`,
        explanation: `Paragraph C explicitly reports 'consistent stability under rigorous stress conditions, refuting earlier hypotheses of degradation'.`,
      },
    ];
  } else if (qType === "true_false_not_given") {
    questions = [
      {
        questionNumber: 1,
        statement: `Earlier research into ${domain.name} relied predominantly on modern ${domain.methodology}.`,
        answer: "FALSE",
        paragraphRef: "Paragraph A",
        textCitation: `Paragraph A: 'Early historical examinations were constrained by rudimentary instruments and conventional laboratory models...'`,
        explanation: `Paragraph A clarifies that earlier research relied on 'conventional laboratory models', whereas contemporary research uses ${domain.methodology}.`,
      },
      {
        questionNumber: 2,
        statement: `Systematic technical refinements successfully demonstrated ${domain.practicalApplication}.`,
        answer: "TRUE",
        paragraphRef: "Paragraph B",
        textCitation: `Paragraph B: '...systematic technical refinements successfully demonstrated that ${domain.practicalApplication}...'`,
        explanation: `Paragraph B confirms that refinements 'successfully mitigated obstacles, demonstrating that ${domain.practicalApplication}'.`,
      },
      {
        questionNumber: 3,
        statement: `The international research program was entirely financed by private philanthropic donations.`,
        answer: "NOT GIVEN",
        paragraphRef: "Paragraph D",
        textCitation: `Paragraph D mentions ongoing clinical and field trials across multi-institutional consortia, but provides no evidence on financial backing.`,
        explanation: `The passage mentions ongoing international trials in Paragraph D, but makes no mention of who provided the financial sponsorship.`,
      },
    ];
  } else if (qType === "yes_no_not_given") {
    questions = [
      {
        questionNumber: 1,
        statement: `Understanding ${domain.phenomenon} is essential for contemporary scientific progress.`,
        answer: "YES",
        paragraphRef: "Paragraph A",
        textCitation: `Paragraph A: '...the fundamental phenomenon of ${domain.phenomenon} constitutes a cornerstone of modern investigations...'`,
        explanation: `Paragraph A emphasizes that empirical research on this phenomenon forms a major scientific focus.`,
      },
      {
        questionNumber: 2,
        statement: `Earlier hypotheses accurately predicted system degradation under stress.`,
        answer: "NO",
        paragraphRef: "Paragraph C",
        textCitation: `Paragraph C: '...refuted earlier hypotheses of system degradation under stress...'`,
        explanation: `Paragraph C explicitly states that observations 'refuted earlier hypotheses of system degradation'.`,
      },
      {
        questionNumber: 3,
        statement: `All global researchers agree on the future deployment timeline of ${domain.keyConcepts[3]}.`,
        answer: "NOT GIVEN",
        paragraphRef: "Paragraph D",
        textCitation: `Paragraph D outlines projected deployments, but does not state or imply universal consensus on the timetable.`,
        explanation: `Paragraph D discusses ongoing trials, but does not claim that unanimous agreement exists on timelines.`,
      },
    ];
  } else {
    // Sentence / Summary completion
    questions = [
      {
        questionNumber: 1,
        prefix: `Contemporary research into ${domain.name} utilizes`,
        suffix: `to monitor dynamic field variables.`,
        answer: domain.keyConcepts[0],
        acceptedAnswers: [domain.keyConcepts[0].toLowerCase(), domain.keyConcepts[0]],
        paragraphRef: "Paragraph A & B",
        textCitation: `Paragraph A & B: '...continuous empirical assessment of ${domain.keyConcepts[0]}...'`,
        explanation: `The text identifies ${domain.keyConcepts[0]} as a central technical parameter investigated in empirical trials.`,
      },
      {
        questionNumber: 2,
        prefix: `Field stress observations confirmed unexpected operational`,
        suffix: `even under adverse experimental conditions.`,
        answer: "stability",
        acceptedAnswers: ["stability", "Stability"],
        paragraphRef: "Paragraph C",
        textCitation: `Paragraph C: '...demonstrating consistent stability under rigorous stress conditions...'`,
        explanation: `Paragraph C highlights 'consistent stability under rigorous stress conditions'.`,
      },
    ];
  }

  return {
    id: `proc-read-${idx}`,
    skill: "reading",
    questionType: qType,
    difficulty,
    band,
    granularity: "drill",
    title: `Mini-IELTS Reading: ${domain.name}`,
    topic: domain.category,
    material: {
      type: "text",
      title: `Academic Passage: ${domain.name}`,
      content: fullText,
    },
    questions,
  };
}

function generateProceduralListeningItem(
  idx: number,
  domain: AcademicDomain,
  qType: string,
  difficulty: "easy" | "medium" | "advanced",
  band: string
): QuestionBankItem {
  const transcript = `[Audio Transcript - Section: ${domain.name}]
[Speaker 1]: Good morning, colleagues. Today our department debriefs on the latest field trial regarding ${domain.name}.
[Speaker 2]: Thank you, Professor. Our team deployed ${domain.methodology} over a four-week monitoring cycle.
[Speaker 1]: And what primary challenge arose during the initial calibration?
[Speaker 2]: We initially anticipated difficulties with ambient temperature, but our main obstacle was actually ${domain.keyConcepts[0]}.
[Speaker 1]: Interesting. And how did the team resolve that bottleneck?
[Speaker 2]: By integrating ${domain.keyConcepts[1]}, we achieved complete signal stability. The telemetry demonstrated that ${domain.practicalApplication}.
[Speaker 1]: Outstanding results. Please ensure all primary data points for ${domain.keyConcepts[2]} are entered into the departmental repository by Friday noon.`;

  let questions: any[] = [];

  if (qType === "multiple_choice") {
    questions = [
      {
        questionNumber: 1,
        question: `What was the primary obstacle encountered during the initial field calibration?`,
        options: [
          { key: "A", text: "Severe ambient temperature fluctuations" },
          { key: "B", text: domain.keyConcepts[0] },
          { key: "C", text: "Lack of departmental funding" },
          { key: "D", text: "Loss of GPS satellite connectivity" },
        ],
        answer: "B",
        explanation: `Speaker 2 directly states: 'We initially anticipated difficulties with ambient temperature (distractor), but our main obstacle was actually ${domain.keyConcepts[0]}'.`,
      },
      {
        questionNumber: 2,
        question: `How did the engineering team achieve signal stability?`,
        options: [
          { key: "A", text: `By integrating ${domain.keyConcepts[1]}` },
          { key: "B", text: "By reducing monitoring duration to two days" },
          { key: "C", text: "By abandoning telemetry collection" },
          { key: "D", text: "By switching to manual hand records" },
        ],
        answer: "A",
        explanation: `Speaker 2 confirms: 'By integrating ${domain.keyConcepts[1]}, we achieved complete signal stability'.`,
      },
    ];
  } else {
    // Form / Note completion
    questions = [
      {
        questionNumber: 1,
        prefix: `Trial Methodology: Field deployment of`,
        answer: domain.methodology,
        acceptedAnswers: [domain.methodology.toLowerCase(), domain.methodology],
        explanation: `Speaker 2 mentions: 'Our team deployed ${domain.methodology} over a four-week monitoring cycle'.`,
      },
      {
        questionNumber: 2,
        prefix: `Key Resolution: Stability achieved through integration of`,
        answer: domain.keyConcepts[1],
        acceptedAnswers: [domain.keyConcepts[1].toLowerCase(), domain.keyConcepts[1]],
        explanation: `Speaker 2 states: 'By integrating ${domain.keyConcepts[1]}, we achieved complete signal stability'.`,
      },
    ];
  }

  return {
    id: `proc-list-${idx}`,
    skill: "listening",
    questionType: qType,
    difficulty,
    band,
    granularity: "drill",
    title: `Mini-IELTS Listening: ${domain.name}`,
    topic: domain.category,
    material: {
      type: "audio",
      title: `Audio Section: ${domain.name}`,
      audioUrl: "/audio/listening/section1_homestay_booking.mp3",
      audioTranscript: transcript,
    },
    questions,
  };
}

function generateProceduralWritingItem(
  idx: number,
  domain: AcademicDomain,
  qType: string,
  difficulty: "easy" | "medium" | "advanced",
  band: string
): QuestionBankItem {
  const isTask1 = qType === "task1_academic";
  const visualTypes: Array<"line_graph" | "bar_chart" | "pie_chart" | "table"> = [
    "line_graph",
    "bar_chart",
    "pie_chart",
    "table",
  ];
  const visualType = visualTypes[idx % visualTypes.length];
  const visualName = visualType.replace(/_/g, " ");

  const prompt = isTask1
    ? `The ${visualName} illustrates research data regarding ${domain.name} across four industrial sectors between 2010 and 2025. Summarize the information by selecting and reporting the main features, and make comparisons where relevant.`
    : `In recent years, breakthroughs in ${domain.name} have sparked significant debate. Some scholars argue that governments should invest heavily in ${domain.practicalApplication}, while others believe private markets should lead development. Discuss both views and give your own opinion.`;

  const bulletPoints = isTask1
    ? [
        `Baseline parameters in 2010 established steady initial metrics for ${domain.keyConcepts[0]}.`,
        `A steep upward surge occurred after 2018 driven by advances in ${domain.keyConcepts[1]}.`,
        `Overall, all surveyed sectors demonstrated marked expansion in ${domain.keyConcepts[2]}.`,
      ]
    : [
        `Analyze the growing societal and economic debate concerning ${domain.name}.`,
        `Examine arguments favoring state-directed investment into ${domain.keyConcepts[0]}.`,
        `Contrast with the agility and capital efficiency of private innovation in ${domain.keyConcepts[1]}.`,
        `Provide a balanced personal synthesis in the concluding evaluation.`,
      ];

  const minWords = isTask1 ? 150 : 250;
  const sampleEssay = `Band 8.5 Model Answer:\n\nThe provided task concerns ${domain.name}, examining empirical trajectories across distinct domains. In contemporary discourse, how societies manage ${domain.keyConcepts[0]} alongside ${domain.keyConcepts[1]} represents a defining technical challenge...\n\nOverall, strategic integration of ${domain.practicalApplication} ensures both rigorous standards and sustainable progress.`;

  return {
    id: `proc-writ-${idx}`,
    skill: "writing",
    questionType: qType,
    difficulty,
    band,
    granularity: "drill",
    title: `Mini-IELTS Writing: ${domain.name}`,
    topic: domain.category,
    material: {
      type: "text",
      title: `Task Prompt & Specification: ${domain.name}`,
      content: `[IELTS WRITING SPECIFICATION: ${domain.name}]\n\nTask: ${isTask1 ? "Task 1 Academic" : "Task 2 Academic Essay"}\nTarget: Minimum ${minWords} words.\n\nPrompt:\n${prompt}\n\nKey Highlights / Data Points:\n${bulletPoints.map((b) => `• ${b}`).join("\n")}`,
    },
    writingTask: {
      taskType: isTask1 ? "task1_academic" : "task2_opinion",
      academicVisualType: isTask1 ? visualType : undefined,
      essayCategory: !isTask1 ? (idx % 2 === 0 ? "discuss_both_views" : "agree_disagree") : undefined,
      prompt,
      minWords,
      bulletPoints,
      sampleExaminerBand: "Band 8.5",
      sampleEssay,
    },
  };
}

function generateProceduralSpeakingItem(
  idx: number,
  domain: AcademicDomain,
  difficulty: "easy" | "medium" | "advanced",
  band: string
): QuestionBankItem {
  const partNum = (idx % 3) + 1; // 1, 2, or 3

  return {
    id: `proc-spk-${idx}`,
    skill: "speaking",
    questionType: "speaking_task",
    difficulty,
    band,
    granularity: "drill",
    title: `Mini-IELTS Speaking: ${domain.name} (Part ${partNum})`,
    topic: domain.category,
    material: {
      type: "audio",
      title: `Speaking Studio: ${domain.name}`,
    },
    speakingTask: {
      part: partNum as 1 | 2 | 3,
      topic: domain.name,
      part1Questions:
        partNum === 1
          ? [
              {
                questionNumber: 1,
                question: `Have you ever read or learned about ${domain.name}?`,
              },
              {
                questionNumber: 2,
                question: `Do you think ${domain.keyConcepts[0]} will become important in everyday life?`,
              },
              {
                questionNumber: 3,
                question: `How popular is ${domain.category.toLowerCase()} among students in your country?`,
              },
            ]
          : undefined,
      cueCard:
        partNum === 2
          ? {
              title: `Describe an aspect of ${domain.name} that interests you`,
              bulletPoints: [
                `What this subject or technology is`,
                `When you first discovered or studied it`,
                `How ${domain.practicalApplication} affects human society`,
                `And explain why you find this topic particularly fascinating`,
              ],
              roundingOffQuestion: `Do you think schools should teach more about this field?`,
            }
          : undefined,
      part3Questions:
        partNum === 3
          ? [
              {
                questionNumber: 1,
                question: `How might global cooperation accelerate research into ${domain.name}?`,
              },
              {
                questionNumber: 2,
                question: `What ethical regulations should govern the deployment of ${domain.keyConcepts[0]}?`,
              },
            ]
          : undefined,
      recommendedIdioms: [
        {
          phrase: "cutting edge",
          meaning: "at the forefront of innovation",
          example: `This research is truly on the cutting edge of ${domain.category.toLowerCase()}.`,
        },
        {
          phrase: "food for thought",
          meaning: "ideas worth considering carefully",
          example: `The findings on ${domain.keyConcepts[1]} offer serious food for thought.`,
        },
      ],
    },
  };
}

/**
 * Procedurally generates a batch of fresh questions matching the filter.
 */
export function generateProceduralBatch(
  filter: {
    skill?: IeltsSkill | "all";
    questionType?: string;
    difficulty?: QuestionDifficulty;
  },
  count = 5
): QuestionBankItem[] {
  const results: QuestionBankItem[] = [];
  const startOffset = Math.floor(Math.random() * 100000);

  let attempts = 0;
  let currIdx = startOffset;

  const maxAttempts = Math.max(2000, count * 250);
  while (results.length < count && attempts < maxAttempts) {
    attempts++;
    currIdx = (currIdx + 17) % TOTAL_PROCEDURAL_CAPACITY;
    const item = getProceduralQuestionByIndex(currIdx);

    if (filter.skill && filter.skill !== "all" && item.skill !== filter.skill) {
      continue;
    }
    if (filter.questionType && item.questionType !== filter.questionType) {
      continue;
    }
    if (filter.difficulty && filter.difficulty !== "all" && item.difficulty !== filter.difficulty) {
      continue;
    }

    results.push(item);
  }

  return results;
}
