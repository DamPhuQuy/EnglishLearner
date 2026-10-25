import type { SkillType } from "../../notebook/types/notebook.ts";

export const SKILL_NAMES: Record<SkillType, string> = {
  listening: "Listening",
  reading: "Reading",
  writing: "Writing",
  speaking: "Speaking",
  markdown: "Notes",
};

export const SKILL_RESOURCE_LABELS: Record<SkillType, string> = {
  listening: "Audio Track",
  reading: "Reading Passage",
  writing: "Prompt & Reference",
  speaking: "Record & Review",
  markdown: "Attached Document",
};

export const SKILL_TEMPLATES: Record<SkillType, string> = {
  listening: "### Listening\n\n1. \n2. \n3. \n\n### Vocabulary & Connected Speech\n\n- ",
  reading:
    "### Reading\n\n1. \n2. \n3. \n\n### Text Evidence\n\n> \n\n### Vocabulary\n\n- ",
  writing: "### Writing\n\n### Outline\n\n- \n\n### Essay\n\n",
  speaking:
    "### Speaking Part 2\n\nTopic: \n\n- What:\n- When:\n- Why:\n\n### Self-Reflection\n\n",
  markdown: "### Notes\n\n",
};

export function getSkillTemplate(skill: SkillType): string {
  return SKILL_TEMPLATES[skill] ?? "";
}

export function appendTemplateToSource(
  existingSource: string,
  skill: SkillType,
): string {
  const template = getSkillTemplate(skill);
  if (!existingSource.trim()) {
    return template;
  }
  return `${existingSource}\n\n${template}`;
}
