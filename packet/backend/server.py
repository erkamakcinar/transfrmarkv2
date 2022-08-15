
from flask import render_template, request
from packet.backend import app
from packet.ui.filter import TeamFiler, PlayerFiler
from packet.backend.requestHandler import handler
from packet.backend import def_table


@app.route("/", methods=["POST", "GET"])
def home():
    table_elements = def_table
    teamFilter = TeamFiler()
    playerFilter = PlayerFiler()
 
    if request.method == "POST":
        table_elements = handler(table_elements).tableBuilder(request.form)
    
    return render_template("home.html", title='Best Football Site', table_elements=table_elements, teamFilter=teamFilter, playerFilter=playerFilter)
