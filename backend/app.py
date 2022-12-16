from flask import Flask
from flask_bootstrap import Bootstrap
from api.files import files_api
from api.time import time_api
from dotenv import dotenv_values
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

config = dotenv_values(".flaskenv")
db = SQLAlchemy()
migrate = Migrate()

def create_app(environment=None):
    if not environment:
        environment = config.get("ENVIRONMENT","Development")
    
    app = Flask(__name__)
    app.config.from_object(f'config.{environment}')
    
    app.register_blueprint(files_api)
    app.register_blueprint(time_api)
    
    Bootstrap(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
