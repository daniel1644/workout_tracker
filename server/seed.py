# seed.py
#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import bcrypt

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Workout, Exercise, Set

fake = Faker()

with app.app_context():

    print("Deleting all records...")
    User.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    Set.query.delete()

    print("Creating users...")

    users = []
    for i in range(20):
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=bcrypt.hashpw(fake.password().encode('utf-8'), bcrypt.gensalt()),
        )
        users.append(user)

    db.session.add_all(users)

    print("Creating workouts...")
    workouts = []
    for i in range(100):
        workout = Workout(
            name=fake.word(),
            date=fake.date_time(),
            user=rc(users)
        )
        workouts.append(workout)

    db.session.add_all(workouts)

    print("Creating exercises...")
    exercises = []
    for i in range(200):
        exercise = Exercise(
            name=fake.word(),
            workout=rc(workouts)
        )
        exercises.append(exercise)

    db.session.add_all(exercises)

    print("Creating sets...")
    sets = []
    for i in range(400):
        set = Set(
            weight=randint(10, 50),
            reps=randint(5, 15),
            exercise=rc(exercises)
        )
        sets.append(set)

    db.session.add_all(sets)

    db.session.commit()
    print("Complete.")

