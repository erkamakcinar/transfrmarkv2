from packet.backend.query import Query

class handler:
    def __init__(self, defTableTeams, defTablePlayers):
        self.defaultTeamsTable = defTableTeams
        self.defaultPlayersTable = defTablePlayers
         
    def tableBuilder(self, response):
        
        if('team_reset' in response):
            return self.defaultTeamsTable,True

        if('player_reset' in response):
            return self.defaultPlayersTable,False
        
        if('team_submit' in response):
            res = Query(response)
            return res.queryBuilder(True),True

        if('player_submit' in response):
            res = Query(response)
            return res.queryBuilder(False),False
