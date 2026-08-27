import random
arpa=[]
arpakuutio=int(input("Anna arpakuutioiden määrä:"))
for i in range(arpakuutio):
    luku=random.randint(1, 6)
    arpa.append(luku)
print(arpa)
summa = sum(arpa)
print(f"Noppien lukujen summa on {summa}")

