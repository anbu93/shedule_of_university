# coding=utf-8
from Event import Event
from Group import Group
from Place import Place
from Teacher import Teacher
from flask import render_template

from Database import app
from models.EventTime import EventTime


class TableManager:
    def __init__(self):
        pass

    rows = []
    columns = []
    values = {}

    def generate(self, row_type, column_type):
        self.generateRowList(row_type)
        self.generateColumnList(column_type)
        self.generateTableValues()
        self.fillValuesTable(row_type, column_type)

    def generateRowList(self, row_type):
        if row_type is "group":
            self.rows = [group.toString() for group in Group.query.all()]
        elif row_type is "place":
            self.rows = [place.toString() for place in Place.query.all()]
        elif row_type is "teacher":
            self.rows = [teacher.toString() for teacher in Teacher.query.all()]
        else:
            self.rows = []

    def generateColumnList(self, column_type):
        if column_type is "datetime":
            self.columns = [datetime.toString() for datetime in EventTime.query.all()]
        else:
            self.columns = []

    def generateTableValues(self):
        self.values = {}
        for row in self.rows:
            self.values[row] = {}
            for column in self.columns:
                self.values[column][row] = "-"

    def fillValuesTable(self, row_type, column_type):
        events = Event.query.all()
        for event in events:
            if row_type is "teacher":
                row = event.teacher.toString()
            elif row_type is "group":
                row = event.group.toString()
            elif row_type is "place":
                row = event.place.toString()
            else:
                raise Exception("Неправильный тип строк")
            if column_type is "datetime":
                column = event.event_time.toString()
            else:
                raise Exception("Неправильный тип колонки")
            self.values[row][column] = event.toString()


manager = TableManager()


@app.route("/table/frame, <row_type>/<column_type>")
def tableViewPage(row_type, column_type):
    manager.generate(row_type, column_type)
    return render_template("tableFrame.html",
                           row_by=row_type,
                           column_list=manager.columns,
                           row_list=manager.columns,
                           table=manager.values)
