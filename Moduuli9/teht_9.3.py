class Auto:
   def __init__(self, rekisteritunnus, huippunopeus):
      self.rekisteritunnus=rekisteritunnus
      self.huippunopeus=huippunopeus
      self.tamanhetkinen_nopeus=60
      self.kuljettu_matka=2000

   def nopeus_muutos(self, muutos):
    uusi_nopeus=self.tamanhetkinen_nopeus + muutos

    if uusi_nopeus > self.huippunopeus:
      self.tamanhetkinen_nopeus = self.huippunopeus
    elif uusi_nopeus < 0:
      self.tamanhetkinen_nopeus=0
    else:
      self.tamanhetkinen_nopeus=uusi_nopeus
   def kulje(self, matka): 
      self.kuljettu_matka+=float(matka*self.tamanhetkinen_nopeus)
      
auto=Auto("ABC-123", 142)
auto.kulje(1.5)

print(f"Ajetut kilometrit: {auto.kuljettu_matka}")

 