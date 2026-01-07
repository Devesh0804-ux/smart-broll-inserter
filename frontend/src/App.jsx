import React, { useState } from "react";
import Upload from "./components/Upload";
import Transcript from "./components/Transcript";
import Timeline from "./components/Timeline";

function App() {
  const [transcript, setTranscript] = useState([]);
  const [timeline, setTimeline] = useState(null);

  return (
    <div style={{ padding: 20 }}>
      <h1>Smart B-Roll Inserter</h1>

      <Upload
        onTranscriptGenerated={setTranscript}
        onTimelineGenerated={setTimeline}
      />

      <Transcript transcript={transcript} />
      <Timeline timeline={timeline} />
    </div>
  );
}

export default App;
