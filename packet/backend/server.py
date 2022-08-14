
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

    if request.method == "GET":
        return render_template("home.html", title='Best Football Site', table_elements=table_elements, teamFilter=teamFilter, playerFilter=playerFilter)
    
    if request.method == "POST":
        table_elements, control = handler(table_elements).tableBuilder(request.form)
        if control:
            print(teamFilter.meta)
            return render_template("home.html", title='Best Football Site', table_elements=table_elements, teamFilter=teamFilter, playerFilter=playerFilter)

        return render_template("home.html", title='Best Football Site', table_elements=table_elements, teamFilter=teamFilter, playerFilter=playerFilter)
    
    
    return render_template("home.html", title='Best Football Site', table_elements=table_elements, teamFilter=teamFilter, playerFilter=playerFilter)
