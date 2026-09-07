
numerolista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def listanumerot(jaettava):
    parilliset=[]
    for luku in jaettava:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

print(numerolista)  
vastaus=listanumerot(numerolista)
print(vastaus)