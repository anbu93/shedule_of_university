import datetime

from Database import app, db
from flask import render_template, request
from Event import Event
from Teacher import Teacher
from Place import Place
from Group import Group
from Subject import Subject


def toStringDate(date):
    return str(date.day) + "/" + str(date.month) + "/" + str(date.year)


@app.route("/table", methods=["GET"])
def tableViewPageGet():
    return render_template("tableView.html", row="group", column="datetime")


@app.route("/table", methods=["POST"])
def tableViewPagePost():
    row = request.form["row"]
    column = request.form["column"]
    return render_template("tableView.html", row=row, column=column)


def getDateTimeString(event):
    return str(event.number_of_lesson) + ":" + toStringDate(event.date)


def getDataTimeColumnsList():
    dates = set()
    events = Event.query.order_by(Event.date).order_by(Event.number_of_lesson).all()
    for event in events:
        dates.add(toStringDate(event.date))
    date_time_column = [str(num)+":"+date for date in dates for num in range(1, 6)]
    #for date in dates:
    #    for num in range(1, 6):
    #       date_time_column.append(str(num) + ":" + date)
    return date_time_column


def createEmptyTableFor(row_list, column_list):
    table = {}
    for row in row_list:
        table[row] = {}
        for column in column_list:
            table[row][column] = "-"
    return table


def getGroupsTable(row_list, column_list):
    table = createEmptyTableFor(row_list, column_list)
    events = Event.query.all()
    for event in events:
        table[event.group.name][getDateTimeString(event)] = event.toString()
    return table


def getTeacherTable(row_list, column_list):
    table = createEmptyTableFor(row_list, column_list)
    events = Event.query.all()
    for event in events:
        table[event.teacher.shortName()][getDateTimeString(event)] = event.toString()
    return table


def getPlaceTable(row_list, column_list):
    table = createEmptyTableFor(row_list, column_list)
    events = Event.query.all()
    for event in events:
        table[event.place.name][getDateTimeString(event)] = event.toString()
    return table


@app.route("/table/frame/<row>/<column>", methods=["GET"])
def tableFramePageGet(row, column):
    date_time_column = getDataTimeColumnsList()
    row_name = row
    if row == "group":
        row_list = [group.name for group in Group.query.order_by(Group.name).all()]
        table = getGroupsTable(row_list, date_time_column)
    if row == "teacher":
        row_list = [teacher.shortName() for teacher in Teacher.query.order_by(Teacher.name).all()]
        table = getTeacherTable(row_list, date_time_column)
    if row == "place":
        row_list = [place.name for place in Place.query.order_by(Place.name).all()]
        table = getPlaceTable(row_list, date_time_column)
    return render_template("tableFrame.html", row_by=row_name, column_list=date_time_column, row_list=row_list, table=table)

