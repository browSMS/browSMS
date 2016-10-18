from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'http://browsms.ctwglzvlbtip.us-west-2.rds.amazonaws.com/'
app.config['SQLCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models for db tables

class history(db.Model):
    phone_number = db.Column(db.varchar(15), primary_key = True)
    link = db.Column(db.varchar(200), unique = True)
    time = db.Column(db.datetime, unique = True )

    def __init__(self, link, time):
        self.link = link
        self.time = time

    def __link__(self):
        return '<Link % r>' % self.link

class links(db.Model):
    url = db.Column(db.varchar(200), primary_key = True)
    description = db.Column(db.varchar(50), unique = True)
    link = db.Column(db.varchar(200), unique = True)

    def __init__(self, description, link):
        self.description = descripion
        self.link = link

    def __description__(self):
        return '<Description %r>' % self.description
