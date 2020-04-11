import time

from flask import request, session

from Api import api_page
from lib.encryption import generateSalt, generateToken, generatePassword
from models import User, db
from lib.req_json_result import req_json_error, req_json_success
from lib.captcha import createImg


@api_page.route("/login", methods=['GET'])
def login():
    req = request.values
    username = req['username']
    password = req['password']
    result = User.query.filter(User.username == username and User.password == password).first()
    if not result:
        return req_json_error(msg="请检查账号密码是否正确！")
    data = {"token": result.token}
    return req_json_success(data=data)


@api_page.route("/register", methods=['GET', 'POST'])
def register():
    req = request.values
    if req['username'] is None or len(req['username']) < 8:
        return req_json_error(msg="用户名格式错误！")
    if req['password'] is None or len(req['password']) < 8:
        return req_json_error(msg="密码格式错误")
    if User.query.filter_by(username=req['username']).all():
        return req_json_error(msg="账号已被注册")
    salt = generateSalt()
    token = generateToken()
    password = generatePassword(req['password'], salt)
    new_user = User(req['username'], password, req['username'], token,
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), salt, 1)
    db.session.add(new_user)
    db.session.commit()
    return req_json_success(msg="注册成功")


@api_page.route("/captcha", methods=['GET', 'POST'])
def getCaptcha():
    img, code = createImg()
    img = "data:image/png;base64," + img
    session['code'] = code
    return "<img src=%s>" % img


@api_page.route("/getCode")
def getCode():
    code = session['code']
    return code
