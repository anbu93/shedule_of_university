# coding=utf-8
from Database import db
from Subject import Subject


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

    event_time_id = db.Column(db.Integer, db.ForeignKey('event_time.id'))
    event_time = db.relationship('EventTime', backref=db.backref('events', lazy='dynamic'))

    def __init__(self, teacher, subject, group, place, event_time):
        self.subject = subject
        self.teacher = teacher
        self.group = group
        self.place = place
        self.event_time = event_time

    def __repr__(self):
        return '<Event %r>' % self.name

    def toString(self):
        return self.subject.name + "\n" + self.teacher.shortName() + "\n" \
            + self.group.name + "\n" + self.place.name
