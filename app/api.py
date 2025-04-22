from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/anomalies', methods=['GET'])
def get_anomalies():
    with open("data/anomalies.json", "r") as file:
        anomalies = json.load(file)
    return jsonify(anomalies)



app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask App!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)

