from Database import db


class EventTime (db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.Date)
    time = db.Column(db.Integer)

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def toString(self):
        return str(self.time) + " : " + str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)

    def __repr__(self):
        return "<DateTime %r>" % self.toString()

    def __str__(self):
        return self.toString()
