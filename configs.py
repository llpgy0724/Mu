HOST = '47.111.144.58'
PORT = '3306'
DATABASE = 'mu'
USERNAME = 'root'
PASSWORD = '342622Wjj!@#'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}"\
    .format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
