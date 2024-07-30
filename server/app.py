#!/usr/bin/env python3

# Remote library imports
from flask import Flask, request
from flask_restful import Resource, Api

# Local imports
from config import app, db
from models import User, Workout, Exercise, Set

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users]

class WorkoutResource(Resource):
    def get(self):
        workouts = Workout.query.all()
        return [workout.to_dict() for workout in workouts]

class ExerciseResource(Resource):
    def get(self):
        exercises = Exercise.query.all()
        return [exercise.to_dict() for exercise in exercises]

class SetResource(Resource):
    def get(self):
        sets = Set.query.all()
        return [set.to_dict() for set in sets]

api = Api(app)
api.add_resource(UserResource, '/users')
api.add_resource(WorkoutResource, '/workouts')
api.add_resource(ExerciseResource, '/exercises')
api.add_resource(SetResource, '/sets')

if __name__ == '__main__':
    app.run(port=5555, debug=True)