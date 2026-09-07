import random
def noppa(tahkot):
   return random.randint(1,tahkot)
max=int(input("Anna nopan maksimi silmäluku: "))
heitto=""
while heitto != max:
   heitto=noppa(max)
   print(heitto)



