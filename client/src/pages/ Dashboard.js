// src/pages/Dashboard.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    axios.get('/api/workouts') // Adjust API endpoint as needed
      .then(response => setWorkouts(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Your Workouts</h1>
      <ul>
        {workouts.map(workout => (
          <li key={workout.id}>{workout.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
