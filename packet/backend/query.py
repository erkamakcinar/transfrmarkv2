
from packet.backend import cursor

class Query:
    def __init__(self, queryElements):
        self.qE = queryElements
        self.cursor = cursor
    
    def queryBuilder(self):
        query = """ select * from TAKIM t where (t.isim = %s)"""
        tp = (self.qE)
        cursor.executemany(query, [tp])
        cursor.connection.commit()
        return cursor.fetchall()