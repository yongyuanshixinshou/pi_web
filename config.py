import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    BOOTSTRAP_SERVE_LOCAL = True
    REDIS_URL = "redis://:00000000@localhost:6379/0"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    #DEBUG = True
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
