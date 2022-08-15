
from flask import render_template, request
from packet.backend import app
from packet.ui.filter import TeamFiler, PlayerFiler
from packet.backend.requestHandler import handler
from packet.backend import def_table_players, def_table_teams


@app.route("/", methods=["POST", "GET"])
def home():

    table_elements = def_table_teams
    teamFilter = TeamFiler()
    playerFilter = PlayerFiler()
 
    if request.method == "POST":
        table_elements = handler(def_table_teams, def_table_players).tableBuilder(request.form)
    
    return render_template("home.html", title='Best Football Site', table_elements=table_elements, teamFilter=teamFilter, playerFilter=playerFilter)
