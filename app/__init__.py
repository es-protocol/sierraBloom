from flask import Flask, redirect, url_for, render_template, send_file
from dotenv import load_dotenv
from app.extensions.database import db, migrate
from app.project.models import Author, Initiative
import os
from . import sierra_b

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    register_extensions(app)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(sierra_b.routes.bleuprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)