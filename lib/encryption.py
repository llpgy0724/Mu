import random
import string

def generateSalt(length=16):
    salt = [random.choice((string.ascii_lowercase + string.ascii_uppercase + string.digits)) for i in range(length)]
    return "".join(salt)


def generatePassword(pwd, salt):
    m = hasslib
    pass
