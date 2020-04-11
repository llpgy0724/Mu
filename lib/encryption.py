import base64
import hashlib
import random
import string


def generateSalt(length=16):
    salt = [random.choice((string.ascii_lowercase + string.ascii_uppercase + string.digits)) for i in range(length)]
    return "".join(salt)


def generatePassword(pwd, salt):
    m = hashlib.md5()
    var_str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
    m.update(var_str.encode("utf-8"))
    return m.hexdigest()


def generateToken():
    return generateSalt(32)
