import mysql.connector
import csv
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='airports_db',
    user='root',
    password="301105"
)
def hae_lentoaseman_icao(koodi):
    sql=f"select airport.name, airport.municipality from airport where airport.gps_code='{koodi}'"
    print(sql)
    