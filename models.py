from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255), unique=True)
    register_time = db.Column(db.String(255))

    def __init__(self, username, password, name, register_time):
        self.username = username
        self.password = password
        self.name = name
        self.register_time = register_time

    def __repr__(self):
        return '<User %r>' % self.username
