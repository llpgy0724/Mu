from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    name = db.Column(db.String(32), unique=True)
    token = db.Column(db.String(32), unique=True)
    register_time = db.Column(db.String(50), unique=True)
    salt = db.Column(db.String(32), unique=True)
    status = db.Column(db.Integer, unique=True)

    def __init__(self, username, password, name, token, register_time, salt, status):
        self.username = username
        self.password = password
        self.name = name
        self.token = token
        self.register_time = register_time
        self.salt = salt
        self.status = status

    def __repr__(self):
        return '<User %r>' % self.token
