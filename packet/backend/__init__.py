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
                        "`Tc`				    VARCHAR(11) NOT NULL,"\
                        "`Isim`			        VARCHAR(40) NOT NULL,"\
                        "`Soyisim`	            VARCHAR(40) NOT NULL,"\
                        "`Maas`			        DECIMAL(10,2) NOT NULL,"\
                        "`Uyruk`			    VARCHAR(3) NOT NULL,"\
                        "`DogumTarihi`	        DATE NOT NULL,"\
                        "PRIMARY KEY (`Tc`)"\
                    ");"

create_table_istatistik = "CREATE TABLE `ISTATISTIK`("\
	                        "`IstNo`			    INT NOT NULL AUTO_INCREMENT,"\
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
                        "`OyuncuTc`		        VARCHAR(11) NOT NULL,"\
                        "`Kilo`			        DECIMAL(5,2) NOT NULL,"\
                        "`PiyasaDegeri` 	    DECIMAL(11,2) NOT NULL,"\
                        "`Boy`				    INT NOT NULL,"\
                        "`Pozisyon`		        VARCHAR(3) NOT NULL,"\
                        "`Ayak`			        VARCHAR(3) NOT NULL,"\
                        "`IstatistikNo`	        INT NOT NULL,"\
                        "`Takim`			    VARCHAR(40) NOT NULL,"\
                        "PRIMARY KEY (`OyuncuTc`),"\
                        "FOREIGN KEY (`OyuncuTc`) REFERENCES `INSAN`(`Tc`),"\
                        "FOREIGN KEY (`IstatistikNo`) REFERENCES `ISTATISTIK`(`IstNo`),"\
                        "FOREIGN KEY (`Takim`) REFERENCES `TAKIM`(`Isim`)"\
                    ");"

create_table_teknikdirektor = "CREATE TABLE `TEKNIKDIREKTOR`("\
                                "`TeknikDirektorTc`	                VARCHAR(11) NOT NULL,"\
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

cursor.connection.commit()                
from packet.backend import server