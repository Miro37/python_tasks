nimet = set()
while True:
    nimi=input("Anna nimi: ").lower()
    if nimi =="":
        print(sorted(nimet))
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimet.remove(nimi)
    elif nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)
   
