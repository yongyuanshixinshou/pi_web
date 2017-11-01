from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
redis = FlaskRedis()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    redis.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .camera import camera as camera_blueprint
    app.register_blueprint(camera_blueprint)

    from .car import car as car_blueprint
    app.register_blueprint(car_blueprint)

    return app
