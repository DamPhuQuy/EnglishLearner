import {
  BookOpen,
  Dices,
  RotateCcw,
  Search,
  Wand2,
  X,
} from "lucide-react";
import React, { useEffect, useMemo, useState } from "react";
import type { IeltsExerciseData, IeltsSkill } from "../../cell/types/ieltsSchema.ts";
import {
  generateProceduralBatch,
  getProceduralQuestionByIndex,
  TOTAL_PROCEDURAL_CAPACITY,
} from "../services/infiniteQuestionEngine.ts";
import {
  convertQuestionBankItemToExerciseData,
  filterQuestionBank,
  getQuestionBankStats,
  getQuestionCount,
  getRandomDrill,
} from "../services/questionBankService.ts";
import type {
  QuestionBankFilter,
  QuestionBankItem,
  QuestionDifficulty,
  QuestionGranularity,
} from "../types/questionBank.ts";

export interface QuestionBankModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectExercise: (exercise: IeltsExerciseData, asNewCell?: boolean) => void;
}

const QUESTION_TYPE_LABELS: Record<string, string> = {
  multiple_choice: "Multiple Choice",
  true_false_not_given: "True / False / Not Given",
  yes_no_not_given: "Yes / No / Not Given",
  sentence_completion: "Sentence Completion",
  summary_completion: "Summary Completion",
  form_completion: "Form Completion",
  note_completion: "Note Completion",
  matching_headings: "Matching Headings",
  matching_information: "Matching Information",
  matching_features: "Matching Features",
  plan_map_diagram_labelling: "Map / Plan Labelling",
  task1_academic: "Task 1 (Academic)",
  task1_general: "Task 1 (General)",
  task2_opinion: "Task 2 (Opinion)",
  task2_discussion: "Task 2 (Discussion)",
  task2_problem_solution: "Task 2 (Problem/Solution)",
  speaking_task: "Speaking Task",
};

const formatSnippetTeaser = (text?: string): string => {
  if (!text) return "";
  const clean = text
    .replace(/^\[[A-Z]\]\s*/i, "")
    .replace(/\n+/g, " ")
    .trim();
  if (clean.length <= 80) return clean;
  const truncated = clean.slice(0, 80);
  const lastSpace = truncated.lastIndexOf(" ");
  return (lastSpace > 45 ? truncated.slice(0, lastSpace) : truncated) + "…";
};

