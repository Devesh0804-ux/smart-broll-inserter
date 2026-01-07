import React from "react";

export default function Upload({ onTranscriptGenerated, onTimelineGenerated }) {
  const handleUpload = async (e) => {
    e.preventDefault();
    const file = e.target.a_roll.files[0];

    const formData = new FormData();
    formData.append("file", file);

    // Step 1: Transcribe
    const transcriptRes = await fetch("http://localhost:8000/transcribe", {
      method: "POST",
      body: formData,
    });

    const transcript = await transcriptRes.json();
    onTranscriptGenerated(transcript);

    // Step 2: Generate timeline
    const timelineRes = await fetch("http://localhost:8000/generate-timeline", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ transcript }),
    });

    const timeline = await timelineRes.json();
    onTimelineGenerated(timeline);
  };

  return (
    <form onSubmit={handleUpload}>
      <h3>Upload A-roll Video</h3>
      <input type="file" name="a_roll" accept="video/*" required />
      <br />
      <br />
      <button type="submit">Generate Plan</button>
    </form>
  );
}
