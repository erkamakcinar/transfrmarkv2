from packet.backend import cursor

class handler:
    def __init__(self):
        self.cursor = cursor
         
    def tableBuilder(self, response):
        print(response)
        if('team_submit' in response):
           team_name = response['team_name'];
           query = """ select * from TAKIM t where (t.isim = %s)"""
           cursor.executemany(query, [(team_name)])
           cursor.connection.commit()
           return cursor.fetchall()

        if('player_submit' in response):
            #self.cursor.execute( "SELECT * FROM mytable")
            result = response
            response = None
            return result

