from flask import Flask, request, jsonify
import yfinance as yf
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "Welcome to the Financial Dashboard API!"

@app.route('/api/financial_data', methods=['POST'])
def financial_data():
    symbol = request.json.get('symbol', 'AAPL')
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1mo')
        prices = data['Close'].tolist()
        dates = data.index.strftime('%Y-%m-%d').tolist()
        return jsonify({"symbol": symbol, "prices": prices, "dates": dates})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt', 'Provide financial analysis.')
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        ai_text = response.choices[0].text.strip()
        return jsonify({"generated_text": ai_text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
