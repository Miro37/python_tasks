import math
pii=math.pi
def pizarvo(hinnat, halkaisijat):
    sade_metriksi=(halkaisijat/100) /2
    koko=(sade_metriksi**2)*pii
    return hinnat/koko
pizzakoko1=float(input("Anna ensimmäisen pizzan halkaisija: "))
pizzakoko2=float(input("Anna toisen pizzan halkaisija: "))
pizzahinta1=float(input("Anna ensimmäisen pizzan hinta: "))
pizzahinta2=float(input("Anna toisen pizzan hinta: "))
arvo1=pizarvo(pizzahinta1, pizzakoko1)
arvo2=pizarvo(pizzahinta2, pizzakoko2)
if arvo1 < arvo2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    print("Toinen pizza antaa paremman vastineen")