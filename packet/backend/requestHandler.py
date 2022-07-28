from packet.backend import cursor

class handler:
    def __init__(self):
        self.cursor = cursor
         
    def tableBuilder(self, response):
        print(response)
        if('team_submit' in response):
            pass
        if('player_submit' in response):
            #self.cursor.execute( "SELECT * FROM mytable")
            result = response
            response = None
            return result

