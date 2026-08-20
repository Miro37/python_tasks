leiviska=float(input("Anna leiviskät: "))
naula=float(input("Anna naulat: "))
luodit=float(input("Anna luodit: "))

luoti_math=luodit*0.0133
naula_math=naula*32
leiviska_math=leiviska*20

luotien_paino=luoti_math * luodit
naula_paino=naula * naula_math
leiviska_paino=leiviska * leiviska_math

vastaus=luotien_paino+naula_paino+leiviska_paino
vastauskg=int(vastaus//1000)
vastausg=int(vastaus % 1000)



print(f"Massa nykymittojen mukaan: {vastauskg}kg ja {vastausg}g  ")

