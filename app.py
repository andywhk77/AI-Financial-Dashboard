from flask import Flask, render_template, request, jsonify
import openai
import yfinance as yf

# Initialize Flask app
app = Flask(__name__)

# OpenAI API configuration
openai.api_key = "YOUR_OPENAI_API_KEY"

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route for financial data
@app.route('/financial_data', methods=['POST'])
def financial_data():
    stock_symbol = request.json.get('symbol', 'AAPL')
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period='1d')
    price = data['Close'][0]
    return jsonify({"symbol": stock_symbol, "price": price})

# Route for AI-generated content
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
    app.run(debug=True)
