import whisper
import os

# Load model once (important for performance)
model = whisper.load_model("base")


def transcribe_video(video_path: str):
    """
    Transcribe A-roll video into timestamped segments.
    Returns: List of {start, end, text}
    """

    if not os.path.exists(video_path):
        raise FileNotFoundError("Video file not found")

    result = model.transcribe(video_path)

    transcript = []
    for segment in result["segments"]:
        transcript.append({
            "start": round(segment["start"], 2),
            "end": round(segment["end"], 2),
            "text": segment["text"].strip()
        })

    return transcript
