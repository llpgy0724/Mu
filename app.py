from flask import Flask
from flask_restful import Api, Resource
import configs
from models import init_db, db, User

app = Flask(__name__)
api = Api(app)

app.config.from_object(configs)
init_db(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/createdb')
def create():
    db.create_all()
    return '创建成功'


# @app.route('/query')
# # def query():
# #     return User.query.all()


@app.route('/add')
def add():
    user = User('llpgy522', 'wujiajie', 'yangrou', '2020-4-7 17:28:00')
    db.session.add(user)
    db.session.commit()
    return '创建成功'


class Hello(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run()
