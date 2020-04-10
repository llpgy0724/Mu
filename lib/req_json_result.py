from flask import jsonify


def req_json_success(code=200, msg="成功~~", data=None):
    if data is None:
        data = {}
    req = jsonify(code=code, msg=msg, data=data)
    return req


def req_json_error(code=-1, msg="失败", data=None):
    if data is None:
        data = {}
    req = jsonify(code=code, msg=msg, data=data)
    return req
