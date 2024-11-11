import tensorflow as tf
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the model and tokenizer (adjust the file paths as necessary)
model = tf.keras.models.load_model('models/phishing_gru_model.h5')
with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

@app.route('/analyze', methods=['POST'])
def analyze_url():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    # Preprocess the URL (ensure it matches the preprocessing done during training)
    processed_input = preprocess_input(url)
    prediction = model.predict(processed_input)

    # Get the predicted class (modify depending on how your model returns predictions)
    prediction_class = np.argmax(prediction, axis=1)

    return jsonify({'prediction': int(prediction_class[0])})

def preprocess_input(url):
    # Tokenize and pad the URL
    tokens = tokenizer.texts_to_sequences([url])
    padded_tokens = tf.keras.preprocessing.sequence.pad_sequences(tokens, maxlen=100, padding='post', truncating='post')
    return padded_tokens

if __name__ == '__main__':
    app.run(debug=True)
