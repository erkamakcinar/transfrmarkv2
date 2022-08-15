
from packet.backend import cursor

class Query:
    def __init__(self, queryElements):
        self.queryElements = queryElements
        self.cursor = cursor
    
    def queryBuilder(self, isQueryAboutTeam):
        if(isQueryAboutTeam == True):
            result = []
            team_name = self.queryElements['team_name']
            cup_num = self.queryElements['cup_num']
            total_val = self.queryElements['total_val']
            home_towns = self.queryElements['home_towns']
            
            if(not team_name and not cup_num and not total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim)
                        """
                cursor.execute(query)

            if(team_name and not cup_num and not total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s)
                        """
                print(query)        
                obj = (team_name)
                cursor.execute(query,obj)

            if(not team_name and cup_num and not total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (kupaSayisi = %s)
                        """
                obj = (cup_num)
                cursor.execute(query,obj)

            if(not team_name and not cup_num and total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (piyasaDegeri = %s)
                        """
                obj = (total_val)
                cursor.execute(query,obj) 
            
            if(not team_name and not cup_num and not total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Sehir = %s)
                        """
                obj = (home_towns)
                cursor.execute(query,obj) 
            
            if(team_name and cup_num and not total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND kupaSayisi = %s)
                        """
                obj = (team_name, cup_num)
                cursor.execute(query,obj)             
            
            if(team_name and not cup_num and total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND piyasaDegeri = %s)
                        """
                obj = (team_name, total_val)
                cursor.execute(query,obj)             
            
            if(team_name and not cup_num and not total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND t.Sehir = %s)
                        """
                obj = (team_name, home_towns)
                cursor.execute(query,obj)                  
            
            if(not team_name and cup_num and total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (kupaSayisi = %s AND piyasaDegeri = %s)
                        """
                obj = (cup_num, total_val)
                cursor.execute(query,obj)               
            
            if(not team_name and cup_num and not total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (kupaSayisi = %s AND t.Sehir = %s)
                        """
                obj = (cup_num, home_towns)
                cursor.execute(query,obj)               
            
            if(not team_name and not cup_num and total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (piyasaDegeri = %s AND t.Sehir = %s)
                        """
                obj = (total_val, home_towns)
                cursor.execute(query,obj)                 

            if(team_name and cup_num and total_val and not home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND kupaSayisi = %s AND piyasaDegeri = %s)
                        """
                obj = (team_name, cup_num, total_val)
                cursor.execute(query,obj)                 
            
            if(team_name and cup_num and not total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND kupaSayisi = %s AND t.Sehir = %s)
                        """
                obj = (team_name, cup_num, home_towns)
                cursor.execute(query,obj)    

            if(team_name and not cup_num and total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND piyasaDegeri = %s AND t.Sehir = %s)
                        """
                obj = (team_name, total_val, home_towns)
                cursor.execute(query,obj)    

            if(not team_name and cup_num and total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (kupaSayisi = %s AND piyasaDegeri = %s AND t.Sehir= %s)
                        """
                obj = (cup_num, total_val, home_towns)
                cursor.execute(query,obj)    

            if(team_name and cup_num and total_val and home_towns):
                query = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                            FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                                inner join OYUNCU `o` on (t.Isim = o.Takim)
                                    inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                            GROUP BY (t.Isim) HAVING (t.Isim = %s AND kupaSayisi = %s AND piyasaDegeri = %s AND t.Sehir= %s)
                        """
                obj = (team_name,cup_num, total_val, home_towns)
                cursor.execute(query,obj)    

            cursor.connection.commit()
            result = cursor.fetchall()
            return result
        
        if(isQueryAboutTeam == False):
            result = []
            player_name = self.queryElements['player_name']
            player_team = self.queryElements['player_team']
            player_age_min = self.queryElements['player_age_min']
            player_age_max = self.queryElements['player_age_max']

            if(not player_name and not player_team and not player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc)
                        """
                cursor.execute(query)
            
            if(player_name and not player_team and not player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s)
                        """
                obj = (player_name)
                cursor.execute(query,obj)
            
            
            if(not player_name and player_team and not player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (o.Takim == %s)
                        """
                obj = (player_team)
                cursor.execute(query,obj)
            
            if(not player_name and not player_team and player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (Yas > %s)
                        """
                obj = (player_age_min)
                cursor.execute(query,obj)
            
            if(not player_name  and not player_team and not player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (Yas < %s)
                        """
                obj = (player_age_max)
                cursor.execute(query,obj)            
            
            if(player_name and player_team and not player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND o.Takim = %s)
                        """
                obj = (player_name, player_team)            
                cursor.execute(query,obj)
            
            if(player_name and not player_team and player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND Yas > %s)
                        """
                obj = (player_name, player_age_min)            
                cursor.execute(query,obj)

            if(player_name and not player_team and not player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND Yas < %s)
                        """
                obj = (player_name, player_age_max)            
                cursor.execute(query,obj)
            
            if(not player_name and player_team and player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (o.Takim = %s AND Yas > %s)
                        """
                obj = (player_team, player_age_min)            
                cursor.execute(query,obj)
            
            if(not player_name and player_team and not player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (o.Takim = %s AND Yas < %s)
                        """
                obj = (player_team, player_age_max)            
                cursor.execute(query,obj)

            if(not player_name and not player_team and  player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (Yas > %s AND Yas < %s)
                        """
                if(player_age_min < player_age_max):
                    obj = (player_age_min, player_age_max)            
                    cursor.execute(query,obj)

            if(player_name and player_team and player_age_min and not player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND o.Takim = %s AND Yas > %s)
                        """
                obj = (player_name, player_team, player_age_min)            
                cursor.execute(query,obj)

            if(player_name and player_team and not player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND o.Takim = %s AND Yas < %s)
                        """
                obj = (player_name, player_team, player_age_max)            
                cursor.execute(query,obj)

            if(player_name and not player_team and player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND Yas > %s AND Yas < %s)
                        """
                if(player_age_min < player_age_max):
                    obj = (player_name, player_age_min, player_age_max)            
                    cursor.execute(query,obj)
            
            if(not player_name and player_team and player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (o.Takim = %s AND Yas > %s AND Yas < %s)
                        """
                if(player_age_min < player_age_max):
                    obj = (player_team, player_age_min, player_age_max)            
                    cursor.execute(query,obj)

            if(player_name and player_team and player_age_min and player_age_max):
                query = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                            FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc) HAVING (i.IsimSoyisim REGEXP %s AND o.Takim = %s AND Yas > %s AND Yas < %s)
                        """
                if(player_age_min < player_age_max):
                    obj = (player_name, player_team, player_age_min, player_age_max)            
                    cursor.execute(query,obj)
                                        
            cursor.connection.commit()
            if(player_age_min < player_age_max):
                result = cursor.fetchall()
            return result
        