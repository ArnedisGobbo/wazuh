from app.db import db, BaseModelMixin


class Task(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, _id, title, completed, user_id):
        self.id = _id
        self.title = title
        self.completed = completed
        self.user_id = user_id

    def __repr__(self):
        return f'Task({self.title})'

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def filter_by_title(cls, title, *args):
        return Task.query.filter(
            Task.title.contains(title),
            *args
        ).all()

    @classmethod
    def filter_by_title_and_completed(cls, title, completed, *args):
        return Task.query.filter(
            Task.title.contains(title),
            Task.completed == completed,
            *args
        ).all()
