from packet.backend.query import Query

class handler:
    def __init__(self):
        pass
         
    def tableBuilder(self, response):
        print(response)
        if('team_submit' in response):
            team_name = response['team_name']
            res = Query(team_name)
            return res.queryBuilder()


        if('player_submit' in response):

            #self.cursor.execute( "SELECT * FROM mytable")
            result = response
            response = None
            return result
