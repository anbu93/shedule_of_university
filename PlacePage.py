from Database import app, db
from flask import request, render_template
from Place import Place


@app.route("/place", methods=["POST", "GET"])
def placePage():
    places = Place.query.all()
    return render_template("place.html", type="show", places=places, result=None)


@app.route("/place/add", methods=["GET"])
def addPlacePage():
    places = Place.query.all()
    return render_template("place.html", type="add", places=places, result=None)


@app.route("/place/add", methods=["POST"])
def addPlacePagePost():
    place = Place(request.form["name"])
    db.session.add(place)
    db.session.commit()
    places = Place.query.all()
    return render_template("place.html", type="add", places=places, result="Ok")


@app.route("/place/remove", methods=["GET"])
def removePlacePage():
    places = Place.query.all()
    return render_template("place.html", type="remove", places=places, result=None)


@app.route("/place/remove", methods=["POST"])
def removePlacePagePost():
    id = int(request.form["id"])
    place = Place.query.filter_by(id=id).first()
    if not (place is None):
        db.session.delete(place)
        db.session.commit()
        result = "Ok"
    else:
        result = "Error"
    places = Place.query.all()
    return render_template("place.html", type="remove", places=places, result=result)
