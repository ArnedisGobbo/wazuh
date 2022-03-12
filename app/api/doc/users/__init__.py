from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('users', 'Users related endpoints')

geo_model = namespace.model('Geo', {
    'lat': fields.String(
        required=True,
        description='Street Name'
    ),
    'lng': fields.String(
        required=True,
        description='Suite'
    )
})

address_model = namespace.model('Address', {
    'street': fields.String(
        required=True,
        description='Street Name'
    ),
    'suite': fields.String(
        required=True,
        description='Suite'
    ),
    'city': fields.String(
        required=True,
        description='City Name'
    ),
    'zipcode': fields.String(
        required=True,
        description='ZipCode'
    ),
    'geo': fields.Nested(
        geo_model,
        description='Geo Location'
    )
})

company_model = namespace.model('Company', {
    'name': fields.String(
        required=True,
        description='Company Name'
    ),
    'catchPhrase': fields.String(
        required=True,
        description='catchPhrase'
    ),
    'bs': fields.String(
        required=True,
        description='Business'
    )
})

user_model = namespace.model('User', {
    'id': fields.Integer(
        required=True,
        description='User ID'
    ),
    'name': fields.Integer(
        required=True,
        description='User Name'
    ),
    'email': fields.String(
        required=True,
        description='Email'
    ),
    'address': fields.Nested(
        address_model,
        description='User Address'
    ),
    'phone': fields.String(
        required=True,
        description='Phone'
    ),
    'website': fields.String(
        required=True,
        description='Website'
    ),
    'company': fields.Nested(
        company_model,
        description='User Company'
    )
})

user_list_model = namespace.model('TaskList', {
    'total_items': fields.Integer(
        description='Total items number'
    ),
    'data': fields.Nested(
        user_model,
        description='List of tasks',
        as_list=True
    )
})

user_example = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}


@namespace.route('')
class Users(Resource):
    @namespace.response(500, 'Internal Server error')
    def get(self):
        """Get all users"""
        user_list = [user_example]

        return {
            'data': user_list,
            'total_items': len(user_list)
        }

    @namespace.response(500, 'Internal Server error')
    @namespace.expect(user_model, as_list=True)
    @namespace.marshal_with(user_list_model, as_list=True, code=HTTPStatus.CREATED)
    def post(self):
        """Create a new user"""

        user_list = request.json

        return {
                   'data': user_list,
                   'total_items': len(user_list)
               }, 201


@namespace.route('/<int:user_id>')
class User(Resource):
    @namespace.response(500, 'Internal Server error')
    def get(self, user_id):
        """Get user by id"""
        user_example['id'] = user_id
        user_list = [user_example]

        return {
            'data': user_list,
            'total_items': len(user_list)
        }
