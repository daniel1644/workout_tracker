// src/pages/Profile.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState({});

  useEffect(() => {
    axios.get('/api/profile') // Adjust API endpoint as needed
      .then(response => setUser(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Your Profile</h1>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      {/* Add form to update user info */}
    </div>
  );
};

export default Profile;
