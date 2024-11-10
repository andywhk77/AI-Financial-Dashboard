// Fetch Stock Data and Display Chart
async function getStockPrice() {
    const symbol = document.getElementById('stock-symbol').value;
    const response = await fetch('/financial_data', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({symbol})
    });
    const data = await response.json();
    const ctx = document.getElementById('stockChart').getContext('2d');
    
    // Create Chart
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [{
                label: `Stock Prices for ${data.symbol}`,
                data: data.prices,
                borderColor: '#007bff',
                borderWidth: 2
            }]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Date' } },
                y: { title: { display: true, text: 'Price (USD)' } }
            }
        }
    });
}

// Generate AI Text Using OpenAI API
async function generateText() {
    const prompt = document.getElementById('text-prompt').value;
    const response = await fetch('/generate_text', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({prompt})
    });
    const data = await response.json();
    document.getElementById('generated-text').textContent = data.generated_text;
}
