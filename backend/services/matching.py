from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from services.broll_analysis import load_broll_metadata


def match_brolls(
    transcript: List[Dict],
    similarity_threshold: float = 0.3
) -> List[Dict]:
    """
    Match transcript segments to relevant B-roll clips.

    Returns:
    [
      {
        "timestamp": float,
        "broll_id": str,
        "duration": float,
        "similarity": float
      }
    ]
    """

    brolls = load_broll_metadata()
    broll_descriptions = [b["description"] for b in brolls]

    results = []

    for segment in transcript:
        texts = [segment["text"]] + broll_descriptions

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(texts)

        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        best_idx = similarities.argmax()
        best_score = similarities[best_idx]

        if best_score >= similarity_threshold:
            results.append({
                "timestamp": segment["start"],
                "broll_id": brolls[best_idx]["broll_id"],
                "duration": round(segment["end"] - segment["start"], 2),
                "similarity": round(float(best_score), 2)
            })

    return results
