from flask import Flask
from .config import config
from flask_pymongo import PyMongo




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app = config[config_name]#.init_app(app)
    mongo = PyMongo(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app