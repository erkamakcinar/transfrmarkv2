from flask import render_template, request
from packet.backend import app
from packet.backend.manipulation import Reader
from packet.ui.filter import TeamFiler, PlayerFiler
from packet.backend.requestHandler import handler


@app.route("/", methods=["POST", "GET"])
def home():
    teams = ()
    teamFilter = TeamFiler()
    playerFilter = PlayerFiler()
    if request.method == "POST":
        print(request.form)
        obj = handler()
        teams = obj.tableBuilder(request.form)
    return render_template("home.html", title='Best Football Site', teams=teams, teamFilter=teamFilter, playerFilter=playerFilter)
