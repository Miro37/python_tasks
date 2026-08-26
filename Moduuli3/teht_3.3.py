sukupuoli=input("Anna sukupuoli: ").lower()

if sukupuoli != "nainen" and sukupuoli != "mies":
    print("input error")
    exit()

hemo_arvo=int(input("Anna hemoglobiiniarvo: "))

if sukupuoli=="nainen" and 117 <=hemo_arvo <= 175:
    print("Hemoglobiiniarvo on normaali")
elif sukupuoli == "nainen" and hemo_arvo > 175:
    print("Hemoglobiiniarvo on korkea")

elif sukupuoli == "mies" and 134 <=hemo_arvo <= 195:
    print("Hemoblogiiniarvo on normaali.")
elif sukupuoli =="mies" and hemo_arvo > 195:
    print("Hemoglobiiniarvo on korkea")

else:
    print("Hemoglobiiniarvo on alhainen.")




