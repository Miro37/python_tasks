import random
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
        
kilpailijat=[]
for i in range(1, 11):
    rekisteri=f"ABC-{i}"
    max_nopeus=random.randint(100, 200)
    kilpailijat.append(Auto(rekisteri, max_nopeus))

kilpailu_on=True
tunnit=0

while kilpailu_on==True:
    tunnit+=1
    for auto in kilpailijat:
      vauhti_muutos=random.randint(-10,15)
      auto.kaasuta(vauhti_muutos)
      auto.kulje(1)
    if auto.matka>=10000:
        kilpailu_on=False
        
for auto in kilpailijat:
    print(auto.rekisterinumero,"Nopeus:",auto.tamanhetkinen_nopeus,"km","matka:",  auto.matka, "km")




