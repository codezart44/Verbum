from flask import Flask
from .entries.routes import blueprint as blueprint_entries

def register_blueprints(app: Flask):
    app.register_blueprint(blueprint_entries)

