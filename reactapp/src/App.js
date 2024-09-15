import React, { useState } from 'react';
import './App.css';

function App() {
  const [sortType, setSortType] = useState('time'); // or 'severity'

  const handleSortChange = (event) => {
    setSortType(event.target.value);
    // Implement sorting logic
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>DispatchIQ</h1>
      </header>

      <div className="content">
        {/* Left side - Scrollable list of cases */}
        <div className="left-panel">
          <h2>Cases</h2>
          <div className="case-list">
            {/* Map through cases and render them here */}
            <p>Case 1: Emergency details...</p>
            <p>Case 2: Emergency details...</p>
            {/* Add more cases dynamically */}
          </div>
        </div>

        {/* Right side - Priority list */}
        <div className="right-panel">
          <h2>Priority List</h2>
          
          <div className="sort-options">
            <label htmlFor="sort">Sort by:</label>
            <select id="sort" value={sortType} onChange={handleSortChange}>
              <option value="time">Time</option>
              <option value="severity">Severity</option>
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
              {/* Map through priority list and render rows */}
              <tr>
                <td>1</td>
                <td>John Doe</td>
                <td>Heart Attack</td>
                <td>12:30 PM</td>
                <td><button>Resolve</button></td>
              </tr>
              {/* Add more rows dynamically */}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;
