import React, { useState, useEffect } from 'react';
import './App.css';

const getSeverityColor = (severity) => {
  if (severity >= 8) return '#FF4136'; // critical
  if (severity >= 6) return '#FF851B'; // high
  if (severity >= 5) return '#FFDC00'; // medium
  return '#2ECC40'; // low
};

const getSeverityText = (severity) => {
  if (severity >= 8) return 'Critical';
  if (severity >= 6) return 'High';
  if (severity >= 5) return 'Medium';
  return 'Low';
};

function App() {
  const [sortType, setSortType] = useState('severity');
  const [activeTab, setActiveTab] = useState('flagged');
  const [incidents, setIncidents] = useState([]);
  const [flaggedCases, setFlaggedCases] = useState([]);
  const [resolvedCases, setResolvedCases] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [expandedIncident, setExpandedIncident] = useState(null);

  useEffect(() => {
    fetchAllData();
    const intervalId = setInterval(fetchAllData, 5000);
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
      const response = await fetch(`http://localhost:5000/incidents?sort=${sortType}&flagged=0`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      let data = await response.json();
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

  const toggleIncidentDetails = (incidentId) => {
    setExpandedIncident(expandedIncident === incidentId ? null : incidentId);
  };

  const resolveIncident = async (incidentId) => {
    try {
      const response = await fetch(`http://localhost:5000/resolve/${incidentId}`, {
        method: 'POST',
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }
      // Remove the resolved incident from the incidents state
      setIncidents(incidents.filter(incident => incident._id !== incidentId));
      // Add the resolved incident to the resolvedCases state
      const resolvedIncident = incidents.find(incident => incident._id === incidentId);
      setResolvedCases([...resolvedCases, resolvedIncident]);
      setError(null); // Clear any previous errors
    } catch (error) {
      console.error('Error resolving incident:', error);
      setError(`Failed to resolve incident: ${error.message}`);
    }
  };

  const casesToShow = activeTab === 'flagged' ? flaggedCases : resolvedCases;

  return (
    <div className="App">
      <header className="App-header">
        <h1>DispatchIQ</h1>
      </header>

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
                <React.Fragment key={incident._id}>
                  <tr 
                    onClick={() => toggleIncidentDetails(incident._id)}
                    style={{ 
                      backgroundColor: getSeverityColor(Number(incident.severity)) + '20',
                      cursor: 'pointer'
                    }}
                  >
                    <td style={{ fontWeight: 'bold', color: getSeverityColor(Number(incident.severity)) }}>
                      {getSeverityText(Number(incident.severity))}
                    </td>
                    <td>{incident.name}</td>
                    <td>{incident.emergency_details}</td>
                    <td>{new Date(incident.timestamp).toLocaleString()}</td>
                    <td>
                      {!incident.resolved && (
                        <button 
                          className="resolve-button"
                          onClick={(e) => {
                            e.stopPropagation();
                            resolveIncident(incident._id);
                          }}
                        >
                          Resolve
                        </button>
                      )}
                      {incident.resolved && (
                        <span className="resolved-text">Resolved</span>
                      )}
                    </td>
                  </tr>
                  {expandedIncident === incident._id && (
                    <tr>
                      <td colSpan="5">
                        <div className="incident-details-card">
                          <h3>Incident Details</h3>
                          <p><strong>Severity:</strong> {incident.severity}</p>
                          <p><strong>Name:</strong> {incident.name}</p>
                          <p><strong>Age:</strong> {incident.age || 'N/A'}</p>
                          <p><strong>Location:</strong> {incident.location || 'N/A'}</p>
                          <p><strong>Emergency Details:</strong> {incident.emergency_details}</p>
                          <div className="transcript">
                            <strong>Transcript:</strong>
                            <p>{incident.transcript || 'No transcript available'}</p>
                          </div>
                        </div>
                      </td>
                    </tr>
                  )}
                </React.Fragment>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;