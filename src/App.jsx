import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header";
import Main from "./components/Main/Main";
import SpeechToText from "./components/Main/SpeechToText";
import TextToSpeech from "./components/Main/TextToSpeech";
import VideoProcessing from "./components/Main/VideoProcessing";
import "./app.css";

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-blue-500 flex flex-col">
        <Header />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/speech-to-text" element={<SpeechToText />} />
          <Route path="/text-to-speech" element={<TextToSpeech />} />
          <Route path="/video-processing" element={<VideoProcessing />} />
        </Routes>
      </div>
    </Router>
  );
}
