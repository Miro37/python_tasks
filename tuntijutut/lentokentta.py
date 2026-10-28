import random
class lentokone:
    def __init__(self, nimi, bensa_max, bensa_nykyinen):
        self.nimi=nimi
        self.bensa_max=bensa_max
        self.bensa_nykyinen=bensa_nykyinen
        pass
    def tulosta_tiedot(self):
        print()


    koneet=["Viuhka","Liitäjä", "Teppo"]
    for i in koneet:
        print([i], lentokone.bensa_max)