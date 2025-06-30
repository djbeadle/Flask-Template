"""
This is the entry point to your application. The environment variable FLASK_APP
is set to the name of this file (excluding the extension, .py)
"""

import os

from app import create_app

print('Firing things up')
print(os.getenv("FLASK_ENV"))
app = create_app(os.getenv('FLASK_ENV') or 'production')
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
