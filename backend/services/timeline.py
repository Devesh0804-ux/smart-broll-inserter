import json
import os
from typing import List, Dict


def generate_timeline(
    a_roll_duration: float,
    matches: List[Dict],
    transcript: List[Dict],
    output_path: str = "../outputs/timeline.json"
):
    """
    Generate final timeline JSON for B-roll insertion.
    """

    insertions = []

    for match in matches:
        # Find matching transcript segment for explanation
        reason_text = ""
        for seg in transcript:
            if abs(seg["start"] - match["timestamp"]) < 0.5:
                reason_text = seg["text"]
                break

        insertions.append({
            "start_sec": round(match["timestamp"], 2),
            "duration_sec": match["duration"],
            "broll_id": match["broll_id"],
            "confidence": match["similarity"],
            "reason": f"Speaker discusses {reason_text.lower()}"
        })

    timeline = {
        "a_roll_duration": round(a_roll_duration, 2),
        "insertions": insertions
    }

    # Ensure outputs directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(timeline, f, indent=2)

    return timeline
