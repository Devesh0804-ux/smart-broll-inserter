from dotenv import load_dotenv
import os

load_dotenv()

print("API key loaded:", os.getenv("OPENAI_API_KEY") is not None)
from fastapi import FastAPI, UploadFile, File
import shutil
import os

from services.transcribe import transcribe_video

app = FastAPI(title="Smart B-Roll Inserter")


@app.get("/")
def health():
    return {"status": "Backend running"}


@app.post("/transcribe")
async def transcribe_a_roll(file: UploadFile = File(...)):
    """
    Upload A-roll video and return timestamped transcript
    """

    temp_video_path = f"temp_{file.filename}"

    with open(temp_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_video(temp_video_path)

    os.remove(temp_video_path)

    return transcript
