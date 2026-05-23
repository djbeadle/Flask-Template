"""
This is the entry point to your application. The environment variable FLASK_APP
is set to the name of this file (excluding the extension, .py)
"""

import os

from app import create_app

print('Firing things up')

app = create_app("development" if os.getenv('FLASK_DEBUG') else "production")

app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
