"""
Audio Synthesis and Timestamp Engine for IELTS Listening
Uses Edge-TTS with authentic British Neural voices (en-GB-SoniaNeural, en-GB-RyanNeural, en-GB-ThomasNeural)
to synthesize real multi-speaker dialogue tracks, measures exact segment durations using ffprobe,
calculates accurate timestamps for each question, and concatenates audio via ffmpeg.
"""

import asyncio
import hashlib
import os
import subprocess
import tempfile
import edge_tts

def get_audio_duration(file_path: str) -> float:
    """Uses ffprobe to obtain exact audio duration in seconds."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Warning: could not get duration for {file_path}: {e}")
        return 2.5

def format_timestamp(seconds: float) -> str:
    """Formats float seconds into standard MM:SS string."""
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

async def synthesize_section_audio(section: dict, output_dir: str) -> dict:
    """
    Synthesizes multi-speaker turns, calculates real question timestamps,
    and produces the final master MP3 file in output_dir.
    Reuses cached chunks if available to allow instant re-runs.
    """
    audio_filename = section["audioFilename"]
    final_audio_path = os.path.join(output_dir, audio_filename)
    chunks_dir = os.path.join(output_dir, ".chunks", section["id"])
    os.makedirs(chunks_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    turns = section["turns"]
    turn_start_times = []
    current_time = 0.0

    print(f"  [TTS] Processing '{section['title']}' ({len(turns)} turns)...")

    chunk_files = []
    regenerate_master = not os.path.exists(final_audio_path)

    for idx, (voice, speaker, text) in enumerate(turns):
        t_hash = hashlib.md5(f"{voice}:{text}".encode("utf-8")).hexdigest()[:10]
        chunk_file = os.path.join(chunks_dir, f"t{idx:02d}_{t_hash}.mp3")
        if not os.path.exists(chunk_file) or os.path.getsize(chunk_file) == 0:
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(chunk_file)
            regenerate_master = True

        turn_start_times.append(current_time)
        duration = get_audio_duration(chunk_file)
        current_time += duration + 0.4  # add 400ms natural conversational pause
        chunk_files.append(chunk_file)

    if regenerate_master:
        concat_list_path = os.path.join(chunks_dir, "concat.txt")
        with open(concat_list_path, "w", encoding="utf-8") as f:
            for cf in chunk_files:
                f.write(f"file '{cf}'\n")

        concat_cmd = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", concat_list_path,
            "-c:a", "libmp3lame", "-b:a", "128k",
            final_audio_path
        ]
        subprocess.run(concat_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    total_duration = get_audio_duration(final_audio_path)
    print(f"  [TTS] Completed '{audio_filename}' -> {total_duration:.1f}s ({format_timestamp(total_duration)})")

    # Construct verbatim audio transcript
    transcript_lines = []
    for _, speaker, text in turns:
        transcript_lines.append(f"[{speaker}]: {text}")
    transcript = "\n\n".join(transcript_lines)

    # Process and assign precise timestamps to questions
    def process_q_timestamp(q: dict) -> dict:
        target_turn = q.get("targetTurn", 0)
        timestamp_sec = turn_start_times[target_turn] if target_turn < len(turn_start_times) else 0.0
        ts_str = format_timestamp(timestamp_sec)

        updated_q = dict(q)
        updated_q.pop("targetTurn", None)
        updated_q["paragraphRef"] = f"Audio timestamp {ts_str}"
        orig_exp = updated_q.get("explanation", "")
        updated_q["explanation"] = f"Audio {ts_str}: {orig_exp}"
        return updated_q

    formatted_questions = [process_q_timestamp(q) for q in section.get("questions", [])]

    formatted_groups = []
    if "questionGroups" in section and section["questionGroups"]:
        for grp in section["questionGroups"]:
            u_grp = dict(grp)
            u_grp["questions"] = [process_q_timestamp(q) for q in grp.get("questions", [])]
            formatted_groups.append(u_grp)

    # Build the final QuestionBankItem
    material = section.get("material", {})
    material["type"] = "audio"
    material["title"] = f"Official Listening Audio Track: {section['title']}"
    material["audioUrl"] = f"/audio/listening/{audio_filename}"
    material["audioTranscript"] = transcript

    item = {
        "id": section["id"],
        "skill": "listening",
        "questionType": section["questionType"],
        "difficulty": section["difficulty"],
        "band": section["band"],
        "granularity": section["granularity"],
        "title": section["title"],
        "topic": section["topic"],
        "material": material,
        "questions": formatted_questions
    }
    if formatted_groups:
        item["questionGroups"] = formatted_groups
    if "wordLimitRule" in section:
        item["wordLimitRule"] = section["wordLimitRule"]

    return item
        "skill": "listening",
        "questionType": section["questionType"],
        "difficulty": section["difficulty"],
        "band": section["band"],
        "granularity": section["granularity"],
        "title": section["title"],
        "topic": section["topic"],
        "material": material,
        "questions": formatted_questions
    }
    if "wordLimitRule" in section:
        item["wordLimitRule"] = section["wordLimitRule"]

    return item

async def build_all_listening_items(sections: list, output_dir: str) -> list:
    items = []
    for s in sections:
        item = await synthesize_section_audio(s, output_dir)
        items.append(item)
    return items
