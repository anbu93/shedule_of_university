# coding=utf-8
from Database import db
from EventTime import EventTime


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    subject = db.relationship('Subject', backref=db.backref('events', lazy='dynamic'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship('Teacher', backref=db.backref('events', lazy='dynamic'))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship('Group', backref=db.backref('events', lazy='dynamic'))
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    place = db.relationship('Place', backref=db.backref('events', lazy='dynamic'))

    eventtime_id = db.Column(db.Integer, db.ForeignKey('EventTime.id'))
    eventtime = db.relationship('DateTime', backref=db.backref('events', lazy='dynamic'))

    date = db.Column(db.Date)
    number_of_lesson = db.Column(db.Integer)

    def __init__(self, teacher, subject, group, place, date, number_of_lesson):
        self.subject = subject
        self.teacher = teacher
        self.group = group
        self.place = place
        # self.eventtime = eventtime
        self.date = date
        self.number_of_lesson = number_of_lesson

    def __repr__(self):
        return '<Event %r>' % self.name

    def toString(self):
        return self.subject.name + "\n" + self.teacher.shortName() + "\n" \
            + self.group.name + "\n" + self.place.name

