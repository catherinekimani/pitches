from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app(config_name):
    
# initializing application
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
# Registering blueprint 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

# initialize flask extension
    db.init_app(app)

# creating app configurations
    app.config.from_object(config_options[config_name])
    
    return app
    
