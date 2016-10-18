from Database import db


class Place (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Place %r>" % self.name

    def toString(self):
        return self.name
