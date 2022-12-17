from flask import Flask
from flask_bootstrap import Bootstrap
from api.files import files_api
from api.time import time_api
from dotenv import dotenv_values
from config import db, migrate

config = dotenv_values(".flaskenv")


def create_app(environment=None):
    if not environment:
        environment = config.get("ENVIRONMENT","Development")
    
    app = Flask(__name__)
    app.config.from_object(f'config.{environment}')
    
    app.register_blueprint(files_api)
    app.register_blueprint(time_api)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    Bootstrap(app)
    
    
    return app
