import React from "react";

export default function Timeline({ timeline }) {
  if (!timeline) return null;

  return (
    <div>
      <h3>Timeline Plan</h3>
      <p>A-roll duration: {timeline.a_roll_duration}s</p>

      <ul>
        {timeline.insertions.map((ins, idx) => (
          <li key={idx}>
            <strong>{ins.start_sec}s</strong> → B-roll: {ins.broll_id} |
            Duration: {ins.duration_sec}s | Confidence: {ins.confidence}
            <br />
            <em>{ins.reason}</em>
          </li>
        ))}
      </ul>
    </div>
  );
}
