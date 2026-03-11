#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat
#ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat
#oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.

oikea_t = "python"
oikea_s = "rules"

arvaus = 0

while arvaus < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    if tunnus == oikea_t and salasana == oikea_s:
        print("Tervetuloa!")
        break
    elif tunnus != oikea_t or salasana != oikea_s:
        print("Salasana tai tunnus on väärin, yritä uudelleen!")
        arvaus += 1

else:
    print("Pääsy evätty")
