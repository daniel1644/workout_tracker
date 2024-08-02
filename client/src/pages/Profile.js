import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data from API
    axios.get('/api/users/me')
      .then(response => setUser(response.data))
      .catch(error => console.error('Error fetching user data:', error));
  }, []);

  return (
    <div>
      {user ? (
        <div>
          <h1>{user.username}'s Profile</h1>
          <p>Email: {user.email}</p>
          {/* Add more user details here */}
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Profile;