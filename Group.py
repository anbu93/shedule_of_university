from Database import db


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Group %r>" % self.name

    def toString(self):
        return self.name
