
suurin = None
pienin = None

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break

    luku = int(syote)
    if suurin is None or luku > suurin:
        suurin = luku
    if pienin is None or luku < pienin:
        pienin = luku

print(f"Suurin luku: {suurin}")
print(f"Pienin luku: {pienin}")
