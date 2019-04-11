from flask import Flask, Blueprint
from config import config

def create_app(config_name):
    """Application factory that returns a fully formed instance of the app

    Args:
      config_name (str): The name of the configuration to use
    
    """

    app = Flask(__name__, static_url_path="/static")
    print('this is the config name: {}'.format(config_name))
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.landing import landing_bp
    app.register_blueprint(landing_bp)

    return app
