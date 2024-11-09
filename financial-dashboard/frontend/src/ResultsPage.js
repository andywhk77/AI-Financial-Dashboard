import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Line } from 'react-chartjs-2';

const ResultsPage = () => {
  const location = useLocation();
  const { symbol, prompt } = location.state;
  const [stockData, setStockData] = useState(null);
  const [aiText, setAiText] = useState('');

  useEffect(() => {
    fetch('/api/financial_data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symbol }),
    })
      .then((res) => res.json())
      .then(setStockData);

    fetch('/api/generate_text', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
    })
      .then((res) => res.json())
      .then((data) => setAiText(data.generated_text));
  }, [symbol, prompt]);

  const chartData = {
    labels: stockData?.dates || [],
    datasets: [
      {
        label: `Stock Prices for ${symbol}`,
        data: stockData?.prices || [],
        borderColor: 'blue',
        backgroundColor: 'lightblue',
      },
    ],
  };

  return (
    <div>
      <h2>Stock Data for {symbol}</h2>
      <Line data={chartData} />
      <h3>AI Insights:</h3>
      <p>{aiText}</p>
    </div>
  );
};

export default ResultsPage;
