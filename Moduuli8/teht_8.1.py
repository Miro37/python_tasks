import mysql.connector
import csv
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='airports_db',
    user='root',
    password="301105"
    
)