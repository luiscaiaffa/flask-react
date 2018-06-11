from flask import Blueprint
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required)
from flask_restful import Resource, reqparse

from back.common.utils import Utils
from .user import User


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email', type=str, required=True, help="This field cannot be blank.")
_user_parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")


class Login(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = User.find_email(data['email'])

        if user and Utils().check_password(data['password'], user.password):
            access_token = create_access_token(identity=user.email, fresh=True)
            refresh_token = create_refresh_token(user.email)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token
                   }, 200

        return {"message": "Invalid Credentials!"}, 401



class Test(Resource):
    @jwt_required
    def get(self):
        print("entrou")
        return {"message": "Credentials ok!"}, 200