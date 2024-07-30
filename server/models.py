# models.py

from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-workouts.user',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    workouts = db.relationship('Workout', backref='user')

    def __repr__(self):
        return f'<User {self.name}>'

class Workout(db.Model, SerializerMixin):
    __tablename__ = 'workouts'

    serialize_rules = ('-exercises.workout',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    exercises = db.relationship('Exercise', backref='workout')

    def __repr__(self):
        return f'<Workout {self.name}>'

class Exercise(db.Model, SerializerMixin):
    __tablename__ = 'exercises'

    serialize_rules = ('-sets.exercise',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    workout_id = db.Column(db.Integer(), db.ForeignKey('workouts.id'))

    sets = db.relationship('Set', backref='exercise')

    def __repr__(self):
        return f'<Exercise {self.name}>'

class Set(db.Model, SerializerMixin):
    __tablename__ = 'sets'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)

    exercise_id = db.Column(db.Integer(), db.ForeignKey('exercises.id'))

    def __repr__(self):
        return f'<Set {self.weight} {self.reps}>'