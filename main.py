# coding=utf-8
from Database import app, db
from flask import render_template
import TeachersPage
import EventsPage
import GroupsPage
import PlacePage
import SubjectsPage
import EventTime
# import TableView
import TableManager


@app.route("/", methods=["GET"])
def main():
    links = {
        "link_to_table_view": "/table",

        "link_to_events_show": "/events",
        "link_to_events_remove": "/events/remove",
        "link_to_events_add": "/events/add",

        "link_to_teachers_add": "/teachers/add",
        "link_to_teachers_remove": "/teachers/remove",

        "link_to_groups_show": "/groups",
        "link_to_groups_add": "/groups/add",
        "link_to_groups_remove": "/groups/remove",

        "link_to_place_show": "/place",
        "link_to_place_add": "/place/add",
        "link_to_place_remove": "/place/remove",

        "link_to_subjects_show": "/subjects",
        "link_to_subjects_add": "/subjects/add",
        "link_to_subjects_remove": "/subjects/remove"
    }
    return render_template("index.html", **links)


if __name__ == "__main__":
    db.create_all()
    app.run()
