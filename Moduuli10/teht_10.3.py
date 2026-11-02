class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin_kerros=ylin_kerros
        self.alin_kerros=alin_kerros
        self.nykyinen_kerros=alin_kerros
        pass
    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        return
    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        return
    def siirry_kerrokseen(self,kohde_kerros):
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        while self.nykyinen_kerros != kohde_kerros:
            if kohde_kerros > self.nykyinen_kerros:
                self.kerros_ylös()
            elif kohde_kerros < self.nykyinen_kerros:
                self.kerros_alas()

class Talo:
    def __init__(self,alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.hissit=[]
        self.alin_kerros=alin_kerros
        for i in range(hissien_lukumäärä): 
            uusi_hissi=Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)
        pass
    def aja_hissiä(self, hissin_numero, kohdekerros):
        ajettavat_hissit=self.hissit[hissin_numero]
        ajettavat_hissit.siirry_kerrokseen(kohdekerros)
    def palohälytys(self):
        print("Palohälytyksen takia kaikki hissit palasivat pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


h=Hissi(1, 50)
talo=Talo(1, 30, 5)
talo.aja_hissiä(3, 7)
talo.palohälytys()