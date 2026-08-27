tunnus="python"
salasana="rules"
yritykset = 0
while True:
    kauttaja_tunnus=input("Anna käyttäjätunnus: ")
    kauttaja_salasana=input("Anna salasana: ")
    if kauttaja_tunnus == tunnus and kauttaja_salasana == salasana:

        print("Tervetuloa")
        break
    elif kauttaja_tunnus != tunnus and kauttaja_salasana != salasana:
            yritykset +=1
            if yritykset == 5:
                print("Pääsy evätty")
                break
