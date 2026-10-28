import {
  AlertCircle,
  BookOpen,
  Check,
  CheckCircle2,
  ChevronDown,
  ChevronUp,
  Clock,
  FileText,
  HelpCircle,
  Mic,
  PenLine,
  RotateCcw,
  Sparkles,
  Trophy,
  Volume2,
  XCircle,
} from "lucide-react";
import React, { useEffect, useState } from "react";
import type {
  IeltsCompletionQuestion,
  IeltsDiagramLabelQuestion,
  IeltsExerciseData,
  IeltsMatchingFeatureQuestion,
  IeltsMatchingHeadingQuestion,
  IeltsMatchingSentenceEndingQuestion,
  IeltsMultipleChoiceQuestion,
  IeltsQuestionGroup,
  IeltsTfngQuestion,
} from "../../types/ieltsSchema.ts";
import { estimateIeltsBand } from "../../types/ieltsSchema.ts";

export interface InteractiveQuestionSheetProps {
  data: IeltsExerciseData;
  onUpdateData: (updated: IeltsExerciseData) => void;
  onOpenImportModal?: () => void;
}

export const InteractiveQuestionSheet: React.FC<InteractiveQuestionSheetProps> = ({
  data,
  onUpdateData,
  onOpenImportModal,
}) => {
  const [isChecked, setIsChecked] = useState(Boolean(data.score));
  const [showSampleEssay, setShowSampleEssay] = useState(false);
  const [prepTimer, setPrepTimer] = useState<number | null>(null);
  const [speakTimer, setSpeakTimer] = useState<number | null>(null);
  const userAnswers = data.userAnswers || {};

  // Timers for Speaking Part 2
  useEffect(() => {
    let interval: number | undefined;
    if (prepTimer !== null && prepTimer > 0) {
      interval = window.setInterval(() => {
        setPrepTimer((t) => (t !== null && t > 0 ? t - 1 : 0));
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [prepTimer]);

  useEffect(() => {
    let interval: number | undefined;
    if (speakTimer !== null && speakTimer > 0) {
      interval = window.setInterval(() => {
        setSpeakTimer((t) => (t !== null && t > 0 ? t - 1 : 0));
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [speakTimer]);

  const handleSelectAnswer = (qNum: number, answer: string) => {
    const nextAnswers = {
      ...userAnswers,
      [qNum]: answer,
    };
    onUpdateData({
      ...data,
      userAnswers: nextAnswers,
    });
  };

  const handleToggleMultiChoice = (qNum: number, optionKey: string, maxChoices = 2) => {
    const raw = userAnswers[qNum] || "";
    const currentList = raw ? raw.split(",").map((s) => s.trim().toUpperCase()) : [];
    const opt = optionKey.toUpperCase();

    let nextList: string[];
    if (currentList.includes(opt)) {
      nextList = currentList.filter((k) => k !== opt);
    } else {
      if (currentList.length >= maxChoices) {
        nextList = [...currentList.slice(1), opt];
      } else {
        nextList = [...currentList, opt];
      }
    }

    nextList.sort();
    handleSelectAnswer(qNum, nextList.join(","));
  };

  const handleCheckAnswers = () => {
    let correctCount = 0;
    let totalQuestions = 0;

    (data.questionGroups || []).forEach((group) => {
      group.questions.forEach((q) => {
        totalQuestions++;
        const userAns = (userAnswers[q.questionNumber] || "").trim().toLowerCase();
        const expected = String(q.answer || "").trim().toLowerCase();
        const accepted = Array.isArray((q as any).acceptedAnswers)
          ? (q as any).acceptedAnswers.map((a: string) => String(a).trim().toLowerCase())
          : [];

        if (Array.isArray(q.answer)) {
          const expectedSorted = [...q.answer].map((a) => a.trim().toLowerCase()).sort().join(",");
          const userSorted = userAns.split(",").map((s) => s.trim().toLowerCase()).sort().join(",");
          if (expectedSorted === userSorted) correctCount++;
        } else if (userAns && (userAns === expected || accepted.includes(userAns))) {
          correctCount++;
        }
      });
    });

    const scoreResult = {
      correct: correctCount,
      total: totalQuestions,
      checkedAt: new Date().toISOString(),
      bandEstimate: estimateIeltsBand(correctCount, totalQuestions),
    };

    setIsChecked(true);
    onUpdateData({
      ...data,
      score: scoreResult,
    });
  };

  const handleReset = () => {
    setIsChecked(false);
    onUpdateData({
      ...data,
      userAnswers: {},
      score: undefined,
    });
  };

  /* Render TFNG / YNNG */
  const renderTfngGroup = (group: IeltsQuestionGroup) => {
    const isYnng = group.type === "yes_no_not_given";
    const options = isYnng ? ["YES", "NO", "NOT GIVEN"] : ["TRUE", "FALSE", "NOT GIVEN"];

    return (
      <div key={group.id} className="interactive-group">
        <div className="group-heading">
          <h4>{group.title || (isYnng ? "Yes / No / Not Given" : "True / False / Not Given")}</h4>
          <p className="group-instruction">{group.instruction}</p>
        </div>
        <div className="group-questions">
          {group.questions.map((q) => {
            const tfq = q as IeltsTfngQuestion;
            const currentAns = userAnswers[tfq.questionNumber];
            const isCorrect =
              isChecked &&
              currentAns?.trim().toUpperCase() === tfq.answer?.trim().toUpperCase();

            return (
              <div
                key={tfq.questionNumber}
                className={`question-item ${isChecked ? (isCorrect ? "correct" : "incorrect") : ""}`}
              >
                <div className="question-statement-row">
                  <span className="q-badge">Q{tfq.questionNumber}</span>
                  <p className="q-statement">{tfq.statement}</p>
                </div>

                <div className="options-pill-grid">
                  {options.map((opt) => {
                    const isSelected = currentAns?.toUpperCase() === opt;
                    const isTarget = isChecked && tfq.answer?.toUpperCase() === opt;

                    let btnClass = "option-pill";
                    if (isSelected) btnClass += " selected";
                    if (isChecked && isTarget) btnClass += " target-answer";
                    if (isChecked && isSelected && !isCorrect) btnClass += " wrong-selection";

                    return (
                      <button
                        key={opt}
                        type="button"
                        className={btnClass}
                        onClick={() => handleSelectAnswer(tfq.questionNumber, opt)}
                      >
                        {opt}
                      </button>
                    );
                  })}
                </div>

                {isChecked && (
                  <div className={`answer-feedback ${isCorrect ? "feedback-pass" : "feedback-fail"}`}>
                    <div className="feedback-status">
                      {isCorrect ? <CheckCircle2 size={15} /> : <XCircle size={15} />}
                      <span>{isCorrect ? "Correct!" : `Correct answer: ${tfq.answer}`}</span>
                    </div>
                    {tfq.explanation && (
                      <div className="feedback-explanation">
                        <HelpCircle size={13} />
                        <span>
                          {tfq.paragraphRef ? `[${tfq.paragraphRef}] ` : ""}
                          {tfq.explanation}
                        </span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  /* Render Multiple Choice (Single & Multi-select) */
  const renderMultipleChoiceGroup = (group: IeltsQuestionGroup) => {
    return (
      <div key={group.id} className="interactive-group">
        <div className="group-heading">
          <h4>{group.title || "Multiple Choice"}</h4>
          <p className="group-instruction">{group.instruction}</p>
        </div>
        <div className="group-questions">
          {group.questions.map((q) => {
            const mcq = q as IeltsMultipleChoiceQuestion;
            const currentAns = userAnswers[mcq.questionNumber] || "";
            const isMulti = mcq.isMultiSelect || Array.isArray(mcq.answer);

            let isCorrect = false;
            if (isChecked) {
              if (Array.isArray(mcq.answer)) {
                const target = [...mcq.answer].map((s) => s.toUpperCase()).sort().join(",");
                const user = currentAns.split(",").map((s) => s.trim().toUpperCase()).sort().join(",");
                isCorrect = target === user;
              } else {
                isCorrect = currentAns.trim().toUpperCase() === String(mcq.answer).trim().toUpperCase();
              }
            }

            return (
              <div
                key={mcq.questionNumber}
                className={`question-item ${isChecked ? (isCorrect ? "correct" : "incorrect") : ""}`}
              >
                <div className="question-statement-row">
                  <span className="q-badge">Q{mcq.questionNumber}</span>
                  <p className="q-statement">{mcq.question}</p>
                </div>

                <div className="mcq-options-list">
                  {mcq.options.map((opt) => {
                    const currentSelectedList = currentAns.split(",").map((s) => s.trim().toUpperCase());
                    const isSelected = isMulti
                      ? currentSelectedList.includes(opt.key.toUpperCase())
                      : currentAns.toUpperCase() === opt.key.toUpperCase();

                    const isTarget = isChecked && (
                      Array.isArray(mcq.answer)
                        ? mcq.answer.map((s) => s.toUpperCase()).includes(opt.key.toUpperCase())
                        : mcq.answer.toUpperCase() === opt.key.toUpperCase()
                    );

                    let optClass = "mcq-choice-card";
                    if (isSelected) optClass += " selected";
                    if (isChecked && isTarget) optClass += " target-answer";
                    if (isChecked && isSelected && !isCorrect) optClass += " wrong-selection";

                    return (
                      <button
                        key={opt.key}
                        type="button"
                        className={optClass}
                        onClick={() => {
                          if (isMulti) {
                            handleToggleMultiChoice(mcq.questionNumber, opt.key, mcq.maxChoices || 2);
                          } else {
                            handleSelectAnswer(mcq.questionNumber, opt.key);
                          }
                        }}
                      >
                        <span className="mcq-key">{opt.key}</span>
                        <span className="mcq-text">{opt.text}</span>
                      </button>
                    );
                  })}
                </div>

                {isChecked && (
                  <div className={`answer-feedback ${isCorrect ? "feedback-pass" : "feedback-fail"}`}>
                    <div className="feedback-status">
                      {isCorrect ? <CheckCircle2 size={15} /> : <XCircle size={15} />}
                      <span>
                        {isCorrect
                          ? "Correct!"
                          : `Correct answer: ${Array.isArray(mcq.answer) ? mcq.answer.join(", ") : mcq.answer}`}
                      </span>
                    </div>
                    {mcq.explanation && (
                      <div className="feedback-explanation">
                        <HelpCircle size={13} />
                        <span>
                          {mcq.paragraphRef ? `[${mcq.paragraphRef}] ` : ""}
                          {mcq.explanation}
                        </span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  /* Render Completion / Blanks / Table / Flow-Chart */
  const renderCompletionGroup = (group: IeltsQuestionGroup) => {
    const boxOptions = group.boxOptions || [];

    return (
      <div key={group.id} className="interactive-group">
        <div className="group-heading">
          <h4>{group.title || "Completion"}</h4>
          <p className="group-instruction">{group.instruction}</p>
          {group.wordLimitRule && (
            <span className="word-limit-badge">{group.wordLimitRule}</span>
          )}
        </div>

        {boxOptions.length > 0 && (
          <div className="box-options-card">
            <span className="box-options-title">Word Pool</span>
            <div className="box-options-grid">
              {boxOptions.map((b) => (
                <span key={b.key} className="box-pill">
                  <strong>{b.key}:</strong> {b.word}
                </span>
              ))}
            </div>
          </div>
        )}

        <div className="group-questions">
          {group.questions.map((q) => {
            const cq = q as IeltsCompletionQuestion;
            const currentAns = userAnswers[cq.questionNumber] || "";
            const expected = String(cq.answer || "").trim().toLowerCase();
            const accepted = Array.isArray(cq.acceptedAnswers)
              ? cq.acceptedAnswers.map((a) => String(a).trim().toLowerCase())
              : [];
            const isCorrect =
              isChecked &&
              currentAns.trim() &&
              (currentAns.trim().toLowerCase() === expected ||
                accepted.includes(currentAns.trim().toLowerCase()));

            return (
              <div
                key={cq.questionNumber}
                className={`question-item ${isChecked ? (isCorrect ? "correct" : "incorrect") : ""}`}
              >
                <div className="completion-row">
                  <span className="q-badge">Q{cq.questionNumber}</span>
                  <div className="completion-line">
                    {cq.prompt && <span className="completion-prompt">{cq.prompt}</span>}
                    {cq.prefix && <span className="completion-prefix">{cq.prefix}</span>}
                    <input
                      type="text"
                      className="completion-input"
                      value={currentAns}
                      placeholder="Your answer…"
                      onChange={(e) =>
                        handleSelectAnswer(cq.questionNumber, e.target.value)
                      }
                    />
                    {cq.suffix && <span className="completion-suffix">{cq.suffix}</span>}
                  </div>
                </div>

                {isChecked && (
                  <div className={`answer-feedback ${isCorrect ? "feedback-pass" : "feedback-fail"}`}>
                    <div className="feedback-status">
                      {isCorrect ? <CheckCircle2 size={15} /> : <XCircle size={15} />}
                      <span>
                        {isCorrect
                          ? "Correct!"
                          : `Expected: ${cq.answer}${cq.acceptedAnswers?.length ? ` (or: ${cq.acceptedAnswers.join(", ")})` : ""}`}
                      </span>
                    </div>
                    {cq.explanation && (
                      <div className="feedback-explanation">
                        <HelpCircle size={13} />
                        <span>
                          {cq.paragraphRef ? `[${cq.paragraphRef}] ` : ""}
                          {cq.explanation}
                        </span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  /* Render Matching Headings */
  const renderMatchingHeadingsGroup = (group: IeltsQuestionGroup) => {
    const headings = group.headingsList || [];

    return (
      <div key={group.id} className="interactive-group">
        <div className="group-heading">
          <h4>{group.title || "Matching Headings"}</h4>
          <p className="group-instruction">{group.instruction}</p>
        </div>

        {headings.length > 0 && (
          <div className="headings-bank-card">
            <span className="headings-bank-title">List of Headings</span>
            <div className="headings-grid">
              {headings.map((h) => (
                <div key={h.id} className="heading-row">
                  <span className="heading-id">{h.id}</span>
                  <span className="heading-text">{h.heading}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="group-questions">
          {group.questions.map((q) => {
            const mhq = q as IeltsMatchingHeadingQuestion;
            const currentAns = userAnswers[mhq.questionNumber];
            const isCorrect =
              isChecked &&
              currentAns?.trim().toLowerCase() === mhq.answer?.trim().toLowerCase();

            return (
              <div
                key={mhq.questionNumber}
                className={`question-item ${isChecked ? (isCorrect ? "correct" : "incorrect") : ""}`}
              >
                <div className="heading-select-row">
                  <span className="q-badge">Q{mhq.questionNumber}</span>
                  <span className="paragraph-label">Paragraph {mhq.paragraph}</span>
                  <select
                    className="heading-dropdown"
                    value={currentAns || ""}
                    onChange={(e) =>
                      handleSelectAnswer(mhq.questionNumber, e.target.value)
                    }
                  >
                    <option value="">-- Choose Heading --</option>
                    {headings.map((h) => (
                      <option key={h.id} value={h.id}>
                        {h.id}: {h.heading}
                      </option>
                    ))}
                  </select>
                </div>

                {isChecked && (
                  <div className={`answer-feedback ${isCorrect ? "feedback-pass" : "feedback-fail"}`}>
                    <div className="feedback-status">
                      {isCorrect ? <CheckCircle2 size={15} /> : <XCircle size={15} />}
                      <span>{isCorrect ? "Correct!" : `Correct heading: ${mhq.answer}`}</span>
                    </div>
                    {mhq.explanation && (
                      <div className="feedback-explanation">
                        <HelpCircle size={13} />
                        <span>{mhq.explanation}</span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  /* Render Matching Information / Features / Endings */
  const renderMatchingGroup = (group: IeltsQuestionGroup) => {
    const isFeatures = group.type === "matching_features";
    const isEndings = group.type === "matching_sentence_endings";
    const features = group.featuresList || [];
    const endings = group.endingsList || [];

    return (
      <div key={group.id} className="interactive-group">
        <div className="group-heading">
          <h4>{group.title || "Matching"}</h4>
          <p className="group-instruction">{group.instruction}</p>
        </div>

        {isFeatures && features.length > 0 && (
          <div className="headings-bank-card">
            <span className="headings-bank-title">List of Items / Researchers</span>
            <div className="headings-grid">
              {features.map((f) => (
                <div key={f.key} className="heading-row">
                  <span className="heading-id">{f.key}</span>
                  <span className="heading-text">
                    <strong>{f.name}</strong>
                    {f.description ? ` — ${f.description}` : ""}
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}

        {isEndings && endings.length > 0 && (
          <div className="headings-bank-card">
            <span className="headings-bank-title">Sentence Endings Bank</span>
            <div className="headings-grid">
              {endings.map((e) => (
                <div key={e.key} className="heading-row">
                  <span className="heading-id">{e.key}</span>
                  <span className="heading-text">{e.text}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="group-questions">
          {group.questions.map((q) => {
            const currentAns = userAnswers[q.questionNumber];
            const isCorrect =
              isChecked &&
              currentAns?.trim().toUpperCase() === String(q.answer).trim().toUpperCase();

            const promptText =
              (q as any).statement || (q as any).beginning || (q as any).question || "";

            return (
              <div
                key={q.questionNumber}
                className={`question-item ${isChecked ? (isCorrect ? "correct" : "incorrect") : ""}`}
              >
                <div className="question-statement-row">
                  <span className="q-badge">Q{q.questionNumber}</span>
                  <p className="q-statement">{promptText}</p>
                </div>

                <div className="matching-select-line">
                  <span className="matching-target-label">Match:</span>
                  <select
                    className="heading-dropdown"
                    value={currentAns || ""}
                    onChange={(e) =>
                      handleSelectAnswer(q.questionNumber, e.target.value)
                    }
                  >
                    <option value="">-- Select Match --</option>
                    {isFeatures
                      ? features.map((f) => (
                          <option key={f.key} value={f.key}>
                            {f.key}: {f.name}
                          </option>
                        ))
                      : isEndings
                      ? endings.map((e) => (
                          <option key={e.key} value={e.key}>
                            {e.key}: {e.text}
                          </option>
                        ))
                      : ["A", "B", "C", "D", "E", "F", "G"].map((letter) => (
                          <option key={letter} value={letter}>
                            Paragraph {letter}
                          </option>
                        ))}
                  </select>
                </div>

                {isChecked && (
                  <div className={`answer-feedback ${isCorrect ? "feedback-pass" : "feedback-fail"}`}>
                    <div className="feedback-status">
                      {isCorrect ? <CheckCircle2 size={15} /> : <XCircle size={15} />}
                      <span>{isCorrect ? "Correct!" : `Correct: ${q.answer}`}</span>
                    </div>
                    {q.explanation && (
                      <div className="feedback-explanation">
                        <HelpCircle size={13} />
                        <span>
                          {q.paragraphRef ? `[${q.paragraphRef}] ` : ""}
                          {q.explanation}
                        </span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  /* Render Writing Task Info Card */
  const renderWritingTaskCard = () => {
    if (!data.writingTask) return null;
    const wt = data.writingTask;

    return (
      <div className="writing-task-card">
        <div className="writing-task-header">
          <div className="writing-task-badge">
            <PenLine size={14} />
            <span>
              {String(wt.taskType).includes("task1") ? "IELTS WRITING TASK 1" : "IELTS WRITING TASK 2"}
            </span>
          </div>
          <span className="writing-target-words">Target: {wt.minWords}+ words</span>
        </div>

        <div className="writing-task-prompt-box">
          <p>{wt.prompt}</p>
        </div>

        {wt.keyDataPoints && wt.keyDataPoints.length > 0 && (
          <div className="writing-datapoints-card">
            <strong>Key Data Highlights:</strong>
            <ul>
              {wt.keyDataPoints.map((dp, i) => (
                <li key={i}>{dp}</li>
              ))}
            </ul>
          </div>
        )}

        {wt.sampleEssay && (
          <div className="sample-essay-section">
            <button
              type="button"
              className="button quiet small toggle-sample-btn"
              onClick={() => setShowSampleEssay((v) => !v)}
            >
              <BookOpen size={13} />
              <span>
                {showSampleEssay ? "Hide Model Answer" : `View ${wt.sampleExaminerBand || "Band 8.0+"} Model Essay`}
              </span>
              {showSampleEssay ? <ChevronUp size={13} /> : <ChevronDown size={13} />}
            </button>

            {showSampleEssay && (
              <div className="sample-essay-box">
                <pre>{wt.sampleEssay}</pre>
              </div>
            )}
          </div>
        )}
      </div>
    );
  };

  /* Render Speaking Task Info Card */
  const renderSpeakingTaskCard = () => {
    if (!data.speakingTask) return null;
    const st = data.speakingTask;

    return (
      <div className="speaking-task-card">
        <div className="speaking-task-header">
          <div className="speaking-task-badge">
            <Mic size={14} />
            <span>SPEAKING PART {st.part}</span>
          </div>
          <span className="speaking-topic-tag">Topic: {st.topic}</span>
        </div>

        {st.part === 1 && st.part1Questions && (
          <div className="speaking-questions-list">
            <strong>Examiner Questions:</strong>
            <ol>
              {st.part1Questions.map((q) => (
                <li key={q.questionNumber}>{q.question}</li>
              ))}
            </ol>
          </div>
        )}

        {st.part === 2 && st.cueCard && (
          <div className="speaking-cuecard-card">
            <h4>{st.cueCard.title}</h4>
            <span className="cuecard-hint">You should say:</span>
            <ul>
              {st.cueCard.bulletPoints.map((pt, i) => (
                <li key={i}>{pt}</li>
              ))}
            </ul>

            <div className="speaking-timer-bar">
              <div className="timer-unit">
                <button
                  type="button"
                  className="button quiet small"
                  onClick={() => setPrepTimer(60)}
                >
                  <Clock size={13} />
                  <span>Start 1-Min Prep</span>
                </button>
                {prepTimer !== null && (
                  <span className={`timer-display ${prepTimer <= 10 ? "urgent" : ""}`}>
                    {prepTimer}s
                  </span>
                )}
              </div>

              <div className="timer-unit">
                <button
                  type="button"
                  className="button quiet small"
                  onClick={() => setSpeakTimer(120)}
                >
                  <Clock size={13} />
                  <span>Start 2-Min Talk</span>
                </button>
                {speakTimer !== null && (
                  <span className={`timer-display ${speakTimer <= 15 ? "urgent" : ""}`}>
                    {Math.floor(speakTimer / 60)}:
                    {(speakTimer % 60).toString().padStart(2, "0")}
                  </span>
                )}
              </div>
            </div>
          </div>
        )}

        {st.part === 3 && st.part3Questions && (
          <div className="speaking-questions-list">
            <strong>Discussion Questions:</strong>
            <ol>
              {st.part3Questions.map((q) => (
                <li key={q.questionNumber}>{q.question}</li>
              ))}
            </ol>
          </div>
        )}

        {st.recommendedIdioms && st.recommendedIdioms.length > 0 && (
          <div className="speaking-idioms-card">
            <strong>High-Scoring Lexical Collocations & Idioms:</strong>
            <div className="idioms-grid">
              {st.recommendedIdioms.map((idm, i) => (
                <div key={i} className="idiom-item">
                  <span className="idiom-phrase">{idm.phrase}</span>
                  <span className="idiom-meaning">{idm.meaning}</span>
                  <span className="idiom-example">"{idm.example}"</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  };

  const questionGroups = data.questionGroups || [];
  const totalQuestions = questionGroups.reduce(
    (acc, g) => acc + (g.questions?.length || 0),
    0
  );
  const answeredCount = Object.keys(userAnswers).filter((k) =>
    Boolean(userAnswers[k]?.trim())
  ).length;

  return (
    <div className="interactive-sheet-container">
      {/* Test Meta Bar */}
      <div className="interactive-meta-bar">
        <div className="meta-left">
          <span className="test-skill-tag">{data.skill.toUpperCase()}</span>
          <span className="test-title-text">{data.title}</span>
          {data.difficulty && (
            <span className="test-difficulty-tag">{data.difficulty}</span>
          )}
        </div>
        <div className="meta-right">
          {totalQuestions > 0 && (
            <span className="answered-status">
              Answered: {answeredCount}/{totalQuestions}
            </span>
          )}
          {onOpenImportModal && (
            <button
              type="button"
              className="button quiet small"
              onClick={onOpenImportModal}
              title="Replace or update with new AI JSON"
            >
              <Sparkles size={13} />
              AI JSON
            </button>
          )}
        </div>
      </div>

      {/* Productive Skill Cards (Writing / Speaking) */}
      {renderWritingTaskCard()}
      {renderSpeakingTaskCard()}

      {/* Score Banner when checked */}
      {data.score && isChecked && totalQuestions > 0 && (
        <div className="score-summary-banner">
          <div className="score-icon-box">
            <Trophy size={20} />
          </div>
          <div className="score-details">
            <span className="score-number">
              Result: {data.score.correct} / {data.score.total} Correct (
              {Math.round((data.score.correct / Math.max(1, data.score.total)) * 100)}%)
            </span>
            <span className="score-band">
              Estimated Score: {data.score.bandEstimate || "N/A"}
            </span>
          </div>
          <button
            type="button"
            className="button quiet small"
            onClick={handleReset}
          >
            <RotateCcw size={13} />
            Try again
          </button>
        </div>
      )}

      {/* Render All Question Groups */}
      <div className="question-groups-flow">
        {questionGroups.map((group) => {
          if (
            group.type === "true_false_not_given" ||
            group.type === "yes_no_not_given"
          ) {
            return renderTfngGroup(group);
          }
          if (group.type === "multiple_choice") {
            return renderMultipleChoiceGroup(group);
          }
          if (group.type === "matching_headings") {
            return renderMatchingHeadingsGroup(group);
          }
          if (
            group.type === "matching_information" ||
            group.type === "matching_features" ||
            group.type === "matching_sentence_endings"
          ) {
            return renderMatchingGroup(group);
          }
          return renderCompletionGroup(group);
        })}
      </div>

      {/* Vocabulary Glossary if present */}
      {data.vocabularyNotes && data.vocabularyNotes.length > 0 && (
        <div className="vocab-glossary-card">
          <span className="vocab-glossary-title">Key Academic Vocabulary</span>
          <div className="vocab-glossary-grid">
            {data.vocabularyNotes.map((v, i) => (
              <div key={i} className="vocab-item">
                <div className="vocab-word-line">
                  <strong>{v.word}</strong>
                  {v.type && <span className="vocab-type">({v.type})</span>}
                </div>
                <p className="vocab-def">{v.definition}</p>
                {v.example && <span className="vocab-ex">"{v.example}"</span>}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bottom Action Footer */}
      {totalQuestions > 0 && (
        <div className="interactive-footer-bar">
          <button
            type="button"
            className="button primary check-answers-btn"
            onClick={handleCheckAnswers}
          >
            <Check size={16} />
            Check Answers ({answeredCount}/{totalQuestions})
          </button>

          {answeredCount > 0 && (
            <button
              type="button"
              className="button quiet"
              onClick={handleReset}
            >
              <RotateCcw size={15} />
              Reset
            </button>
          )}
        </div>
      )}
    </div>
  );
};
