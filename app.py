from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Palm Oil Forecast API is running!"})

@app.route("/forecast")
def forecast():
    # Örnek tahmini fiyat verisi (daha sonra gerçek verilerle değiştirilebilir)
    days = list(range(1, 31))
    base_price = 950
    prices = [round(base_price + random.uniform(-20, 25), 2) for _ in days]
    return jsonify({"days": days, "prices": prices})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
