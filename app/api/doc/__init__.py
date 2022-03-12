from flask import Blueprint
from flask_restx import Api
from app.api.doc.tasks import namespace as tasks_ns
from app.api.doc.users import namespace as users_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='api doc',
    version='1.0',
    description='Documentation of api rest',
    doc='/doc'
)

api_extension.add_namespace(tasks_ns)
api_extension.add_namespace(users_ns)
