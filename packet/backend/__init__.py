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
drop_database_query = "DROP DATABASE IF EXISTS 'transfermark_v2';"
create_database_query = "CREATE DATABASE 'transfermark_v2';"
use_query = "USE 'transfermark_v2';"
create_table_query = "CREATE TABLE `Team` ("\
                    "`team_id` tinyint(4) NOT NULL AUTO_INCREMENT,"\
                    "`team_name` varchar(50) NOT NULL,"\
                    "`stadium_name` varchar(50),"\
                    "`hometown` varchar(50),"\
                    "PRIMARY KEY (`team_id`)"\
                    ") ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"



#team = Reader(file_paths).getTeam()


cursor.execute(drop_database_query) 
cursor.execute(create_database_query)
cursor.execute(use_query)
#cursor.execute(create_table_query)         
cursor.connection.commit()                
from packet.backend import server