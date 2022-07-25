from urllib.parse import uses_query
from flask import Flask
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'AL266493'
app.config['MYSQL_DATABASE_DB'] = 'transfermark_v2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

db = MySQL(app)

conn = db.connect()
cursor =conn.cursor()
drop_database_query = "DROP DATABASE IF EXISTS `sql_invoicing`;"
create_database_query = "CREATE DATABASE `sql_invoicing`;"
use_query = "USE `sql_invoicing`;"
create_table_query = "CREATE TABLE `payment_methods` ("\
                    "`payment_method_id` tinyint(4) NOT NULL AUTO_INCREMENT,"\
                    "`name` varchar(50) NOT NULL,"\
                    "PRIMARY KEY (`payment_method_id`)"\
                    ") ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"

cursor.execute(drop_database_query) 
cursor.execute(create_database_query)
cursor.execute(use_query)
cursor.execute(create_table_query)              
#db.connection.commit()
#cursor.close()                
#from packet import server