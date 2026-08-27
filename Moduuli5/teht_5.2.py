lista=[]
while True:
    luku=input("Anna luku:")
    if luku == "":
        break
    else:
        numero= int(luku)
        lista.append(numero)
    lista.sort(reverse=True)
    print(lista)
    for ensimmäiset in lista[:5]:
        print(ensimmäiset)



