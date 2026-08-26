kuha=float(input("Anna kuhan pituus: "))
if kuha < 37:
    alamitta=37-kuha
    alamitta_vastaus=37-alamitta
    print(f"Kuhasta puuttuu {alamitta}cm laske se takaisin veteen")
else:      
    print("kuha on hyvän mittainen")