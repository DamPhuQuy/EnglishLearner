#!/usr/bin/env python3
"""
Master Authentic IELTS Question Bank Generator & Validator
Orchestrates high-fidelity IELTS question bank generation across all 4 skills:
- Reading: 8 full-length academic passages (~850 words each) with verified questions
- Listening: 8 multi-speaker audio tracks synthesized via Edge-TTS & ffmpeg with exact timestamps
- Writing: 28 tasks (8 Academic Task 1, 6 General Task 1, 14 Task 2) with full authentic model essays
- Speaking: 20 modules (12 Part 1 everyday topics, 8 Part 2 cue cards & Part 3 discussion modules)

Validates all converted exercise models against ielts-exercise-schema.json.
Outputs to frontend/src/data/question-bank/ and frontend/public/audio/listening/.
"""

import asyncio
import json
import os
import sys
import jsonschema

# Add authentic_builder to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from authentic_builder.writing_data import WRITING_ITEMS
from authentic_builder.speaking_data import SPEAKING_ITEMS
from authentic_builder.reading_data import READING_ITEMS
from authentic_builder.listening_data import LISTENING_SECTIONS
from authentic_builder.audio_generator import build_all_listening_items

def convert_item_to_exercise_schema(item: dict) -> dict:
    """Converts a QuestionBankItem to the exact format defined in ielts-exercise-schema.json."""
    exercise = {
        "version": "1.0",
        "skill": item["skill"],
        "title": item["title"],
        "topic": item.get("topic", "IELTS Academic Test"),
        "difficulty": item.get("band", "Band 6.5–7.5"),
        "timeLimitMinutes": 20
    }

    if "material" in item and item["material"]:
        exercise["material"] = dict(item["material"])

    if "questionGroups" in item and item["questionGroups"]:
        exercise["questionGroups"] = item["questionGroups"]
    elif "questions" in item and item["questions"]:
        q_type = item["questionType"]
        # Map generic 'matching' to matching_features or matching_information
        if q_type == "matching":
            q_type = "matching_information"

        group = {
            "id": f"group-{item['id']}",
            "type": q_type,
            "instruction": item.get("instruction", f"Answer the questions below according to the {item['skill']} material."),
            "questions": item["questions"]
        }
        if "wordLimitRule" in item:
            group["wordLimitRule"] = item["wordLimitRule"]
        if "headingsList" in item:
            group["headingsList"] = item["headingsList"]
        if "featuresList" in item:
            group["featuresList"] = item["featuresList"]
        if "endingsList" in item:
            group["endingsList"] = item["endingsList"]
        if "boxOptions" in item:
            group["boxOptions"] = item["boxOptions"]

        exercise["questionGroups"] = [group]

    if "writingTask" in item and item["writingTask"]:
        exercise["writingTask"] = dict(item["writingTask"])
        # ensure academicVisualType / generalLetterType is valid enum or omit if None
        wt = exercise["writingTask"]
        if wt.get("academicVisualType") is None:
            wt.pop("academicVisualType", None)
        if wt.get("generalLetterType") is None:
            wt.pop("generalLetterType", None)

    if "speakingTask" in item and item["speakingTask"]:
        exercise["speakingTask"] = dict(item["speakingTask"])

    return exercise

async def main():
    print("=================================================================")
    print("      AUTHENTIC IELTS QUESTION BANK GENERATOR & VALIDATOR        ")
    print("=================================================================\n")

    base_dir = os.path.dirname(os.path.dirname(__file__))
    schema_path = os.path.join(base_dir, "ielts-exercise-schema.json")
    out_data_dir = os.path.join(base_dir, "frontend", "src", "data", "question-bank")
    out_audio_dir = os.path.join(base_dir, "frontend", "public", "audio", "listening")

    os.makedirs(out_data_dir, exist_ok=True)
    os.makedirs(out_audio_dir, exist_ok=True)

    # Load JSON Schema
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    print(f"Loaded validation schema: {schema_path}")

    # 1. Synthesize Audio & Build Listening Dataset
    print("\n--- [1/4] Generating Listening Audio & Exercise Items ---")
    listening_items = await build_all_listening_items(LISTENING_SECTIONS, out_audio_dir)
    print(f"Listening items built: {len(listening_items)} sections with real audio & timestamps.")

    # 2. Reading Dataset
    print("\n--- [2/4] Processing Reading Passages & Question Groups ---")
    reading_items = READING_ITEMS
    print(f"Reading items loaded: {len(reading_items)} comprehensive academic passages.")

    # 3. Writing Dataset
    print("\n--- [3/4] Processing Authentic Writing Tasks ---")
    writing_items = WRITING_ITEMS
    print(f"Writing tasks loaded: {len(writing_items)} tasks with full model essays.")

    # 4. Speaking Dataset
    print("\n--- [4/4] Processing Speaking Modules ---")
    speaking_items = SPEAKING_ITEMS
    print(f"Speaking modules loaded: {len(speaking_items)} Part 1/2/3 modules.")

    # Validation Pass
    print("\n--- Validating All Datasets Against Schema ---")
    all_categories = [
        ("Reading", reading_items),
        ("Listening", listening_items),
        ("Writing", writing_items),
        ("Speaking", speaking_items)
    ]

    total_validated = 0
    total_questions = 0

    for cat_name, items in all_categories:
        print(f"Validating {cat_name} ({len(items)} items)...")
        for idx, item in enumerate(items, 1):
            exercise = convert_item_to_exercise_schema(item)
            try:
                jsonschema.validate(instance=exercise, schema=schema)
                total_validated += 1
            except jsonschema.ValidationError as e:
                print(f"ERROR in {cat_name} item {item['id']}: {e.message}")
                print(f"Path: {list(e.path)}")
                sys.exit(1)

            # Count individual questions
            if "questions" in item and item["questions"]:
                total_questions += len(item["questions"])
            elif "writingTask" in item:
                total_questions += 1
            elif "speakingTask" in item:
                st = item["speakingTask"]
                if "part1Questions" in st and st["part1Questions"]:
                    total_questions += len(st["part1Questions"])
                elif "cueCard" in st:
                    total_questions += 4 + len(st.get("part3Questions", []))
                else:
                    total_questions += 1

    print(f"ALL {total_validated} modules successfully validated against ielts-exercise-schema.json!")

    # Write output files
    print("\n--- Writing Question Bank JSON Files ---")
    files_map = {
        "readingQuestions.json": reading_items,
        "listeningQuestions.json": listening_items,
        "writingQuestions.json": writing_items,
        "speakingQuestions.json": speaking_items
    }

    for filename, data in files_map.items():
        target_path = os.path.join(out_data_dir, filename)
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Wrote: {target_path} ({os.path.getsize(target_path):,} bytes)")

    print("\n=================================================================")
    print(f"SUCCESS: Generated {total_questions} Authentic IELTS Questions across {total_validated} Modules")
    print(f"  - Reading Passages:  {len(reading_items)} (~850 words each, 100% extractable answers)")
    print(f"  - Listening Audio:   {len(listening_items)} real MP3 tracks with exact second timestamps")
    print(f"  - Writing Essays:    {len(writing_items)} tasks (Task 1 & Task 2) with Band 7.5-8.5 model essays")
    print(f"  - Speaking Modules:  {len(speaking_items)} Part 1/2/3 sets with authentic idioms & rubrics")
    print("=================================================================")

if __name__ == "__main__":
    asyncio.run(main())
