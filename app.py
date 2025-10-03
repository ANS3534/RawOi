from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Palm Oil Forecast API is running!"}

@app.route("/forecast")
def forecast():
    # örnek tahmin verisi
    prices = [850 + random.randint(-5, 10) for _ in range(7)]
    return jsonify({"days": list(range(1, 8)), "prices": prices})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
