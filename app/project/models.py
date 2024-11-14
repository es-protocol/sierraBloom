from app.extensions.database import db
from datetime import datetime

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    street = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    zip = db.Column(db.String(10))
    country = db.Column(db.String(80))
    initiative = db.relationship('Initiative', backref='author', uselist=False, lazy=True)

class Initiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    description = db.Column(db.String(200))
    owner = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    picture_url = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    