from packet import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(20), unique=True, nullable=False)
    home_town = db.Column(db.String(20))
    stadium_name = db.Column(db.String(20))
    players = db.relationship('Player', backref='PlaysFor', lazy=True)

    def __repr__(self) -> str:
        return f"Team('{self.team_name}', '{self.home_town}', '{self.stadium_name}')"

class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Float)
    position = db.Column(db.String(20), nullable=False)
    team_played = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    
    def __repr__(self) -> str:
        return f"Player('{self.value}', '{self.position}')"


   