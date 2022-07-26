import imp
from packet import cursor

class handler:
    def __init__(self):
        self.cursor = cursor
         
    def tableBuilder(self, response):
        if(response['submit'] == 'OyuncuBtn'):
            pass
        if(response['submit'] == 'TakımBtn'):
            self.cursor.execute( "SELECT * FROM `Team` where team_id = 1")
            result = self.cursor.fetchall()
            return result

