# coding=utf-8
from Database import db, app
from flask import render_template, request
from Subject import Subject


@app.route("/subjects", methods=["GET", "POST"])
def showSubjectsPage():
    subjects = Subject.query.all()
    return render_template("subjects.html", subjects=subjects, type="show", result=None)


# Методы создания предметов

@app.route("/subjects/add", methods=["GET"])
def addSubjectsPage():
    subjects = Subject.query.all()
    return render_template("subjects.html", subjects=subjects, type="add", result=None)


@app.route("/subjects/add", methods=["POST"])
def addSubjectsPagePost():
    name = request.form["name"]
    subject = Subject(name)
    db.session.add(subject)
    db.session.commit()
    result = "Ok"
    subjects = Subject.query.all()
    return render_template("subjects.html", subjects=subjects, type="add", result=result)


# Методы удаления предметов

@app.route("/subjects/remove", methods=["GET"])
def removeSubjectsPage():
    subjects = Subject.query.all()
    return render_template("subjects.html", subjects=subjects, type="remove", result=None)


@app.route("/subjects/remove", methods=["POST"])
def removeSubjectsPagePost():
    id = int(request.form["id"])
    subject = Subject.query.filter_by(id=id).first()
    if subject is None:
        result = "Error: не найден предмет с таким id"
    else:
        db.session.delete(subject)
        db.session.commit()
        result = "Ok"
    subjects = Subject.query.all()
    return render_template("subjects.html", subjects=subjects, type="remove", result=result)
