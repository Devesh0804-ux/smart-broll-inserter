import React from "react";

export default function Transcript({ transcript }) {
  if (!transcript.length) return null;

  return (
    <div>
      <h3>Transcript</h3>
      <ul>
        {transcript.map((seg, idx) => (
          <li key={idx}>
            <strong>
              {seg.start}s – {seg.end}s:
            </strong>{" "}
            {seg.text}
          </li>
        ))}
      </ul>
    </div>
  );
}
