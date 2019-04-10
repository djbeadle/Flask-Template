from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
  return "This is Flask running on Azure App Service for Linux"