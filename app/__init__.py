from flask import Flask, Blueprint
from config import config, DevelopmentConfig, ProductionConfig
import sqlite3

def create_app(config_name):
    """Application factory that returns a fully formed instance of the app

    The application context doesn't exist when this file is running, so 
    instead of being able to access values defined in the file config.py 
    the normal way as follows which uses the 'current_app' proxy:
    
    ~~~python
    from flask import current_app
    current_app.config['KEY_NAME']
    ~~~
    
    We have to manually access the config file as follows:

    ~~~python
    from config import config
    config[config_name].KEY_NAME
    ~~~
    
    Args:
      config_name (str): The name of the configuration to use
    
    """

    app = Flask(__name__, static_url_path="/static")
    print('this is the config name: {}'.format(config_name))
    
    # Select the desired config object from FLASK_ENV environment variable
    app.config.from_object(config[config_name])
    try:
      config[config_name].init_app(app)
    except:
      print('An error occurred initalizing the app. Be sure to set the environment \
        variables FLASK_ENV=(development|production) and FLASK_APP=application.py')

    from app.landing import landing_bp
    app.register_blueprint(landing_bp)

    return app
