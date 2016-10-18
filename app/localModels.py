from flask_sqlalchemy import SQLAlchemy
from app import app
import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models for db tables

class history(db.Model):
    phone_number = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.String)
    time = db.Column(db.Integer)

    def __init__(self, link, time):
        self.link = link
        self.time = time

    def __link__(self):
        return '<Link % r>' % self.link

class links(db.Model):
    url = db.Column(db.String, primary_key = True)
    description = db.Column(db.String)
    link = db.Column(db.String)

    def __init__(self, description, link):
        self.description = descripion
        self.link = link

    def __description__(self):
        return '<Description %r>' % self.description
