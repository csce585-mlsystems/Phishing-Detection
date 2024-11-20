import React, { useState } from 'react';

const PhishingDetector = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    if (!url) {
      setError('Please enter a URL');
      setLoading(false);
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        throw new Error('Failed to analyze URL');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '20px auto', padding: '20px' }}>
      <h1>URL Phishing Detector</h1>
      <p>Enter a URL to analyze if it's potentially a phishing site</p>

      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '20px' }}>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter URL (e.g., https://example.com)"
            style={{ 
              width: '70%',
              padding: '8px',
              marginRight: '10px'
            }}
          />
          <button
            type="submit"
            disabled={loading}
            style={{ 
              padding: '8px 16px',
              backgroundColor: '#007bff',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: loading ? 'not-allowed' : 'pointer'
            }}
          >
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>

        {error && (
          <div style={{ 
            padding: '10px', 
            backgroundColor: '#ffebee', 
            color: '#c62828',
            marginBottom: '10px',
            borderRadius: '4px'
          }}>
            {error}
          </div>
        )}

        {result && (
          <div style={{ 
            padding: '20px', 
            backgroundColor: '#f5f5f5',
            borderRadius: '4px'
          }}>
            <h3>Analysis Results:</h3>
            <p>Classification: <strong style={{ 
              color: result.classification === 'phishing' ? '#c62828' : '#2e7d32'
            }}>
              {result.classification}
            </strong></p>
            <p>Confidence: {(result.confidence * 100).toFixed(1)}%</p>
            <p>Raw Score: {result.prediction.toFixed(4)}</p>
          </div>
        )}
      </form>
    </div>
  );
};

export default PhishingDetector;