class Auto:
    def __init__(self,rekisterinumero,huippunopeus):
        self.rekisterinumero=rekisterinumero
        self.huippunopeus=huippunopeus
        self.tamanhetkinen_nopeus=0
        self.matka=0
        pass
    def kaasuta(self,muutos):
        
        uusi_nopeus=self.tamanhetkinen_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus=self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus=0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus
    def kulje(self,aika):
       self.matka += self.tamanhetkinen_nopeus * aika
class Sähköauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti=akkukapasiteetti
        super().__init__(rekisterinumero, huippunopeus)
class Polttomoottoriauto(Auto):
    def __init__(self,rekisterinumero, huippunopeus, bensatankinkoko):
        self.bensatankinkoko=bensatankinkoko
        super().__init__(rekisterinumero, huippunopeus)
        
kilpailijat=[]
kilpailijat.append(Sähköauto("ABC-15", 180, 52.5))
kilpailijat.append(Polttomoottoriauto("ACD-123", 165, 32.3))
kilpailu_on=True
tunnit=0
for auto in kilpailijat:
    auto.kaasuta(auto.huippunopeus)
    

while kilpailu_on==True:
    tunnit+=1
    for auto in kilpailijat:
      auto.kulje(1)
      print(auto.rekisterinumero,"tunti:", tunnit,"matka:",  auto.matka, "km")
    if tunnit==3:
        kilpailu_on=False

 


