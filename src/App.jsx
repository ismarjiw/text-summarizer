import { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSummarize = async () => {
    try {
      setLoading(true); 
      const response = await axios.post('http://localhost:8000/summarize/', { text });
      setSummary(response.data.summary);
      setText("");
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false); 
    }
  };

  return (
    <div>
      <h1>Text Summarizer</h1>
      <textarea value={text} onChange={(e) => setText(e.target.value)} rows="4" placeholder="Enter text to summarize"></textarea>
      <br />
      <button onClick={handleSummarize}>Summarize</button>
      {loading && <p className="loading">Loading...</p>}
      {summary && !loading && (
        <div>
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
