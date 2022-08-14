from packet.backend.query import Query

class handler:
    def __init__(self, default_elements):
        self.de = default_elements
         
    def tableBuilder(self, response):
        
        if('team_reset' in response or 'player_reset' in response):
            return self.de
        
        if('team_submit' in response):
            res = Query(response)
            return res.queryBuilder(True),False


        if('player_submit' in response):
            result = response
            response = None
            return result
