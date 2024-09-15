import React, { useState } from 'react';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchRandomUser = async () => {
    try {
      setLoading(true);
      const response = await fetch('/random-user');
      const data = await response.json();
      
      if (response.ok) {
        setUser(data);
        setError(null);
      } else {
        setError('Failed to fetch user data');
      }
    } catch (err) {
      setError('An error occurred: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={fetchRandomUser}>Fetch Random User</button>
        {loading && <p>Loading...</p>}
        {error && <p>Error: {error}</p>}
        {user && (
          <div>
            <p><strong>Name:</strong> {user.name}</p>
            <p><strong>Location:</strong> {user.Location}</p>
            <p><strong>Age:</strong> {user.age}</p>
            {/* Add more fields as needed */}
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
