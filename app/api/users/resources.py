from flask import request, Blueprint
from flask_restx import Api, Resource

from app.api.users.schemas import UserSchema
from app.api.models.users import User, Geo, Address, Company
from app.common.error_handling import ObjectNotFound

users_bp = Blueprint('users_bp', __name__)

user_schema = UserSchema()

api = Api(users_bp)


class UserListResource(Resource):
    @staticmethod
    def get():
        users = User.get_all()
        result = user_schema.dump(users, many=True)
        return result

    def post(self):
        data = request.get_json()
        users = user_schema.load(data, many=True)
        for user_dict in users:
            self.save_user(user_dict)
        resp = user_schema.dump(users, many=True)
        return resp, 201

    @staticmethod
    def save_user(user_dict):
        geo = Geo(lat=user_dict['address']['geo']['lat'],
                  lng=user_dict['address']['geo']['lng'])

        address = Address(street=user_dict['address']['street'],
                          suite=user_dict['address']['suite'],
                          city=user_dict['address']['city'],
                          zipcode=user_dict['address']['zipcode'],
                          geo=geo)

        company = Company(name=user_dict['company']['name'],
                          catch_phrase=user_dict['company']['catch_phrase'],
                          bs=user_dict['company']['bs'], )

        user = User(_id=user_dict['id'],
                    name=user_dict['name'],
                    username=user_dict['username'],
                    email=user_dict['email'],
                    address=address,
                    phone=user_dict['phone'],
                    website=user_dict['website'],
                    company=company,
                    )

        user.save()


class UserResource(Resource):
    @staticmethod
    def get(user_id):
        user = User.get_by_id(user_id)
        if user is None:
            raise ObjectNotFound('User not found')
        resp = user_schema.dump(user)
        return resp


api.add_resource(UserListResource, '/api/users/', endpoint='user_list_resource')
api.add_resource(UserResource, '/api/users/<int:user_id>', endpoint='user_resource')
