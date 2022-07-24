from flask import Flask,render_template, request, flash
from filter import TeamFiler, PlayerFiler
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

teams = ["fb", "gs", "bjk", "ts"]
x=8
@app.route("/", methods=["POST", "GET"])
def home():
    teamFilter = TeamFiler()
    playerFilter = PlayerFiler()
    if request.method == "POST":
        pass
    if teamFilter.validate_on_submit():
        flash(f'Filtreleme Yapıldı', 'success')
    
   
    return render_template('home.html', title='Best Football Site', teams=teams, teamFilter=teamFilter, playerFilter=playerFilter)

if __name__ == '__main__':
    app.run(debug=True)