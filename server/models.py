# models.py
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

from config import db

bcrypt = Bcrypt()



class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False) 

    user_workouts = db.relationship('Workout', back_populates='user', cascade="all, delete")

    serialize_rules = ('-user_workouts.user',)

    workouts = association_proxy('user_workouts', 'workout', creator=lambda workout_obj: Workout(user=workout_obj))

    @classmethod
    def create(cls, username, email, password):
        try:
            user = cls(username=username, email=email)
            user.password = password
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        try:
            self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        except Exception as e:
            print(f"Error setting password: {e}")
            raise ValueError("Error setting password")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username cannot be empty")
        return username

    def validate_email(self, key, email):
        if not email:
            raise ValueError("Email cannot be empty")
        return email

    def __repr__(self):
        return f"<User {self.username}>"


class Workout(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='user_workouts')

    workout_exercises = db.relationship('Exercise', back_populates='workout', cascade="all, delete")

    serialize_rules = ('-workout_exercises.workout',)

    exercises = association_proxy('workout_exercises', 'exercise', creator=lambda exercise_obj: Exercise(workout=exercise_obj))

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    @validates('date')
    def validate_date(self, key, date):
        if not date:
            raise ValueError("Date cannot be empty")
        return date

    def __repr__(self):
        return f"<Workout {self.name}>"


class Exercise(db.Model, SerializerMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    workout = db.relationship('Workout', back_populates='workout_exercises')

    exercise_sets = db.relationship('Set', back_populates='exercise', cascade="all, delete")

    serialize_rules = ('-exercise_sets.exercise',)

    sets = association_proxy('exercise_sets', 'set', creator=lambda set_obj: Set(exercise=set_obj))

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    def __repr__(self):
        return f"<Exercise {self.name}>"


class Set(db.Model, SerializerMixin):
    __tablename__ = "sets"

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)

    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    exercise = db.relationship('Exercise', back_populates='exercise_sets')

    @validates('weight')
    def validate_weight(self, key, weight):
        if weight <= 0:
            raise ValueError("Weight must be greater than 0")
        return weight

    @validates('reps')
    def validate_reps(self, key, reps):
        if reps <= 0:
            raise ValueError("Reps must be greater than 0")
        return reps

    def __repr__(self):
        return f"<Set {self.weight} {self.reps}>"


