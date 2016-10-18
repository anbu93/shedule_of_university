from Database import db


class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def __init__(self, date_str):
        tokens = date_str.split("/")
        self.day = tokens[0]
        self.month = tokens[1]
        self.year = tokens[2]

    # def __init__(self, day, month, year):
    #     self.day = day
    #     self.month = month
    #     self.year = year

    def toString(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)


class EventTime (db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_id = db.Column(db.Integer, db.ForeignKey('date.id'))
    date = db.relationship('Date', backref=db.backref('event_times', lazy='dynamic'))

    time = db.Column(db.Integer)

    def __init__(self, date, time):
        self.date = date
        self.time = time

    def toString(self):
        return str(self.time) + " : " + self.date.toString()

    def __repr__(self):
        return "<DateTime %r>" % self.toString()

    def __str__(self):
        return self.toString()

