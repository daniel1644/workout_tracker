// src/pages/WorkoutDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const WorkoutDetails = () => {
  const { id } = useParams(); // Get workout ID from URL
  const [workout, setWorkout] = useState(null);

  useEffect(() => {
    // Fetch workout details from API
    axios.get(`/api/workouts/${id}`)
      .then(response => setWorkout(response.data))
      .catch(error => console.error('Error fetching workout details:', error));
  }, [id]);

  return (
    <div>
      {workout ? (
        <div>
          <h1>{workout.name}</h1>
          <p>Description: {workout.description}</p>
          <p>Duration: {workout.duration} minutes</p>
          <p>Date: {new Date(workout.date).toLocaleDateString()}</p>
          {/* Add more details as needed */}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default WorkoutDetails;
