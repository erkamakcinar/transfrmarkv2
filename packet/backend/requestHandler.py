from packet.backend.query import Query

class handler:
    def __init__(self, default_elements):
        self.de = default_elements
         
    def tableBuilder(self, response):
        
        if('team_reset' in response or 'player_reset' in response):
            return self.de, True 
        
        if('team_submit' in response):
            team_name = response['team_name']
            res = Query(team_name)
            return res.queryBuilder(),False


        if('player_submit' in response):
            result = response
            response = None
            return result,False
