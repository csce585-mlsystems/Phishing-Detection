from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os
import numpy as np
from flask_cors import CORS
import tensorflow as tf

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
        # Load the trained model
        model = load_model(MODEL_PATH)
        print(f"Model loaded successfully from {MODEL_PATH}")
        
        # Load the tokenizer
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
        # Tokenize and pad the sequence
        sequence = tokenizer.texts_to_sequences([url])
        padded_sequence = pad_sequences(sequence, maxlen=max_length)
        
        # Debugging information
        print(f"Input URL: {url}")
        print(f"Tokenized sequence: {sequence}")
        print(f"Padded sequence shape: {padded_sequence.shape}")
        
        # Make prediction
        prediction = model.predict(padded_sequence, verbose=0)[0][0]
        print(f"Raw prediction: {prediction}")
        
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
    """Endpoint to predict if a URL is phishing or not."""
    # Ensure model and tokenizer are loaded
    if model is None or tokenizer is None:
        if not load_resources():
            return jsonify({'error': 'Model or tokenizer not loaded'}), 500
    
    try:
        # Get URL from request
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'No URL provided'}), 400
            
        url = data['url']
        
        # Make prediction
        result = predict_url(url)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint to verify the service is running and model is loaded."""
    return jsonify({
        'status': 'healthy' if model is not None and tokenizer is not None else 'unhealthy',
        'model_loaded': model is not None,
        'tokenizer_loaded': tokenizer is not None,
        'model_path': MODEL_PATH,
        'tokenizer_path': TOKENIZER_PATH
    })

if __name__ == '__main__':
    # Check for GPU availability
    if tf.config.list_physical_devices('GPU'):
        print("GPU is available and will be used for TensorFlow.")
    else:
        print("No GPU found. Using CPU.")

    # Load resources immediately when starting the app
    if not load_resources():
        print("Warning: Failed to load model or tokenizer")
    
    # Run the app
    app.run(debug=True, port=5000)
