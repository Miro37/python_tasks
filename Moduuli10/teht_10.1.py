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
    
h=Hissi(1, 50)
h.siirry_kerrokseen(34)


  
      


