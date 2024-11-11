import React, { useState } from 'react';

const UrlAnalyzer = () => {
    // State to hold the URL and the prediction result
    const [url, setUrl] = useState('');
    const [prediction, setPrediction] = useState(null);  // To store prediction result
    const [loading, setLoading] = useState(false);  // To handle loading state

    // Function to handle URL analysis
    const analyzeUrl = async () => {
        if (!url) {
            alert("Please enter a URL to analyze.");
            return;
        }

        setLoading(true);  // Start loading
        try {
            const response = await fetch('http://localhost:5000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url }),
            });

            const result = await response.json();
            setPrediction(result.prediction);  // Update state with prediction result
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while analyzing the URL.');
        }
        setLoading(false);  // Stop loading
    };

    return (
        <div>
            <h2>URL Phishing Analyzer</h2>

            {/* Input field for URL */}
            <input
                type="text"
                placeholder="Enter URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                style={{ padding: '8px', marginBottom: '10px', width: '300px' }}
            />

            {/* Analyze button */}
            <button onClick={analyzeUrl} disabled={loading} style={{ padding: '8px 16px' }}>
                {loading ? 'Analyzing...' : 'Analyze'}
            </button>

            {/* Display the prediction result */}
            {prediction !== null && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Prediction Result:</h3>
                    <p>{prediction === 1 ? 'Phishing URL' : 'Safe URL'}</p>
                </div>
            )}
        </div>
    );
};

export default UrlAnalyzer;
