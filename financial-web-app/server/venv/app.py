from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import requests

app = Flask(__name__)
CORS(app)

# Set OpenAI API key
openai.api_key = "your-openai-api-key"

@app.route('/api/generate-text', methods=['POST'])
def generate_text():
    user_input = request.json.get('input')
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=user_input,
        max_tokens=150
    )
    text = response.choices[0].text.strip()
    return jsonify({'response': text})

@app.route('/api/stock-data', methods=['GET'])
def get_stock_data():
    stock_symbol = request.args.get('symbol', 'AAPL')
    api_url = f"https://api.twelvedata.com/time_series?symbol={stock_symbol}&interval=1day&apikey=your-api-key"
    data = requests.get(api_url).json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
