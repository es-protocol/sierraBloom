from app.extensions.database import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), unique=True)
    description = db.Column(db.String(200))
    owner = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    picture_url = db.column(db.String(200))

    def __init__(self, title, description, picture_url, owner=None, tag=None):
        self.title = title
        self.description = description
        self.owner = owner
        self.tag = tag
        self.picture_url = picture_url
