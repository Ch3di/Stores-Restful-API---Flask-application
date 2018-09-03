import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        required=True,
        type=str,
        help="You have to specify a username"
    )
    parser.add_argument('password',
        required=True,
        type=str,
        help="You have to specify a username"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.findUserByUsername(data['username']):
            return { "message": "The user " + data['username'] + " has already registred" }, 400

        user = UserModel(**data)
        user.save_to_db()
        return { "message": "The user " + data['username'] + " is registred successfully"}, 201
