// src/components/WorkoutForm.js
import React, { useState } from 'react';

const WorkoutForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({ name: '', description: '' });

  const handleChange = e => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = e => {
    e.preventDefault();
    onSubmit(formData);
    setFormData({ name: '', description: '' });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <label htmlFor="name" className="form-label">Workout Name</label>
        <input
          type="text"
          className="form-control"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="description" className="form-label">Description</label>
        <textarea
          className="form-control"
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
        />
      </div>
      <button type="submit" className="btn btn-primary">Add Workout</button>
    </form>
  );
};

export default WorkoutForm;
