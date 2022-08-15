from flask import Flask
from flaskext.mysql import MySQL
import os
import csv



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'AL266493'
app.config['MYSQL_DATABASE_DB'] = 'transfermark_v2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

db = MySQL(app)

file_paths = ["packet/db_data/cup/date.csv", "packet/db_data/cup/name.csv", "packet/db_data/human/country.csv", "packet/db_data/human/date.csv", "packet/db_data/human/name.csv", "packet/db_data/human/surname.csv", "packet/db_data/human/tc.csv", "packet/db_data/human/wage.csv", "packet/db_data/player/height.csv", "packet/db_data/player/position.csv", "packet/db_data/player/statistics.csv", "packet/db_data/player/value.csv", "packet/db_data/player/weight.csv", "packet/db_data/team/city.csv", "packet/db_data/team/name.csv","packet/db_data/team/stadium.csv"]

conn = db.connect()
cursor =conn.cursor()
drop_database_query = "DROP DATABASE IF EXISTS `transfermark_v2`;"
create_database_query = "CREATE DATABASE `transfermark_v2`;"
use_query = "USE `transfermark_v2`;"

create_table_insan = "CREATE TABLE `INSAN` ("\
                        "`Tc`				    INT AUTO_INCREMENT,"\
                        "`IsimSoyisim`		    VARCHAR(80) NOT NULL,"\
                        "`Maas`			        INT,"\
                        "`Uyruk`			    VARCHAR(40) NOT NULL,"\
                        "`DogumTarihi`	        DATE,"\
                        "PRIMARY KEY (`Tc`)"\
                    ");"

create_table_istatistik = "CREATE TABLE `ISTATISTIK`("\
	                        "`IstNo`			    INT AUTO_INCREMENT,"\
                            "`AtilanGol`		    INT NOT NULL,"\
                            "`YenenGol`		        INT NOT NULL,"\
                            "`KupaSayisi`		    INT NOT NULL,"\
                            "PRIMARY KEY (`IstNo`)"\
                        ");"

create_table_takim = "CREATE TABLE `TAKIM`("\
	                    "`Isim`			        VARCHAR(40) NOT NULL,"\
                        "`Sehir`			    VARCHAR(40) NOT NULL,"\
                        "`Stadyum`			    VARCHAR(100) NOT NULL,"\
                        "PRIMARY KEY (`Isim`)"\
                    ");"

create_table_oyuncu = "CREATE TABLE `OYUNCU`("\
                        "`OyuncuTc`		        INT NOT NULL,"\
                        "`FormaNo`			    VARCHAR(5),"\
                        "`Takim`			    VARCHAR(40),"\
                        "`Kilo`			        DOUBLE,"\
                        "`Boy`				    INT,"\
                        "`Pozisyon`		        VARCHAR(40) NOT NULL,"\
                        "`Ayak`			        VARCHAR(5),"\
                        "`PiyasaDegeri` 	    INT,"\
                        "`IstatistikNo`	        INT,"\
                        "PRIMARY KEY (`OyuncuTc`),"\
                        "FOREIGN KEY (`OyuncuTc`) REFERENCES `INSAN`(`Tc`),"\
                        "FOREIGN KEY (`IstatistikNo`) REFERENCES `ISTATISTIK`(`IstNo`),"\
                        "FOREIGN KEY (`Takim`) REFERENCES `TAKIM`(`Isim`)"\
                    ");"

create_table_teknikdirektor = "CREATE TABLE `TEKNIKDIREKTOR`("\
                                "`TeknikDirektorTc`	                INT NOT NULL,"\
                                "`YonettigiTakim`		            VARCHAR(40) NOT NULL,"\
                                "PRIMARY KEY (`TeknikDirektorTc`),"\
                                "FOREIGN KEY (`YonettigiTakim`) REFERENCES `TAKIM`(`Isim`),"\
                                "FOREIGN KEY (`TeknikDirektorTc`) REFERENCES `INSAN`(`Tc`)"\
                            ") AUTO_INCREMENT=515;"

create_table_kupa = "CREATE TABLE `KUPA`("\
                        "`KupaId`			    INT AUTO_INCREMENT,"\
                        "`Isim`			        VARCHAR(80) NOT NULL,"\
                        "`Yil`				    VARCHAR(40) NOT NULL,"\
                        "`KupaSahibi`		    VARCHAR(40) NOT NULL,"\
                        "PRIMARY KEY (`KupaId`),"\
                        "FOREIGN KEY (`KupaSahibi`) REFERENCES `TAKIM`(`Isim`)"\
                    ");"

with open('packet/db_data/PL_Human_o_Tables.csv', newline='') as f:
    reader = csv.reader(f)
    playerHumanData = [tuple(row) for row in reader]
    del playerHumanData[0]

with open('packet/db_data/PL_Human_td_Tables.csv', newline='') as f:
    reader = csv.reader(f)
    CoachHumanData = [tuple(row) for row in reader]
    del CoachHumanData[0]

with open('packet/db_data/PL_TeamsTables.csv', newline='') as f:
    reader = csv.reader(f)
    teamData = [tuple(row) for row in reader]
    del teamData[0]

with open('packet/db_data/PL_PlayerTables.csv', newline='') as f:
    reader = csv.reader(f)
    playerData = [tuple(row) for row in reader]
    del playerData[0]

