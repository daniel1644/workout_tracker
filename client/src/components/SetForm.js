import React from 'react';
import { Link } from 'react-router-dom';

function Set({ set }) {
  return (
    <div className="card">
      <h2>
        <Link to={`/sets/${set.id}`}>{set.weight} x {set.reps}</Link>
      </h2>
    </div>
  );
}

export default Set;
