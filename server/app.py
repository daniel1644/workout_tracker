#!/usr/bin/env python3
import os

# Remote library imports
from flask import Flask, request, make_response
from flask_restful import Resource, Api

# Local imports
from config import app, db
from models import User, Workout, Exercise, Set
from auth import AuthResource, ProtectedResource

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

    def post(self):
        try:
            new_user = User(
                username=request.get_json()["username"],
                email=request.get_json()["email"]
            )
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

class UserByIdResource(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).one_or_none()
        if user is not None:
            return make_response(user.to_dict(), 200)
        else:
            return make_response({"error": "User not found"}, 404)

    def delete(self, id):
        user = User.query.filter_by(id=id).one_or_none()
        if user is None:
            return make_response({"error": "User not found"}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)

class WorkoutResource(Resource):
    def get(self):
        workouts = Workout.query.all()
        return [workout.to_dict() for workout in workouts]

    def post(self):
        try:
            new_workout = Workout(
                name=request.get_json()["name"],
                description=request.get_json()["description"]
            )
            db.session.add(new_workout)
            db.session.commit()
            return make_response(new_workout.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

class WorkoutByIdResource(Resource):
    def get(self, id):
        workout = Workout.query.filter_by(id=id).one_or_none()
        if workout is not None:
            return make_response(workout.to_dict(), 200)
        else:
            return make_response({"error": "Workout not found"}, 404)

    def delete(self, id):
        workout = Workout.query.filter_by(id=id).one_or_none()
        if workout is None:
            return make_response({"error": "Workout not found"}, 404)
        db.session.delete(workout)
        db.session.commit()
        return make_response({}, 204)

class ExerciseResource(Resource):
    def get(self):
        exercises = Exercise.query.all()
        return [exercise.to_dict() for exercise in exercises]

    def post(self):
        try:
            new_exercise = Exercise(
                name=request.get_json()["name"],
                description=request.get_json()["description"]
            )
            db.session.add(new_exercise)
            db.session.commit()
            return make_response(new_exercise.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

class ExerciseByIdResource(Resource):
    def get(self, id):
        exercise = Exercise.query.filter_by(id=id).one_or_none()
        if exercise is not None:
            return make_response(exercise.to_dict(), 200)
        else:
            return make_response({"error": "Exercise not found"}, 404)

    def delete(self, id):
        exercise = Exercise.query.filter_by(id=id).one_or_none()
        if exercise is None:
            return make_response({"error": "Exercise not found"}, 404)
        db.session.delete(exercise)
        db.session.commit()
        return make_response({}, 204)

class SetResource(Resource):
    def get(self):
        sets = Set.query.all()
        return [set.to_dict() for set in sets]

    def post(self):
        try:
            new_set = Set(
                reps=request.get_json()["reps"],
                weight=request.get_json()["weight"],
                exercise_id=request.get_json()["exercise_id"],
                workout_id=request.get_json()["workout_id"]
            )
            db.session.add(new_set)
            db.session.commit()
            return make_response(new_set.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)

class SetByIdResource(Resource):
    def get(self, id):
        set = Set.query.filter_by(id=id).one_or_none()
        if set is not None:
            return make_response(set.to_dict(), 200)
        else:
            return make_response({"error": "Set not found"}, 404)

    def delete(self, id):
        set = Set.query.filter_by(id=id).one_or_none()
        if set is None:
            return make_response({"error": "Set not found"}, 404)
        db.session.delete(set)
        db.session.commit()
        return make_response({}, 204)

api = Api(app)
api.add_resource(AuthResource, '/auth')
api.add_resource(ProtectedResource, '/protected')
api.add_resource(UserResource, '/users')
api.add_resource(UserByIdResource, '/users/<int:id>')
api.add_resource(WorkoutResource, '/workouts')
api.add_resource(WorkoutByIdResource, '/workouts/<int:id>')
api.add_resource(ExerciseResource, '/exercises')
api.add_resource(ExerciseByIdResource, '/exercises/<int:id>')
api.add_resource(SetResource, '/sets')
api.add_resource(SetByIdResource, '/sets/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
    