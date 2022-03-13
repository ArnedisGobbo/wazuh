from marshmallow import fields, post_dump

from app.ext import ma


class TaskSchema(ma.Schema):
    class Meta:
        ordered = True

    id = fields.Integer()
    title = fields.String()
    user_id = fields.Integer()
    completed = fields.Boolean()

    @post_dump(pass_many=True)
    def build_response(self, data, many):
        resp = {}
        if many is True:
            resp["total_items"] = len(data)

        resp["data"] = data

        return resp
