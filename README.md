# Setting up the development environment
Prerequisites Python3 and Pip [(install guide)](https://docs.python-guide.org/dev/virtualenvs/#make-sure-you-ve-got-python-pip), virtualenv [(install guide)](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv), and git [(another install guide)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

1. Clone the repository

2. Navigate to the repository's top level (the level with 'README.md', 'requirements.txt', the folder 'app', etc)

3. Create a virtual environment with python 3 and enter it [(guide here)](https://docs.python-guide.org/dev/virtualenvs/#basic-usage)

4. Install the required python packages from requirements.txt [(guide here)](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

5. Create a copy of 'config-example.py' in the same directory called 'config.py' and fill it in with your secrets. 'config.py' already has an entry in '.gitignore'

6. Set the Flask environment variables

Unix:

~~~bash
export FLASK_ENV=development
export FLASK_APP=myapp
~~~

Windows CMD:

~~~bash
set FLASK_ENV=development
set FLASK_APP=myapp
~~~

Windows PowerShell:

~~~bash
$env:FLASK_ENV='development'
$env:FLASK_APP='myapp.py'
~~~

7. Run it!

~~~bash
flask run
~~~

# Tips & Tricks & Notes

## How do I run code on application startup?

Put it in **/app/__init__.py**

## How do I run this under Apache?

1. Install Apache

2. Install the appropriate version of [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/) for your distribution and version of Python.

3. Download this project and set it up based on the instructions in the previous section, [Setting up the development environment](Setting-up-the-development-environment)

4. Add an Apache virtual host with the following details

  ~~~bash
  WSGIDaemonProcess fugue python-home=[PATH_TO_VIRTUALENV] home=[PATH_TO_PROJECT_HOME]
  WSGIApplicationGroup %{GLOBAL}
  WSGIScriptAlias /[PATH] [PATH_TO_CONF_WSGI]
  <Directory [PATH_TO_PROJECT_HOME]>
      WSGIProcessGroup [PROCESS_GROUP_NAME]
      Options FollowSymLinks
      AllowOverride None
      Require all granted
  </Directory>
  ~~~
  
  Example variable values are as follows:
  
  - PATH_TO_VIRTUALENV: **"/home/djbeadle/flask-template/venv/"**
  - PATH_TO_PROJECT_HOME: **"/home/djbeadle/flask-template"**
  - PATH: **"flask_template"**
  - PATH_TO_CONF_WSGI: **"/home/djbeadle/Daniel-fugue-take-home/conf.wsgi"**
  - PROCESS_GROUP_NAME: **"flask_template"**

5. Restart Apache and see if it works!

5. Tweak your project's home directory permissions if Apache can't access it. 

# Build and Test

Tests can be run from the root directory with the command

~~~bash
pytest
~~~
