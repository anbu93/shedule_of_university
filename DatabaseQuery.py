import EventTime
from Event import Event
from Group import Group
from Place import Place
from Teacher import Teacher

from Database import db
from models.Subject import Subject


def getTeacherById(id_str):
    _id = int(id_str)
    return Teacher.query.filter_by(id=_id).first()


def getSubjectById(id_str):
    _id = int(id_str)
    return Subject.query.filter_by(id=_id).first()


def getGroupById(id_str):
    _id = int(id_str)
    return Group.query.filter_by(id=_id).first()


def getPlaceById(id_str):
    _id = int(id_str)
    return Place.query.filter_by(id=_id).first()


def getDateFromHtmlDate(date_str):
    dates = EventTime.Date.query.all()
    new_date = EventTime.Date(date_str)
    for d in dates:
        if d.equals(new_date):
            return new_date
    db.session.add(new_date)
    db.session.commit()
    return new_date


def getEventById(id_str):
    _id = int(id_str)
    return Event.query.filter_by(id=_id).first()


def getEventTime(date, time):
    event_time = EventTime.EventTime.query.filter_by(time=time).filter_by(date_id=date.id).first()
    if event_time is None:
        event_time = EventTime.EventTime(date, time)
    return event_time
