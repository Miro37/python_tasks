from geopy import distance
import mysql.connector
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='flight_game',
    user='root',
    password="301105",
    autocommit=True
)
def hae_kentan_koodit(koodi):
    sql=f"select airport.latitude_deg, airport.longitude_deg from airport where gps_code='{koodi}'"
    print(sql)
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print({rivi})
    else:
            print("Väärä koodi")
koodi1=input("Anna ICAO-koodi: ").upper
koodi2=input("Anna toinen ICAO-koodi: ").upper

paikka1=hae_kentan_koodit(koodi1)
paikka2=hae_kentan_koodit(koodi2)
print(f"Ensimmäinen paikka: {paikka1}")
print(f"Toinen paikka: {paikka2}")
vastaus=(distance.distance(paikka1, paikka2).km)
print(f"Näiden välillä on {vastaus:.3f}km")