with open('packet/db_data/PL_CoachTables.csv', newline='') as f:
    reader = csv.reader(f)
    coachData = [tuple(row) for row in reader]
    del coachData[0]

with open('packet/db_data/PL_CupTables.csv', newline='') as f:
    reader = csv.reader(f)
    cupData = [tuple(row) for row in reader]
    del cupData[0]

insert_into_insan_o_query = "INSERT INTO INSAN (Tc, IsimSoyisim, Maas, Uyruk, DogumTarihi) VALUES(%s, %s, %s, %s, %s)"

insert_into_insan_td_query = "INSERT INTO INSAN (Tc, IsimSoyisim, Uyruk, DogumTarihi) VALUES(%s, %s, %s, %s)"

insert_into_takim_query = "INSERT INTO TAKIM (Isim, Sehir, Stadyum) VALUES(%s, %s, %s)"

insert_into_oyuncu_query = "INSERT INTO OYUNCU (OyuncuTc, FormaNo, Takim, Kilo,  Boy, Pozisyon, Ayak, PiyasaDegeri) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

insert_into_teknikDirektor_query = "INSERT INTO TEKNIKDIREKTOR (TeknikDirektorTc, YonettigiTakim) VALUES(%s, %s)"

instert_into_kupa_query = "INSERT INTO KUPA (Isim, Yil, KupaSahibi) VALUES(%s, %s, %s)"

def_query_teams = """ SELECT t.Isim, t.Sehir, t.Stadyum, COUNT(DISTINCT k.KupaSahibi,k.KupaId) AS `kupaSayisi`, SUM(o.PiyasaDegeri) AS `piyasaDegeri`
                        FROM TAKIM `t` left outer join KUPA `k` on (t.Isim = k.KupaSahibi)
                            inner join OYUNCU `o` on (t.Isim = o.Takim)
                                inner join INSAN `i` on(i.Tc = o.OyuncuTc)
                        GROUP BY (t.Isim)
                    """

def_query_players = """ SELECT i.IsimSoyisim, o.Takim, i.Uyruk, TIMESTAMPDIFF( YEAR, i.DogumTarihi,  CURDATE()) AS Yas, o.PiyasaDegeri, o.Pozisyon
                        FROM OYUNCU o inner join INSAN i on (o.OyuncuTc = i.Tc)
                    """

cursor.execute(drop_database_query) 
cursor.execute(create_database_query)
cursor.execute(use_query)

#table creating order is important
cursor.execute(create_table_insan)
cursor.execute(create_table_istatistik)
cursor.execute(create_table_takim)
cursor.execute(create_table_oyuncu)
cursor.execute(create_table_teknikdirektor)
cursor.execute(create_table_kupa)   

#inserting data
cursor.executemany(insert_into_insan_o_query, playerHumanData)
cursor.executemany(insert_into_insan_td_query, CoachHumanData)
cursor.executemany(insert_into_takim_query, teamData)  
cursor.executemany(insert_into_oyuncu_query, playerData)
cursor.executemany(insert_into_teknikDirektor_query, coachData)
cursor.executemany(instert_into_kupa_query, cupData)

cursor.execute(def_query_players)
def_table_players = cursor.fetchall()
cursor.execute(def_query_teams)
def_table_teams = cursor.fetchall()
cursor.connection.commit()

'''
insert_into_insan_data = [("Erkam Akcinar", 10000.00, "TR", "1998-11-01"),
                            ("Altay Bayındır", 5 , "TR", "1998-04-14")
                        ]
'''
'''
insert_into_oyuncu_data = [("1", "1", "Fenerbahçe", 73, "198", "KL", "SAG", "16000000"),
                            ("2", "54", "Fenerbahçe", None, "188", "KL", "SAG", "75000")
                        ]
''' 
'''
#              ---------------------- INSAN ------------------  ----------------------------- OYUNCU -----------------------------
#                Isim     Soyisim    Maas    Uyruk  DgmTarihi   Tc  FrNo      Takım      Kilo   Boy  Pzyn,  Ayak  PysaDgri  IstatistikNo
oyuncu_data = [("Altay", "Bayındır", "NULL", "TR", "1998-04-14", 1, "1", "Fenerbahçe", "NULL", 198, "KL", "SAG", 16000000, "NULL"),
                ("Ertugrul", "Cetin", "NULL", "TR", "2003-04-21", 2, "54", "Fenerbahçe" "NULL", 188, "KL", "SAG", 75000, "NULL"),
                ("Attila", "Szalai", "NULL", "MCR", "1998-01-20", 3, "41", "Fenerbahçe" "NULL", 192, "STP", "SOL", 12000000, "NULL"),
                ("Luan", "Peres", "NULL", "BRZ", "1994-07-19", 4, "NULL", "Fenerbahçe" "NULL", 190, "STP", "SOL", 7000000, "NULL"),
                ("Gustavo", "Henrique", "NULL", "BRZ", "1993-03-24", 5, "NULL", "Fenerbahçe" "NULL", 196, "STP", "SAG", 2800000, "NULL"),
                ("Marcel", "Tisserand", "NULL", "FR", "1993-01-10", 6, "32", "Fenerbahçe" "NULL", 190, "STP", "SAG", 2800000, "NULL"),
                ("Serdar", "Aziz", "NULL", "TR", "1990-10-23", 7, "4", "Fenerbahçe" "NULL", 183, "STP", "SAG", 2500000, "NULL")
            ]
'''
from packet.backend import server