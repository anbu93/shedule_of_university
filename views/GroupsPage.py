from flask import render_template, request

from Database import db, app
from models.Group import Group


@app.route("/groups", methods=["GET", "POST"])
def showGroupsPage():
    groups = Group.query.all()
    return render_template("groups.html", type="show", groups=groups)


@app.route("/groups/add", methods=["GET"])
def addGroupsPage():
    groups = Group.query.all()
    return render_template("groups.html", type="add", groups=groups)


@app.route("/groups/add", methods=["POST"])
def addGroupsPagePost():
    group = Group(request.form["name"])
    db.session.add(group)
    db.session.commit()
    groups = Group.query.all()
    return render_template("groups.html", type="add", groups=groups)


@app.route("/groups/remove", methods=["GET"])
def removeGroupsPage():
    groups = Group.query.all()
    return render_template("groups.html", type="remove", groups=groups)


@app.route("/groups/remove", methods=["POST"])
def removeGroupsPagePost():
    id = int(request.form["id"])
    group = Group.query.filter_by(id=id).first()
    db.session.delete(group)
    db.session.commit()
    groups = Group.query.all()
    return render_template("groups.html", type="remove", groups=groups)
