from flask import Flask
import configs
from Api.user import api_page
from models import init_db

app = Flask(__name__)
app.register_blueprint(api_page, url_prefix="/api")

app.config.from_object(configs)
init_db(app)


if __name__ == '__main__':
    app.run()
