# coding=utf-8
from Database import db, app
from models import *


@app.route("/")
def index():
    events = Event.query.all()
    result = "Events: <br>"
    for event in events:
        result = result + event.toString() + "<br>"
        result = result + event.event_time.toString() + "<br>"
    return result


if __name__ == "__main__":
    db.create_all()
    app.run()
