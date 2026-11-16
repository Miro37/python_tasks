import mysql.connector
import csv
from flask import Flask, request
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='flight_game',
    user='root',
    password="301105",
    autocommit=True
)
app = Flask(__name__)
@app.route('/kentta/<koodi>')
def hae_lentoaseman_icao(koodi):
    koodi_str=request.args.get("koodi")
    sql=f"select airport.name, airport.municipality from airport where airport.gps_code='{koodi}'"
    koodi=koodi_str
    print(sql)
    kursori=yhteys.cursor() 
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if tulos:
        tulos_str=""
        for rivi in tulos:
            tulos_str += (f"{rivi[0]}, {rivi[1]} <br>")
            return tulos_str
    else:
        return ("Luuseri ei toimi")
if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1, port=3000')
        