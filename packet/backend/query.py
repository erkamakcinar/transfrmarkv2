
from packet.backend import cursor

class Query:
    def __init__(self, queryElements):
        self.queryElements = queryElements
        self.cursor = cursor
    
    def queryBuilder(self, isQueryAboutTeam):
        print(self.queryElements)
        if(isQueryAboutTeam == True):
            team_name = self.queryElements['team_name']
            cup_num = self.queryElements['cup_num']
            total_val = self.queryElements['total_val']
            home_towns = self.queryElements['home_towns']
            query = """ select * from TAKIM t where (t.isim = %s)"""
            tp = (team_name)
        cursor.executemany(query, [tp])
        cursor.connection.commit()
        return cursor.fetchall()
