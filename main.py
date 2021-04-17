from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)
model = LinearRegression()

@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    LOG.info(f"JSON payload: {json_payload['day']}")
    LOG.info(f"JSON payload: {json_payload['total']}")    
    prediction = model.predict([[json_payload['day'], json_payload['total']]])
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    df = pd.read_csv('national-history-update.csv')
    X = df[['day', 'totalTestResultsIncrease']].values
    y = df['positiveIncrease'].values
    model.fit(X, y)
    app.run(host='127.0.0.1', port=8080, debug=True)
