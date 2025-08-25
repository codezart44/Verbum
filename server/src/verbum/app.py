from flask import Flask

from verbum.api.domains import register_blueprints

def create_app():
    app = Flask(__name__)

    # register stuff here
    register_blueprints(app)

    return app
