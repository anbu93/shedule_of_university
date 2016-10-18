from Group import Group
from Place import Place
from Subject import Subject
from Teacher import Teacher
from Event import Event
from datetime import date


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
    dates = date_str.split('/')
    return date(int(dates[2]), int(dates[1]), int(dates[0]))


def getEventById(id_str):
    _id = int(id_str)
    return Event.query.filter_by(id=_id).first()