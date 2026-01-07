# Smart B-Roll Inserter 🎬

## 1️⃣ Project Overview

Smart B-Roll Inserter is an AI-powered system that analyzes an A-roll video,
understands its spoken content, and automatically generates a timeline plan
for inserting relevant B-roll clips at appropriate moments.

The system:
- Transcribes A-roll video with timestamps
- Performs semantic matching between transcript segments and B-roll descriptions
- Applies simple editorial rules (spacing, confidence threshold, emotional filtering)
- Outputs a structured timeline JSON for video editing
- (Bonus) Can render a final video using FFmpeg

The focus of this project is on **AI reasoning, explainability, and system design**, not UI polish.

---

## 2️⃣ Tech Stack

### Backend
- Python
- FastAPI
- OpenAI API (Whisper + Embeddings)
- FFmpeg (optional video rendering)
- NumPy, scikit-learn

### Frontend
- React (minimal UI)

---

## 3️⃣ How to Run Locally

### 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-xxxx

cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

Frontend
cd frontend
npm install
npm run dev

http://localhost:5173


Outputs
📄 Timeline Plan
outputs/timeline.json
{
  "a_roll_duration": 45.2,
  "insertions": [
    {
      "start_sec": 12.5,
      "duration_sec": 2.5,
      "broll_id": "broll_3",
      "confidence": 0.81,
      "reason": "Speaker discusses uncovered food hygiene"
    }
  ]
}


Final Rendered Video
outputs/final_video.mp4
