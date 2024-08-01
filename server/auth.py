# auth.py

from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models import User
from flask_restful import Resource

class AuthResource(Resource):
    def post(self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')

        user = User.query.filter_by(username=username).one_or_none()
        if user is None or not user.check_password(password):
            return make_response(jsonify({'error': 'Invalid credentials'}), 401)

        access_token = create_access_token(identity=username)
        return make_response(jsonify({'access_token': access_token}), 200)

class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).one_or_none()
        if user is None:
            return make_response(jsonify({'error': 'User not found'}), 404)
        response = {'message': f'Hello, {current_user}!'}
        response.update(user.to_dict())  # assuming User model has a to_dict method
        return make_response(jsonify(response), 200)