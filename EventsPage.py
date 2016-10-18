# coding=utf-8
import Event
from Database import app, db
from flask import render_template, request
from Event import Event

from Teacher import Teacher
from Place import Place
from Group import Group
from Subject import Subject
from DatabaseQuery import getGroupById, getPlaceById, getSubjectById, getTeacherById, getDateFromHtmlDate, getEventById


@app.route("/events", methods=["GET"])
def showEventsPageGet():
    events = Event.query.order_by(Event.date).order_by(Event.number_of_lesson).all()
    return render_template("eventsShow.html", events=events, result=None)


@app.route("/events/add", methods=["GET"])
def addEventsPageGet(result=None):
    events = Event.query.order_by(Event.date).order_by(Event.number_of_lesson).all()
    teachers = Teacher.query.all()
    groups = Group.query.all()
    places = Place.query.all()
    subjects = Subject.query.all()
    return render_template("eventsCreate.html", events=events,
                           teachers=teachers,
                           groups=groups,
                           places=places,
                           subjects=subjects, result=result)


@app.route("/events/add", methods=["POST"])
def addEventsPagePost():
    teacher = getTeacherById(request.form["teacher"])
    subject = getSubjectById(request.form["subject"])
    group = getGroupById(request.form["group"])
    place = getPlaceById(request.form["place"])
    date = getDateFromHtmlDate(request.form["date"])
    number = int(request.form["number"])
    if teacher is not None \
            and subject is not None \
            and group is not None \
            and place is not None \
            and date is not None \
            and number is not None:
        event = Event(teacher, subject, group, place, date, number)
        db.session.add(event)
        db.session.commit()
        result = "Ok"
    else:
        result = "Need a fill all fields"
    return addEventsPageGet(result)


@app.route("/events/remove", methods=["GET"])
def removeEventsPageGet():
    events = Event.query.order_by(Event.date).order_by(Event.number_of_lesson).all()
    return render_template("eventsRemove.html", events=events, result=None)


@app.route("/events/remove", methods=["POST"])
def removeEventsPagePost():
    event = getEventById(request.form["id"])
    if event is not None:
        db.session.delete(event)
        db.session.commit()
        result = "Ok"
    else:
        result = "Not found"
    events = Event.query.order_by(Event.date).order_by(Event.number_of_lesson).all()
    return render_template("eventsRemove.html", events=events, result=result)

