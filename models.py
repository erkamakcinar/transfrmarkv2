from server import db

class Team(db.model):
    id = db.Column(db.Integer, unique=True)
    team_name = db.Column(db.String(20), primary_key = True, nullable=False)
    home_town = db.Column(db.String(20), nullable=False)
    stadium_name = db.Column(db.String(20), nullable=False)
    players = db.relationship('Player', backref='Player')

    def __repr__(self) -> str:
        return f"Team('{self.team_name}', '{self.home_town}', '{self.stadium_name}')"

class Player(db.model):
    id = db.Column(db.Integer, unique=True)
    value = db.Column(db.Float)
    position = db.Column(db.String(20), primary_key = True, nullable=False)
    team = db.Column(db.String(20), db.ForeignKey('team.team_name'), nullable=False)
    
    def __repr__(self) -> str:
        return f"Player('{self.value}', '{self.position}')"


   