export const QuestionBankModal: React.FC<QuestionBankModalProps> = ({
  isOpen,
  onClose,
  onSelectExercise,
}) => {
  const [bankMode, setBankMode] = useState<"curated" | "infinite">("curated");
  const [selectedSkill, setSelectedSkill] = useState<IeltsSkill | "all">("all");
  const [selectedType, setSelectedType] = useState<string>("all");
  const [selectedDiff, setSelectedDiff] = useState<QuestionDifficulty>("all");
  const [selectedGranularity, setSelectedGranularity] = useState<QuestionGranularity>("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [indexInput, setIndexInput] = useState("428192");
  const [proceduralItems, setProceduralItems] = useState<QuestionBankItem[]>([]);

  const stats = useMemo(() => getQuestionBankStats(), []);

  // Keyboard escape listener to close modal
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        onClose();
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  // Compute available question types based on selected skill
  const availableTypes = useMemo(() => {
    const types = new Set<string>();
    const baseItems = filterQuestionBank({
      skill: selectedSkill,
    });
    for (const item of baseItems) {
      types.add(item.questionType);
    }
    return Array.from(types);
  }, [selectedSkill]);

  // Reset selectedType if unavailable under new skill
  useEffect(() => {
    if (selectedType !== "all" && !availableTypes.includes(selectedType)) {
      setSelectedType("all");
    }
  }, [availableTypes, selectedType]);

  const activeFilter: QuestionBankFilter = useMemo(
    () => ({
      skill: selectedSkill,
      questionTypes: selectedType !== "all" ? [selectedType] : undefined,
      difficulty: selectedDiff,
      granularity: selectedGranularity,
      search: searchQuery,
    }),
    [selectedSkill, selectedType, selectedDiff, selectedGranularity, searchQuery]
  );

  const filteredItems = useMemo(() => filterQuestionBank(activeFilter), [activeFilter]);

  const handleGenerateProcedural = (count = 6) => {
    const batch = generateProceduralBatch(
      {
        skill: selectedSkill,
        questionType: selectedType !== "all" ? selectedType : undefined,
        difficulty: selectedDiff,
      },
      count
    );
    setProceduralItems(batch);
  };

  const handleFetchIndex = () => {
    const num = parseInt(indexInput, 10);
    if (!isNaN(num) && num >= 0) {
      const single = getProceduralQuestionByIndex(num);
      setProceduralItems([single]);
    }
  };

  // Auto-generate items when switching to infinite mode or changing filters
  useEffect(() => {
    if (bankMode === "infinite") {
      handleGenerateProcedural(6);
    }
  }, [bankMode, selectedSkill, selectedType, selectedDiff]);

  const displayItems = bankMode === "curated" ? filteredItems : proceduralItems;

  const displayQuestionsCount = useMemo(() => {
    return displayItems.reduce((acc, item) => acc + getQuestionCount(item), 0);
  }, [displayItems]);

  const hasActiveFilters =
    selectedSkill !== "all" ||
    selectedType !== "all" ||
    selectedDiff !== "all" ||
    selectedGranularity !== "all" ||
    searchQuery.trim().length > 0;

  const handleResetFilters = () => {
    setSelectedSkill("all");
    setSelectedType("all");
    setSelectedDiff("all");
    setSelectedGranularity("all");
    setSearchQuery("");
    if (bankMode === "infinite") {
      handleGenerateProcedural(6);
    }
  };

  const handleRandomDrill = () => {
    if (bankMode === "infinite") {
      const randomIdx = Math.floor(Math.random() * TOTAL_PROCEDURAL_CAPACITY);
      const randomItem = getProceduralQuestionByIndex(randomIdx);
      const exercise = convertQuestionBankItemToExerciseData(randomItem);
      onSelectExercise(exercise, false);
      onClose();
      return;
    }
    const randomItem = getRandomDrill(activeFilter);
    if (randomItem) {
      const exercise = convertQuestionBankItemToExerciseData(randomItem);
      onSelectExercise(exercise, false);
      onClose();
    }
  };

  const handleApplyItem = (item: QuestionBankItem, asNewCell = false) => {
    const exercise = convertQuestionBankItemToExerciseData(item);
    onSelectExercise(exercise, asNewCell);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div
      className="qb-modal-backdrop"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="qb-modal-title"
    >
      <div className="qb-modal-container" onClick={(e) => e.stopPropagation()}>
        {/* Header */}
        <header className="qb-modal-header">
          <div className="qb-header-left">
            <div className="qb-header-title-row">
              <BookOpen size={16} className="qb-header-icon" />
              <h2 id="qb-modal-title" className="qb-title">Question bank</h2>
            </div>
            <div className="qb-mode-tabs" role="tablist" aria-label="Question Bank Mode">
              <button
                type="button"
                role="tab"
                aria-selected={bankMode === "curated"}
                className={`qb-mode-tab ${bankMode === "curated" ? "active" : ""}`}
                onClick={() => setBankMode("curated")}
              >
                Curated ({stats.totalQuestions})
              </button>
              <button
                type="button"
                role="tab"
                aria-selected={bankMode === "infinite"}
                className={`qb-mode-tab ${bankMode === "infinite" ? "active" : ""}`}
                onClick={() => setBankMode("infinite")}
              >
                Generator
              </button>
            </div>
          </div>
          <button
            className="qb-close-btn"
            onClick={onClose}
            aria-label="Close modal"
            title="Close (Esc)"
          >
            <X size={16} />
          </button>
        </header>

        {/* Filters Section */}
        <div className="qb-filters-section">
          {/* Skill Segmented Navigation */}
          <div className="qb-skill-bar" role="tablist" aria-label="Filter by skill">
            {(
              [
                { id: "all", label: "All skills", count: stats.totalQuestions },
                { id: "reading", label: "Reading", count: stats.bySkill.reading || 0 },
                { id: "listening", label: "Listening", count: stats.bySkill.listening || 0 },
                { id: "writing", label: "Writing", count: stats.bySkill.writing || 0 },
                { id: "speaking", label: "Speaking", count: stats.bySkill.speaking || 0 },
              ] as const
            ).map((skill) => {
              const isActive = selectedSkill === skill.id;
              return (
                <button
                  key={skill.id}
                  type="button"
                  role="tab"
                  aria-selected={isActive}
                  className={`qb-skill-btn ${skill.id} ${isActive ? "active" : ""}`}
                  onClick={() => setSelectedSkill(skill.id as IeltsSkill | "all")}
                >
                  <span className="qb-skill-label">{skill.label}</span>
                  <span className="qb-pill-count">{skill.count}</span>
                </button>
              );
            })}
          </div>

          {/* Controls Bar */}
          <div className="qb-controls-bar">
            <div className="qb-search-wrap">
              <Search size={14} className="qb-search-icon" />
              <input
                type="text"
                placeholder="Search topics, passages, or questions..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="qb-search-input"
                aria-label="Search questions"
              />
              {searchQuery && (
                <button
                  type="button"
                  className="qb-search-clear"
                  onClick={() => setSearchQuery("")}
                  aria-label="Clear search"
                >
                  <X size={13} />
                </button>
              )}
            </div>

            <div className="qb-dropdown-group">
              <select
                value={selectedType}
                onChange={(e) => setSelectedType(e.target.value)}
                className="qb-select"
                aria-label="Filter by question type"
              >
                <option value="all">All question types</option>
                {availableTypes.map((t) => (
                  <option key={t} value={t}>
                    {QUESTION_TYPE_LABELS[t] || t.replace(/_/g, " ")}
                  </option>
                ))}
              </select>

              <select
                value={selectedDiff}
                onChange={(e) => setSelectedDiff(e.target.value as QuestionDifficulty)}
                className="qb-select"
                aria-label="Filter by target band"
              >
                <option value="all">All bands</option>
                <option value="easy">Band 5.0 (Easy)</option>
                <option value="medium">Band 6.5 (Medium)</option>
                <option value="advanced">Band 8.0+ (Advanced)</option>
              </select>

              <select
                value={selectedGranularity}
                onChange={(e) => setSelectedGranularity(e.target.value as QuestionGranularity)}
                className="qb-select"
                aria-label="Filter by drill format"
              >
                <option value="all">All formats</option>
                <option value="micro">Micro-drill (1–3 Qs)</option>
                <option value="drill">Type drill (4–8 Qs)</option>
              </select>
            </div>

            {bankMode === "infinite" ? (
              <div className="qb-generator-bar">
                <div className="qb-seed-wrap">
                  <span className="qb-seed-prefix">#</span>
                  <input
                    type="number"
                    min="0"
                    max={TOTAL_PROCEDURAL_CAPACITY - 1}
                    value={indexInput}
                    onChange={(e) => setIndexInput(e.target.value)}
                    onKeyDown={(e) => e.key === "Enter" && handleFetchIndex()}
                    className="qb-seed-input"
                    aria-label="Question seed index"
                    placeholder="Index"
                  />
                  <button
                    type="button"
                    className="button quiet qb-sm-btn"
                    onClick={handleFetchIndex}
                  >
                    Jump
                  </button>
                </div>
                <button
                  type="button"
                  className="button quiet qb-sm-btn"
                  onClick={() => handleGenerateProcedural(6)}
                  title="Synthesize 6 new questions"
                >
                  <Wand2 size={13} />
                  Synthesize
                </button>
              </div>
            ) : (
              <div className="qb-actions-right">
                <button
                  type="button"
                  className="button quiet qb-sm-btn"
                  onClick={handleRandomDrill}
                  disabled={displayItems.length === 0}
                  title="Pick a random drill from current results"
                >
                  <Dices size={14} />
                  Random drill
                </button>
                {hasActiveFilters && (
                  <button
                    type="button"
                    className="button quiet qb-sm-btn qb-reset-btn"
                    onClick={handleResetFilters}
                    title="Reset all filters"
                  >
                    <RotateCcw size={12} />
                    Reset
                  </button>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Results Info Bar */}
        <div className="qb-results-bar">
          <span className="qb-results-text">
            {bankMode === "curated" ? (
              <>
                Showing <strong>{displayItems.length}</strong> modules (
                <strong>{displayQuestionsCount}</strong> questions)
              </>
            ) : (
              <>
                Showing <strong>{displayItems.length}</strong> synthesized modules from 500,000+ generator space
              </>
            )}
          </span>
          {hasActiveFilters && (
            <button
              type="button"
              className="qb-clear-all-link"
              onClick={handleResetFilters}
            >
              Clear filters
            </button>
          )}
        </div>

        {/* Cards Grid */}
        <div className="qb-cards-scrollable">
          {displayItems.length === 0 ? (
            <div className="qb-empty-state">
              <div className="qb-empty-icon-wrap">
                <Search size={22} className="qb-empty-icon" />
              </div>
              <h3 className="qb-empty-title">No matching exercises</h3>
              <p className="qb-empty-desc">
                No exercises found matching your current filter criteria.
              </p>
              <button
                type="button"
                className="button secondary"
                onClick={handleResetFilters}
              >
                Reset all filters
              </button>
            </div>
          ) : (
            <div className="qb-cards-grid">
              {displayItems.map((item) => {
                const count = getQuestionCount(item);
                const rawSnippet =
                  item.material?.content ||
                  item.material?.audioTranscript ||
                  item.writingTask?.prompt ||
                  item.speakingTask?.cueCard?.title ||
                  item.speakingTask?.part1Questions?.[0]?.question ||
                  "";
                const snippet = formatSnippetTeaser(rawSnippet);

                const skillLabel =
                  item.skill.charAt(0).toUpperCase() + item.skill.slice(1);
                const bandLabel =
                  item.difficulty === "easy"
                    ? "Band 5.0"
                    : item.difficulty === "medium"
                    ? "Band 6.5"
                    : "Band 8.0+";

                return (
                  <article key={item.id} className="qb-card">
                    <div className="qb-card-top">
                      <div className="qb-card-badges">
                        <span className={`qb-skill-badge ${item.skill}`}>
                          {skillLabel}
                        </span>
                        <span className="qb-type-badge">
                          {QUESTION_TYPE_LABELS[item.questionType] ||
                            item.questionType.replace(/_/g, " ")}
                        </span>
                        <span className={`qb-band-badge ${item.difficulty}`}>
                          <span className={`qb-band-dot ${item.difficulty}`} />
                          {bandLabel}
                        </span>
                      </div>
                      <span className="qb-count-badge">
                        {count} {count === 1 ? "question" : "questions"}
                      </span>
                    </div>

                    <div className="qb-card-body">
                      <h3 className="qb-card-title">{item.title}</h3>
                      {item.topic && (
                        <p className="qb-card-topic">{item.topic}</p>
                      )}
                      {snippet && (
                        <p className="qb-card-snippet">{snippet}</p>
                      )}
                    </div>

                    <div className="qb-card-footer">
                      <button
                        type="button"
                        className="button primary qb-card-action-btn"
                        onClick={() => handleApplyItem(item, false)}
                      >
                        Practice
                      </button>
                      <button
                        type="button"
                        className="button outlined qb-card-action-btn"
                        onClick={() => handleApplyItem(item, true)}
                        title="Append as a new cell in notebook"
                      >
                        + New cell
                      </button>
                    </div>
                  </article>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
