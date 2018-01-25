import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'pkyx'

    # @staticmethod
    # def init_app(app):
    #     from flask_pymongo import PyMongo
    #     app = PyMongo(app)
    #     return app

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'default': DevelopmentConfig,
    'dev': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}