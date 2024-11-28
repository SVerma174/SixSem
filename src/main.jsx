import React from "react";
import TextToSpeech from "./TextToSpeech";
import SpeechToText from "./SpeechToText";
import TextProcessing from "./TextProcessing";
import VideoProcessing from "./VideoProcessing";
import SearchBox from "./SearchBox";
import "./Main.css"; // Import CSS for Main component

export default function Main() {
  return (
    <main className="flex flex-col items-center flex-grow mt-10 space-y-10 px-4">
      <div className="grid grid-cols-2 gap-6 w-full max-w-4xl">
        <TextToSpeech />
        <SpeechToText />
        <TextProcessing />
        <VideoProcessing />
      </div>
      <div className="w-full max-w-md">
        <SearchBox />
      </div>
    </main>
  );
}
