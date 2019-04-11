from flask import Blueprint

landing_bp = Blueprint('landing_bp', __name__)

from app.landing import routes