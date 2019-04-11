from flask import render_template
from app.landing import landing_bp

@landing_bp.route('/', methods=['GET'])
def home():
    text = 'This is the landing route!'
    return render_template('landing.html', content=text)

@landing_bp.route('/info', methods=['GET'])
def info():
    text = 'This is the info route! Here is a kitten:'
    return render_template('info.html', content=text)

@landing_bp.route('/info', methods=['PUT'])
def update_info():
    return 'You have made a put request!'