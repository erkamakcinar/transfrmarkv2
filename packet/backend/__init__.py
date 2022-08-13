from flask import Flask
from flaskext.mysql import MySQL
import os
from packet.backend.manipulation import Reader

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
                        "`Isim`			        VARCHAR(40) NOT NULL,"\
                        "`Soyisim`	            VARCHAR(40) NOT NULL,"\
                        "`Maas`			        DOUBLE,"\
                        "`Uyruk`			    VARCHAR(3) NOT NULL,"\
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
                        "`Stadyum`			    VARCHAR(40) NOT NULL,"\
                        "PRIMARY KEY (`Isim`)"\
                    ");"

create_table_oyuncu = "CREATE TABLE `OYUNCU`("\
                        "`OyuncuTc`		        INT NOT NULL,"\
                        "`FormaNo`			    VARCHAR(2),"\
                        "`Takim`			    VARCHAR(40),"\
                        "`Kilo`			        DOUBLE,"\
                        "`Boy`				    INT,"\
                        "`Pozisyon`		        VARCHAR(3) NOT NULL,"\
                        "`Ayak`			        VARCHAR(3),"\
                        "`PiyasaDegeri` 	    DOUBLE,"\
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
                            ");"

create_table_kupa = "CREATE TABLE `KUPA`("\
                        "`KupaId`			    INT NOT NULL AUTO_INCREMENT,"\
                        "`Isim`			        VARCHAR(40) NOT NULL,"\
                        "`Yil`				    INT NOT NULL,"\
                        "`KupaSahibi`		    VARCHAR(40) NOT NULL,"\
                        "PRIMARY KEY (`KupaId`),"\
                        "FOREIGN KEY (`KupaSahibi`) REFERENCES `TAKIM`(`Isim`)"\
                    ");"

#              ---------------------- INSAN ------------------  ----------------------------- OYUNCU -----------------------------
#                Isim     Soyisim    Maas    Uyruk  DgmTarihi   Tc  FrNo      Takım      Kilo   Boy  Pzyn,  Ayak  PysaDgri  IstatistikNo
player_data = [("Altay", "Bayındır", "NULL", "TR", "1998-04-14", 1, "1", "Fenerbahçe", "NULL", 198, "KL", "SAG", 16000000, "NULL"),
                ("Ertugrul", "Cetin", "NULL", "TR", "2003-04-21", 2, "54", "Fenerbahçe" "NULL", 188, "KL", "SAG", 75000, "NULL"),
                ("Attila", "Szalai", "NULL", "MCR", "1998-01-20", 3, "41", "Fenerbahçe" "NULL", 192, "STP", "SOL", 12000000, "NULL"),
                ("Luan", "Peres", "NULL", "BRZ", "1994-07-19", 4, "NULL", "Fenerbahçe" "NULL", 190, "STP", "SOL", 7000000, "NULL"),
                ("Gustavo", "Henrique", "NULL", "BRZ", "1993-03-24", 5, "NULL", "Fenerbahçe" "NULL", 196, "STP", "SAG", 2800000, "NULL"),
                ("Marcel", "Tisserand", "NULL", "FR", "1993-01-10", 6, "32", "Fenerbahçe" "NULL", 190, "STP", "SAG", 2800000, "NULL"),
                ("Serdar", "Aziz", "NULL", "TR", "1990-10-23", 7, "4", "Fenerbahçe" "NULL", 183, "STP", "SAG", 2500000, "NULL")
            ]

insert_into_insan_query = "INSERT INTO INSAN (Isim, Soyisim, Maas, Uyruk, DogumTarihi) VALUES(%s, %s, %s, %s, %s)"
#"10000000000", "Erkam", "Akcinar", 10000000.00, "TC", "1998-11-01"
insert_into_insan_data = [("Erkam", "Akcinar", 10000.00, "TR", "1998-11-01"),
                            ("Altay", "Bayındır", 5 , "TR", "1998-04-14")
                        ]
                    
#team = Reader(file_paths).getTeam()

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

cursor.executemany(insert_into_insan_query, insert_into_insan_data) 
cursor.connection.commit()
from packet.backend import server