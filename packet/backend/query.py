
from packet.backend import cursor

class Query:
    def __init__(self, queryElements):
        self.queryElements = queryElements
        self.cursor = cursor
    
    def queryBuilder(self, isQueryAboutTeam):
        if(isQueryAboutTeam == True):
            team_name = self.queryElements['team_name']
            cup_num = self.queryElements['cup_num']
            total_val = self.queryElements['total_val']
            home_towns = self.queryElements['home_towns']
            query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                        FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                            inner join OYUNCU `o` on (t.Isim = o.Takim)
                                inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                        GROUP BY (t.Isim)
                    """
            cursor.execute(query)
            cursor.connection.commit()
            result = cursor.fetchall()
            return result
        
        if(isQueryAboutTeam == False):
            query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                        FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc);
                    """
            cursor.execute(query)
            cursor.connection.commit()
            result = cursor.fetchall()
            return result
        