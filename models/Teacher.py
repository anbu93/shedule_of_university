# coding=utf-8
from Database import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(100), unique=False)
    name = db.Column(db.String(100), unique=False)
    lastname = db.Column(db.String(100), unique=False)

    def __init__(self, surname, name, lastname):
        self.name = name
        self.surname = surname
        self.lastname = lastname

    def fullName(self):
        return self.surname + " " + self.name + " " + self.lastname

    def shortName(self):
        return self.surname + " " + self.name[0] + "." + self.lastname[0] + "."

    def __repr__(self):
        return "<Teacher %r>" % self.shortName()

    def toString(self):
        return self.shortName()
