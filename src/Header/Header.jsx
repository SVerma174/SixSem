import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="bg-white shadow p-4 flex justify-between">
      <h1 className="text-xl font-bold">Conversation AI</h1>
      <nav>
        <Link to="/" className="mr-4 text-blue-500">Home</Link>
        <Link to="/speech-to-text" className="mr-4 text-blue-500">Speech to Text</Link>
        <Link to="/text-to-speech" className="mr-4 text-blue-500">Text to Speech</Link>
        <Link to="/video-processing" className="text-blue-500">Video Processing</Link>
      </nav>
    </header>
  );
}
