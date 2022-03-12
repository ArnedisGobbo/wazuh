from flask import request, Blueprint
from flask_restx import Api, Resource

from app.api.tasks.schemas import TaskSchema
from app.api.models.tasks import Task
from app.common.error_handling import ObjectNotFound

tasks_bp = Blueprint('tasks_bp', __name__)

task_schema = TaskSchema()

api = Api(tasks_bp)


class TaskListResource(Resource):
    @staticmethod
    def get():
        filter_by_title = request.args.get('title', default='', type=str)
        filter_by_completed = request.args.get('completed', default=None, type=lambda v: v.lower() == 'true')

        if filter_by_completed is not None:
            tasks = Task.filter_by_title_and_completed(completed=filter_by_completed, title=filter_by_title)
        else:
            tasks = Task.filter_by_title(title=filter_by_title)

        result = task_schema.dump(tasks, many=True)
        return result

    def post(self):
        data = request.get_json()
        tasks = task_schema.load(data, many=True)
        for task_dict in tasks:
            self.save_task(task_dict)
        resp = task_schema.dump(tasks, many=True)
        return resp, 201

    @staticmethod
    def save_task(task_dict):
        task = Task(_id=task_dict['id'],
                    title=task_dict['title'],
                    completed=task_dict['completed'],
                    user_id=task_dict['user_id'],
                    )
        task.save()


class TaskResource(Resource):
    @staticmethod
    def get(task_id):
        task = Task.get_by_id(task_id)
        if task is None:
            raise ObjectNotFound('Task not found')
        resp = task_schema.dump(task)
        return resp


class UserTaskListResource(Resource):
    @staticmethod
    def get(user_id):
        filter_by_title = request.args.get('title', default='', type=str)
        filter_by_completed = request.args.get('completed', default=None, type=lambda v: v.lower() == 'true')

        if filter_by_completed is not None:
            tasks = Task.filter_by_title_and_completed(
                filter_by_title,
                filter_by_completed,
                Task.user_id == user_id,
            )
        else:
            tasks = Task.filter_by_title(filter_by_title, Task.user_id == user_id)

        result = task_schema.dump(tasks, many=True)
        return result


api.add_resource(TaskListResource, '/api/tasks/', endpoint='task_list_resource')
api.add_resource(TaskResource, '/api/tasks/<int:task_id>', endpoint='task_resource')

api.add_resource(UserTaskListResource, '/api/users/<int:user_id>/tasks', endpoint='user_task_list_resource')
