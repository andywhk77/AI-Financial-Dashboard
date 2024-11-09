import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

from flask import Flask, render_template, request, jsonify
import openai
import yfinance as yf
from config import OPENAI_API_KEY

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/financial_data', methods=['POST'])
def financial_data():
    stock_symbol = request.json.get('symbol', 'AAPL')
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period='1mo')
    prices = data['Close'].tolist()
    dates = data.index.strftime('%Y-%m-%d').tolist()
    return jsonify({"symbol": stock_symbol, "prices": prices, "dates": dates})

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt', '')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    ai_text = response.choices[0].text.strip()
    return jsonify({"generated_text": ai_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
