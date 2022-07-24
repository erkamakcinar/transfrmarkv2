from flask import render_template, request
from packet import app
from packet.filter import TeamFiler, PlayerFiler


teams = ["fb", "gs", "bjk", "ts"]
x=8
@app.route("/", methods=["POST", "GET"])
def home():
    teamFilter = TeamFiler()
    playerFilter = PlayerFiler()
    if request.method == "POST":
        pass
    return render_template('home.html', title='Best Football Site', teams=teams, teamFilter=teamFilter, playerFilter=playerFilter)
