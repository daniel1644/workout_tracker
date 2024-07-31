# auth.py
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource

from models import User

class AuthResource(Resource):
    def post(self):
        email = request.get_json()["email"]
        password = request.get_json()["password"]
        user = User.query.filter_by(email=email).one_or_none()
        if user is None or not user.check_password(password):
            return make_response(jsonify({"error": "Invalid email or password"}), 401)
        access_token = create_access_token(identity=user.id)
        return make_response(jsonify({"access_token": access_token}), 200)

class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).one_or_none()
        if user is None:
            return make_response(jsonify({"error": "User not found"}), 404)
        response = {"message": f"Hello, {user.name}!"}
        response.update(user.to_dict())  # assuming User model has a to_dict method
        return make_response(jsonify(response), 200)