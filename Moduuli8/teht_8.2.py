import mysql.connector
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database='flight_game',
    user='root',
    password="301105",
    autocommit=True
)
def hae_maan_kenttien_tyyppi(tunnus):
    sql=f"select airport.type, count(*) from airport join country on airport.iso_country=country.iso_country where country.iso_country='{tunnus}'group by airport.type"
    print(sql)
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(rivi)
    else:
        print("Väärä tunnus")

tunnus=input("Anna maan tunnus: ")
hae_maan_kenttien_tyyppi(tunnus)
