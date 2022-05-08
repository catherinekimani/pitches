from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    
# initializing application
    app = Flask(__name__)
    # register auth blueprint
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'DATABASE_URL'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
# Registering blueprint 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

# initialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

# creating app configurations
    app.config.from_object(config_options[config_name])
    
    return app
    
