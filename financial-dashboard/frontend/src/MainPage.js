import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const MainPage = () => {
  const [symbol, setSymbol] = useState('');
  const [prompt, setPrompt] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate('/results', { state: { symbol, prompt } });
  };

  return (
    <div className="p-8">
      <h1 className="text-4xl font-bold mb-4">Financial Dashboard</h1>
      <form onSubmit={handleSubmit}>
        <input className="border p-2 mb-4 w-full" type="text" placeholder="Enter Stock Symbol" value={symbol} onChange={(e) => setSymbol(e.target.value)} />
        <textarea className="border p-2 mb-4 w-full" placeholder="Enter AI Prompt" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
        <button className="bg-blue-500 text-white px-4 py-2 rounded">Submit</button>
      </form>
    </div>
  );
};

export default MainPage;
