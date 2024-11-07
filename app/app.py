from flask import Flask, redirect, url_for, render_template, send_file
from . import sierra_b

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(sierra_b.routes.bleuprint)