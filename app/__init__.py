from flask import Flask
from config import config_options

def create_app(config_name):
    
# initializing application
    app = Flask(__name__)
    
# creating app configurations
    app.config.from_object(config_options[config_name])
    
    return app
    
