from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# TODO: Load the trained model from the shared volume (use the correct path)
model = ...

@app.route('/predict', methods=['POST'])
def predict():
    # TODO: Get the input array from the request body
    get_json = request.get_json()
    iris_input = get_json['input']

    # TODO: Make prediction using the model 
    # HINT: use np.array().reshape(1, -1) to convert input to 2D array
    prediction = ...

    # TODO: Return the prediction as a response
    return ...

@app.route('/')
def hello():
    return 'Welcome to Docker Lab'

if __name__ == '__main__':
    # TODO: Run the Flask app (bind it to port 8080 or anyt other port)
    app.run(debug=True, port=8080, host='0.0.0.0')
