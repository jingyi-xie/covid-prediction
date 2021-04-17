from flask import Flask, request, jsonify, render_template
from flask.logging import create_logger
import logging
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)
model = LinearRegression()
df = pd.read_csv('national-history-update.csv')
X = df[['day', 'totalTestResultsIncrease']].values
y = df['positiveIncrease'].values
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    if len(request.form) == 0:
        json_payload = request.json
        prediction = model.predict([[json_payload['day'], json_payload['total']]])
        return jsonify({'prediction': prediction[0]})
    day = request.form.get('day')
    total = request.form.get('total')
    prediction = model.predict([[day, total]])
    return render_template("index.html",prediction_text=f"Predicted positive cases: {prediction[0]}")
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
