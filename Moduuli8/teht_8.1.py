import mysql.connector
import csv
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='flight_game',
    user='root',
    password="301105",
    autocommit=True
)
def hae_lentoaseman_icao(koodi):
    sql=f"select airport.name, airport.municipality from airport where airport.gps_code='{koodi}'"
    print(sql)
    kursori=yhteys.cursor() 
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(rivi)
    else:
        print("Väärä ICAO koodi")
        
koodi=input("Anna ICAO koodi: ") 
hae_lentoaseman_icao(koodi)