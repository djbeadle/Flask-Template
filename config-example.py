"""
This is an example of the config file!
You MUST make a copy of it named "config.py" in the same location and fill it 
with the actual values. Since "config.py" holds all of your secrets it should 
NEVER be committed to git.
"""

import os

class Config:
    APP_NAME = 'Facebook II'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    
    # All sorts of configuration variables can be set here

    @staticmethod
    def init_app(app):
        """
        This method can be used to set up configuration-related things.
        """
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    
    DB_NAME = "myapp_dev.db"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        print('This is initalization for the development config.')

class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "myapp_test.db"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        print('This is initalization for the testing config.')
        
class ProductionConfig(Config):
    DEBUG = False

    DB_NAME = "myapp_prod.db"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        print('This is initalization for the production config.')

# This dictionary maps different environment names to the actual config classes.
config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
