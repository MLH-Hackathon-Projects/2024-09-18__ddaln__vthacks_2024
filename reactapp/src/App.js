import React, { useState, useEffect } from 'react';
import './App.css';

const getSeverityColor = (severity) => {
  if (severity >= 8) return '#FF4136'; // critical
  if (severity >= 6) return '#FF851B'; // high
  if (severity >= 5) return '#FFDC00'; // medium
  return '#2ECC40'; // low
};

const getSeverityText = (color) => {
  switch (color) {
    case '#FF4136':
      return 'Critical';
    case '#FF851B':
      return 'High';
    case '#FFDC00':
      return 'Medium';
    case '#2ECC40':
      return 'Low';
    default:
      return 'Unknown';
  }
};

function App() {
  const [sortType, setSortType] = useState('severity');
  const [activeTab, setActiveTab] = useState('flagged');
  const [incidents, setIncidents] = useState([]);
  const [flaggedCases, setFlaggedCases] = useState([]);
  const [resolvedCases, setResolvedCases] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Initial fetch
    fetchAllData();

    // Set up interval for fetching data every 5 seconds
    const intervalId = setInterval(fetchAllData, 5000);

    // Clean up interval on component unmount
    return () => clearInterval(intervalId);
  }, [sortType]);

  const fetchAllData = async () => {
    setIsLoading(true);
    setError(null);
    await fetchIncidents();
    await fetchFlaggedCases();
    await fetchResolvedCases();
    setIsLoading(false);
  };

  const fetchIncidents = async () => {
    try {
      const response = await fetch(`http://localhost:5000/incidents?sort=${sortType}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      let data = await response.json();
      // Only reverse the data for severity sorting
      if (sortType === 'severity') {
        data = data.reverse();
      }
      setIncidents(data);
    } catch (error) {
      console.error('Error fetching incidents:', error);
      setError('Failed to fetch incidents. Please try again later.');
      setIncidents([]);
    }
  };

  const fetchFlaggedCases = async () => {
    try {
      const response = await fetch('http://localhost:5000/incidents/flagged');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setFlaggedCases(data);
    } catch (error) {
      console.error('Error fetching flagged cases:', error);
      setFlaggedCases([]);
    }
  };

  const fetchResolvedCases = async () => {
    try {
      const response = await fetch('http://localhost:5000/incidents/resolved');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setResolvedCases(data);
    } catch (error) {
      console.error('Error fetching resolved cases:', error);
      setResolvedCases([]);
    }
  };

  const handleSortChange = (event) => {
    setSortType(event.target.value);
  };

  const handleTabChange = (tab) => {
    setActiveTab(tab);
  };

  const casesToShow = activeTab === 'flagged' ? flaggedCases : resolvedCases;

  return (
    <div className="App">
      <header className="App-header">
        <h1>DispatchIQ</h1>
      </header>

      {isLoading && <div className="loading-indicator">Updating data...</div>}
      {error && <div className="error-message">{error}</div>}

      <div className="content">
        <div className="left-panel">
          <div className="card">
            <div className="tabs">
              <button 
                className={`tab ${activeTab === 'flagged' ? 'active' : ''}`} 
                onClick={() => handleTabChange('flagged')}
              >
                Flagged Cases
              </button>
              <button 
                className={`tab ${activeTab === 'resolved' ? 'active' : ''}`} 
                onClick={() => handleTabChange('resolved')}
              >
                Resolved Cases
              </button>
            </div>
            <div className="case-list">
              {casesToShow.map((incident) => (
                <div key={incident._id} className="case" style={{ borderLeft: `4px solid ${getSeverityColor(Number(incident.severity))}` }}>
                  <span className="priority-indicator" style={{ backgroundColor: getSeverityColor(Number(incident.severity)) }}></span>
                  <p>{incident.emergency_details}</p>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="right-panel">
          <h2>Priority List</h2>
          
          <div className="sort-options">
            <label htmlFor="sort">Sort by:</label>
            <select id="sort" value={sortType} onChange={handleSortChange}>
              <option value="severity">Severity</option>
              <option value="time">Time</option>
            </select>
          </div>

          <table>
            <thead>
              <tr>
                <th>Priority</th>
                <th>Caller</th>
                <th>Issue</th>
                <th>Time</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {incidents.map((incident) => (
                <tr key={incident._id} style={{ backgroundColor: `${getSeverityColor(Number(incident.severity))}22` }}>
                  <td style={{ fontWeight: 'bold', color: getSeverityColor(Number(incident.severity)) }}>{getSeverityText(getSeverityColor(incident.severity))}</td>
                  <td>{incident.name}</td>
                  <td>{incident.emergency_details}</td>
                  <td>{new Date(incident.timestamp).toLocaleTimeString()}</td>
                  <td><button className="resolve-button">Resolve</button></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;