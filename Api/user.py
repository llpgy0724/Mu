from flask import Blueprint, request, make_response, jsonify

from models import User
from req_json_result import req_json_error,req_json_success

api_page = Blueprint('api_page', __name__)


@api_page.route("/login", methods=['GET'])
def login():
    req = request.values
    username = req['username']
    password = req['password']
    result = User.query.filter(User.username == username and User.password == password).all()
    print(type(result))
    print(type(result[0]))
    return result[0].token


@api_page.route("/register", methods=['POST'])
def register():
    req = request.values
    if req['username'] is None or req['username'] < 8:
        return req_json_error("用户名错误！")
    if req['password'] is None or req['password'] < 8:
        return req_json_error("密码错误")

    return req_json_success("注册成功")
