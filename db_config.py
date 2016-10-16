from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}/{database}'
db = SQLAlchemy(app)


class History(db.Model):
    __tablename__ = 'history'

    session_id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(80), unique=True)
    time = db.Column(db.TIME, unique=True)

    def __init__(self, page, time):
        self.page = page
        self.time = time

    def __repr__(self):
        return '<Session %r>' % self.session_id

class Links(db.Model):
    __tablename__ = 'links'

    url = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=True)
    about = db.Column(db.String(120), unique=True)

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return '<Session %r>' % self.session_id