// src/pages/Home.js
import React from 'react';
import pic1 from '../logo.png';
import pic2 from '../1.png';
import pic3 from '../2.png';
// import pic4 from '../3.png';
// import pic5 from '../4.png';
import '../pages/home.css'; // Import the CSS file for styling

const Home = () => {
  return (
    <div>
      <h1>Welcome to the Workout Tracker</h1>
      <p>Your journey to a fitter you starts here.</p>
      <div className="image-gallery">
        <img src={pic1} alt="Picture 1" className="img-fluid" />
        <img src={pic2} alt="Picture 2" className="img-fluid" />
        <img src={pic3} alt="Picture 3" className="img-fluid" />
        {/* <img src={pic4} alt="Picture 4" className="img-fluid" /> */}
        {/* <img src={pic5} alt="Picture 5" className="img-fluid" /> */}
      </div>
    </div>
  );
};

export default Home;
