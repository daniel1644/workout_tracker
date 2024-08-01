// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/ Home';
import Dashboard from './pages/ Dashboard';
import Profile from './pages/Profile';
import Login from './pages/Login';
import Register from './pages/ Register';
import ResetPassword from './pages/PasswordReset';
import WorkoutDetails from './pages/WorkoutDetails';
import NotFound from './pages/NotFound';
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <Switch>
          <Route exact path="/" component={Home} />
          <ProtectedRoute path="/dashboard" component={Dashboard} />
          <ProtectedRoute path="/profile" component={Profile} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/reset-password" component={ResetPassword} />
          <Route path="/workouts/:id" component={WorkoutDetails} />
          <Route component={NotFound} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
