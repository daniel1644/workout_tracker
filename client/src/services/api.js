// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5555', // Update to your backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common['Authorization'];
  }
};

export default api;
