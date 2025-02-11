import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    age = int(data["age"])
    likes_sweet = int(data["likes_sweet"])
    color = data["color"].strip().lower()

    color_map = {"red": 0, "blue": 1, "green": 2}
    color = color_map.get(color, 0) 

    prediction = model.predict(np.array([[age, likes_sweet, color]]))[0]
    result = "Coffee" if prediction == 1 else "Tea"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
