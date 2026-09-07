talvi=(12, 1, 2)
kevat=(3, 4, 5)
kesa=(6, 7, 8)
syksy=(9, 10, 11)
kysely=int(input("Anna kuukautesi numero: "))
if kysely in talvi:
    print("Talvi")
elif kysely in kevat:
    print("Kevät")
elif kysely in kesa:
    print("Kesä")
elif kysely in syksy:
    print("Syksy")
else:
    print("Numero ei ole kuukausi")
    