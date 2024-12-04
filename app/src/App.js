import React, { useState, useEffect } from 'react';

const PhishingDetector = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [emailLinks, setEmailLinks] = useState([]);
  const [error, setError] = useState(null);
  const [history, setHistory] = useState([]);

  const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';

  useEffect(() => {
    const storedHistory = JSON.parse(localStorage.getItem('phishingHistory')) || [];
    setHistory(storedHistory);
  }, []);

  useEffect(() => {
    localStorage.setItem('phishingHistory', JSON.stringify(history));
  }, [history]);

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
      const response = await fetch(`${backendUrl}/predict`, {
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

      setHistory((prevHistory) => [
        { url, ...data, timestamp: new Date().toISOString() },
        ...prevHistory,
      ]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const clearHistory = () => {
    setHistory([]);
    localStorage.removeItem('phishingHistory');
  };

  const handleFetchEmails = async () => {
    setLoading(true);
    setError(null);
    setEmailLinks([]);

    try {
      const response = await fetch(`${backendUrl}/fetch-emails`, {
        method: 'GET',
      });

      if (!response.ok) {
        throw new Error('Failed to fetch email links');
      }

      const data = await response.json();
      setEmailLinks(data);
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
              marginRight: '10px',
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
              cursor: loading ? 'not-allowed' : 'pointer',
            }}
          >
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
        </div>

        {error && (
          <div
            style={{
              padding: '10px',
              backgroundColor: '#ffebee',
              color: '#c62828',
              marginBottom: '10px',
              borderRadius: '4px',
            }}
          >
            {error}
          </div>
        )}

        {result && (
          <div
            style={{
              padding: '20px',
              backgroundColor: '#f5f5f5',
              borderRadius: '4px',
            }}
          >
            <h3>Analysis Results:</h3>
            <p>
              Classification:{' '}
              <strong
                style={{
                  color: result.classification === 'phishing' ? '#c62828' : '#2e7d32',
                }}
              >
                {result.classification}
              </strong>
            </p>
            <p>Confidence: {(result.confidence * 100).toFixed(1)}%</p>
            <p>Raw Score: {result.prediction.toFixed(4)}</p>
          </div>
        )}
      </form>

      <div style={{ marginTop: '20px' }}>
        <h3>History</h3>
        {history.length === 0 ? (
          <p>No history available</p>
        ) : (
          <div>
            <ul>
              {history.map((entry, index) => (
                <li key={index} style={{ marginBottom: '10px' }}>
                  <p>
                    <strong>URL:</strong> {entry.url}
                  </p>
                  <p>
                    <strong>Classification:</strong>{' '}
                    <span
                      style={{
                        color: entry.classification === 'phishing' ? '#c62828' : '#2e7d32',
                      }}
                    >
                      {entry.classification}
                    </span>
                  </p>
                  <p>
                    <strong>Confidence:</strong> {(entry.confidence * 100).toFixed(1)}%
                  </p>
                  <p>
                    <strong>Analyzed at:</strong>{' '}
                    {new Date(entry.timestamp).toLocaleString()}
                  </p>
                </li>
              ))}
            </ul>
            <button
              onClick={clearHistory}
              style={{
                padding: '8px 16px',
                backgroundColor: '#d32f2f',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer',
              }}
            >
              Clear History
            </button>
          </div>
        )}
      </div>

      <div style={{ marginTop: '20px' }}>
        <button onClick={handleFetchEmails}>Check Gmail for phishing links</button>
        {emailLinks.length > 0 && (
          <div>
            <div
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
                gap: '20px',
                marginTop: '20px',
              }}
            >
              {emailLinks.map((linkData, index) => (
                <div
                  key={index}
                  style={{
                    padding: '15px',
                    border: '1px solid #ddd',
                    borderRadius: '8px',
                    backgroundColor: '#f9f9f9',
                    boxShadow: '0 2px 5px rgba(0, 0, 0, 0.1)',
                  }}
                >
              <p>
                <strong>Link:</strong>{' '}
                <a
                  href={linkData.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{
                    color: '#007bff',
                    textDecoration: 'none',
                    wordBreak: 'break-word',
                  }}
                >
                  {linkData.url}
                </a>
            </p>
            <p>
              <strong>Classification:</strong>{' '}
              <span
                style={{
                  color:
                    linkData.classification === 'phishing'
                      ? '#c62828'
                      : linkData.classification === 'safe'
                      ? '#2e7d32'
                      : '#757575',
                  fontWeight: 'bold',
                }}
              >
                {linkData.classification.toUpperCase()}
              </span>
            </p>
            <p>
              <strong>Confidence:</strong>{' '}
              {(linkData.confidence * 100).toFixed(1)}%
            </p>
          </div>
        ))}
        </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default PhishingDetector;
