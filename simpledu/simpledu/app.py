from flask import Flask
from flask_migrate import Migrate
from simpledu.config import configs
from simpledu.models import db

def register_blueprints(app):
    from .handlers import front,course,admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

def create_app(config):

    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    db.init_app(app)
    Migrate(app,db)
    register_blueprints(app)
    return app

