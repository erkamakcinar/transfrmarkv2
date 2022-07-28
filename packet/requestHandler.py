import imp
from packet import cursor

class handler:
    def __init__(self):
        self.cursor = cursor
         
    def tableBuilder(self, response):
        print(response)
        if('team_submit' in response):
            pass
        if('player_submit' in response):
            self.cursor.execute( "SELECT * FROM `Team` where team_id = 1")
            result = self.cursor.fetchall()
            return result

