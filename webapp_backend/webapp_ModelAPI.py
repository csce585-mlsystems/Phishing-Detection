from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Global variables to store model and tokenizer
model = None
tokenizer = None

def load_resources():
    """Load the model and tokenizer when the app starts."""
    global model, tokenizer
    
    try:
        # Load the trained model
        model = load_model('C:/Users/tyler/Phishing-Detection/phishing_gru_model.keras')
        
        # Load the tokenizer
        with open('C:/Users/tyler/Phishing-Detection/tokenizer.pkl', 'rb') as f:
            tokenizer = pickle.load(f)
            
        return True
    except Exception as e:
        print(f"Error loading resources: {str(e)}")
        return False

def predict_url(url, max_length=100):
    """Predict if a URL is phishing or benign."""
    # Tokenize and pad the sequence
    sequence = tokenizer.texts_to_sequences([url])
    padded_sequence = pad_sequences(sequence, maxlen=max_length)
    
    # Print debug information
    print(f"Input URL: {url}")
    print(f"Tokenized sequence: {sequence}")
    print(f"Padded sequence shape: {padded_sequence.shape}")
    print(f"Padded sequence in Flask: {padded_sequence}")
    
    # Make prediction
    prediction = model.predict(padded_sequence, verbose=0)[0][0]
    
    # Print debug information
    print(f"Raw prediction: {prediction}")
    
    return {
        'url': url,
        'prediction': float(prediction),
        'classification': 'phishing' if prediction >= 0.5 else 'benign',
        'confidence': float(prediction if prediction > 0.5 else 1 - prediction)
    }

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
        'status': 'healthy',
        'model_loaded': model is not None,
        'tokenizer_loaded': tokenizer is not None
    })

if __name__ == '__main__':
    # Load resources immediately when starting the app
    if not load_resources():
        print("Warning: Failed to load model or tokenizer")
    
    # Run the app
    app.run(debug=True, port=5000)