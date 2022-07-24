from sqlalchemy import true
from server import db

class Team(db.model):
    id = db.Column(db.Integer, unique=True)
    team_name = db.Column(db.String(20), primary_key = true, nullable=False)
    home_town = db.Column(db.String(20), nullable=False)
    stadium_name = db.Column(db.String(20), nullable=False)
   