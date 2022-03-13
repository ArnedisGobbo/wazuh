from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource, fields, reqparse

namespace = Namespace('tasks', 'Tasks related endpoints')

task_model = namespace.model('Task', {
    'user_id': fields.Integer(
        required=True,
        description='User ID'
    ),
    'id': fields.Integer(
        required=True,
        description='Task ID'
    ),
    'title': fields.String(
        required=True,
        description='Task title'
    ),
    'completed': fields.Boolean(
        required=True,
        description='Task is completed'
    )
})

task_list_model = namespace.model('TaskList', {
    'total_items': fields.Integer(
        description='Total items number'
    ),
    'data': fields.Nested(
        task_model,
        description='List of tasks',
        as_list=True
    )
})

task_example = {
    'user_id': 1,
    'id': 1,
    'title': 'Sample title',
    'completed': True,
}

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Task title')
parser.add_argument('completed', type=lambda v: v.lower() == 'true', help='Task is completed')


@namespace.route('')
class Tasks(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(parser)
    def get(self):
        """Get all tasks"""
        title = request.args.get('title') if 'title' in request.args else task_example['title']
        completed = request.args.get('completed', default=task_example['completed'], type=lambda v: v.lower() == 'true')

        task_example['title'] = title
        task_example['completed'] = completed
        task_list = [task_example]

        return {
            'data': task_list,
            'total_items': len(task_list)
        }

    @namespace.response(500, 'Internal Server error')
    @namespace.expect(task_model, as_list=True)
    @namespace.marshal_with(task_list_model, as_list=True, code=HTTPStatus.CREATED)
    def post(self):
        """Create a new task"""

        task_list = request.json

        return {
                   'data': task_list,
                   'total_items': len(task_list)
               }, 201


@namespace.route('/<int:task_id>')
class Task(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(parser)
    def get(self, task_id):
        """Get task by id"""
        title = request.args.get('title') if 'title' in request.args else task_example['title']
        completed = request.args.get('completed') if 'completed' in request.args else task_example['completed']

        task_example['id'] = task_id
        task_example['title'] = title
        task_example['completed'] = completed
        task_list = [task_example]

        return {
            'data': task_list,
            'total_items': len(task_list)
        }


@namespace.route('/<int:user_id>/tasks')
class UserTask(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(parser)
    def get(self, user_id):
        """Get task by id"""
        title = request.args.get('title') if 'title' in request.args else task_example['title']
        completed = request.args.get('completed') if 'completed' in request.args else task_example['completed']

        task_example['user_id'] = user_id
        task_example['title'] = title
        task_example['completed'] = completed
        task_list = [task_example]

        return {
            'data': task_list,
            'total_items': len(task_list)
        }
