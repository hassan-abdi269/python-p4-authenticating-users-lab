# server/resources/sessions.py
from flask import request, session
from flask_restful import Resource
from models import User

class Login(Resource):
    def post(self):
        data = request.get_json() or {}
        username = data.get('username')

        if not username:
            return {"error": "Username required"}, 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return {"error": "User not found"}, 404

        session['user_id'] = user.id
        return user.to_dict(), 200


class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return '', 204


class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {}, 401  # return JSON, not string

        user = User.query.get(user_id)
        if not user:
            session.pop('user_id', None)
            return {}, 401  # same fix here

        return user.to_dict(), 200

