from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os
import numpy as np
from flask_cors import CORS
import tensorflow as tf
from gmail_API import authenticate_gmail, fetch_links_from_emails

app = Flask(__name__)
CORS(app)

# Global variables for model and tokenizer
model = None
tokenizer = None

# Paths to model and tokenizer
MODEL_PATH = os.path.join(os.getcwd(), "model", "phishing_gru_model.keras")
TOKENIZER_PATH = os.path.join(os.getcwd(), "model", "gru_tokenizer.pkl")

def load_resources():
    """Load the model and tokenizer when the app starts."""
    global model, tokenizer
    try:
        model = load_model(MODEL_PATH)
        print(f"Model loaded successfully from {MODEL_PATH}")
        with open(TOKENIZER_PATH, 'rb') as f:
            tokenizer = pickle.load(f)
        print(f"Tokenizer loaded successfully from {TOKENIZER_PATH}")
        return True
    except Exception as e:
        print(f"Error loading resources: {str(e)}")
        return False

def predict_url(url, max_length=100):
    """Predict if a URL is phishing or benign."""
    try:
        sequence = tokenizer.texts_to_sequences([url])
        padded_sequence = pad_sequences(sequence, maxlen=max_length)
        prediction = model.predict(padded_sequence, verbose=0)[0][0]
        return {
            'url': url,
            'prediction': float(prediction),
            'classification': 'phishing' if prediction >= 0.5 else 'benign',
            'confidence': float(prediction if prediction > 0.5 else 1 - prediction)
        }
    except Exception as e:
        print(f"Error during prediction: {e}")
        return {'error': str(e)}

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or tokenizer is None:
        if not load_resources():
            return jsonify({'error': 'Model or tokenizer not loaded'}), 500
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'No URL provided'}), 400
        url = data['url']
        result = predict_url(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/fetch-emails', methods=['GET'])
def fetch_emails():
    """Endpoint to fetch email links and classify them."""
    if model is None or tokenizer is None:
        if not load_resources():
            return jsonify({'error': 'Model or tokenizer not loaded'}), 500
    
    service = authenticate_gmail()
    if not service:
        return jsonify({'error': 'Failed to authenticate Gmail'}), 500
    
    links = fetch_links_from_emails(service)
    if not links:
        return jsonify({'error': 'No links found in recent emails'}), 404

    results = [predict_url(link) for link in links]
    return jsonify(results)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy' if model is not None and tokenizer is not None else 'unhealthy',
        'model_loaded': model is not None,
        'tokenizer_loaded': tokenizer is not None,
        'model_path': MODEL_PATH,
        'tokenizer_path': TOKENIZER_PATH
    })

if __name__ == '__main__':
    if tf.config.list_physical_devices('GPU'):
        print("GPU is available and will be used for TensorFlow.")
    else:
        print("No GPU found. Using CPU.")
    if not load_resources():
        print("Warning: Failed to load model or tokenizer")
    app.run(debug=True, host='0.0.0.0', port=5000)
