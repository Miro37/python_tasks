def bensa(litroina):
    litra = litroina * 3.789
    return litra
while True:
    maara=float(input("Anna bensiinin määrä nestegalloina: "))
    if maara >= 0:
        litrat=bensa(maara)
        print(f"Nestegallonit litroina:{litrat:.2f} ")
    else:
        break
