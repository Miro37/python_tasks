lentokentät = {"Thomas C Russel Field": "ADDE",
               "Afutara Airport": "AGAF",
               "Ulawa Airport": "Agar",
               "Atoifi": "Agat"}
while True:
    print("Valitse toiminto:")
    print("1 = syötä uusi lentokenttä")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta ohjelma")
    valinta = int(input("Valitse 1-3: "))
    if valinta == 1:
        kenttänimi=input("Anna lentokentän nimi: ")
        icao=input("Anna lentokentän ICAO: ").upper()
        print("Lentokenttä lisätty")
        lentokentät[icao] = kenttänimi
    elif valinta ==2:
        haku=input("Anna ICAO: ").upper()
        if haku in lentokentät:
            print(lentokentät[haku])
        else:
            print("Tuntematon ICAO")
    elif valinta == 3:
        break
    else:
        print("Väärä numero")