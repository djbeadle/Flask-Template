from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "This is Flask running on Azure App Service for Linux"