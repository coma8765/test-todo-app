from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app, version="1.0", title="Todo API", description="A simple TODO API")

    from app.routes import api as tasks_api

    api.add_namespace(tasks_api)

    return app
