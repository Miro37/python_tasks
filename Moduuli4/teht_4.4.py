import random 

randomi_numero=random.randint(1,10)

while True: 

    arvaus=int(input("Arvaa luku: "))
    if arvaus > randomi_numero:
        print("Liian suuri arvaus")
    elif arvaus < randomi_numero:
        print("Arvaus on liian pieni")
    elif arvaus == randomi_numero:
        print("Arvasit oikein")
        
        break