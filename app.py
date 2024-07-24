from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

# Example location factors (these should be determined from your model or data)
location_factors = {
    "Madhapur": 1.0,
    "Banjara Hills": 1.5,
    "Gachibowli": 1.2,
    "Jubilee Hills": 1.7,
    "Kondapur": 1.1
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    location = data['location']
    sqft = int(data['sqft'])
    bhk = int(data['bhk'])
    bathrooms = int(data['bathrooms'])

    # Use the location factor in the prediction (this is just an example)
    location_factor = location_factors.get(location, 1.0)
    features = np.array([[sqft, bhk, bathrooms]]) * location_factor
    
    # Predict using the model
    prediction = model.predict(features)[0]

    return jsonify({'price': prediction})

