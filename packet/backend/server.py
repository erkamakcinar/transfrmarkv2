from flask import render_template, request
from packet.backend import app
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
        print(teams)
        return render_template("home.html", title='Best Football Site', teams=teams, teamFilter=teamFilter, playerFilter=playerFilter)
    return render_template("home.html", title='Best Football Site', teams=teams, teamFilter=teamFilter, playerFilter=playerFilter)
