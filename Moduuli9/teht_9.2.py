class Auto:
   def __init__(self, rekisteritunnus, huippunopeus):
      self.rekisteritunnus=rekisteritunnus
      self.huippunopeus=huippunopeus
      self.tamanhetkinen_nopeus=0
      self.kuljettu_matka=0

   def nopeus_muutos(self, muutos):
    uusi_nopeus=self.tamanhetkinen_nopeus + muutos

    if uusi_nopeus > self.huippunopeus:
      self.tamanhetkinen_nopeus = self.huippunopeus
    elif uusi_nopeus < 0:
      self.tamanhetkinen_nopeus=0
    else:
      self.tamanhetkinen_nopeus=uusi_nopeus

auto=Auto("ABC-123", 142)

auto.nopeus_muutos(30)
auto.nopeus_muutos(70)
auto.nopeus_muutos(50)
print(f"Nopeus kiihdytyksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")
auto.nopeus_muutos(-200)
print(f"Nopeus jarrutuksen jälkeen: {auto.tamanhetkinen_nopeus} km/h")