import json
import os
from typing import List, Dict

from services.transcribe import transcribe_video
from services.matching import match_brolls


def generate_timeline(
    video_path: str,
    output_path: str = "outputs/timeline.json"
) -> Dict:
    """
    Full pipeline:
    A-roll video → transcript → B-roll matches → timeline JSON
    """

    # 1. Transcribe A-roll
    transcript = transcribe_video(video_path)

    # 2. Match B-rolls
    matches = match_brolls(transcript)

    # 3. Estimate A-roll duration (last segment end)
    a_roll_duration = round(transcript[-1]["end"], 2) if transcript else 0.0

    # 4. Build timeline insertions
    insertions = []
    for match in matches:
        insertions.append({
            "start_sec": match["timestamp"],
            "duration_sec": match["duration"],
            "broll_id": match["broll_id"],
            "confidence": match["similarity"],
            "reason": "Semantic match between transcript and B-roll description"
        })

    timeline = {
        "a_roll_duration": a_roll_duration,
        "insertions": insertions
    }

    # 5. Ensure outputs directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 6. Save JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(timeline, f, indent=2)

    return timeline
