# coding=utf-8
from Database import app, db
from flask import render_template, request
from Teacher import Teacher


def getTeachers():
    """Взять список преподователей"""
    return Teacher.query.order_by(Teacher.surname).all()


@app.route("/teachers/add", methods=["GET"])
def addTeachersPageGet():
    return render_template("teachers.html", teachers=getTeachers(), result=None, isAddTeacherPage=True)


@app.route("/teachers/add", methods=["POST"])
def addTeachersPagePost():
    name = request.form["name"]
    surname = request.form["surname"]
    lastname = request.form["lastname"]
    teacher = Teacher(surname, name, lastname)
    db.session.add(teacher)
    db.session.commit()
    result = "Successful added"
    return render_template("teachers.html", teachers=getTeachers(), result=result, isAddTeacherPage=True)


@app.route("/teachers/remove", methods=["GET"])
def removeTeachersPageGet():
    return render_template("teachers.html", teachers=getTeachers(), result=None, isAddTeacherPage=False)


@app.route("/teachers/remove", methods=["POST"])
def removeTeachersPagePost():
    id = int(request.form["id"])
    teacher = Teacher.query.filter_by(id=id).first()
    db.session.delete(teacher)
    db.session.commit()
    result = "Successful deleted"
    return render_template("teachers.html", teachers=getTeachers(), result=result, isAddTeacherPage=False)

