from http.client import HTTPResponse
from venv import create
from flask import render_template, Response
from app.landing import landing_bp
from db_operations import create_thing, list_all_things


@landing_bp.route('/', methods=['GET'])
def home():
    text = 'This is the landing route!'
    return render_template(
        'landing.html',
        things=list_all_things(),
        content=text
    )


@landing_bp.route('/info', methods=['GET'])
def info():
    text = 'This is the info route! Here is a kitten:'
    return render_template('info.html', content=text)


@landing_bp.route('/info', methods=['PUT'])
def update_info():
    return 'You have made a put request!'


@landing_bp.route('/create_thing', methods=['GET'])
def create_thing_route():
    create_thing("Thing!", "This is another thing", 2)
    return Response("New thing inserted in to the database.", 200)
