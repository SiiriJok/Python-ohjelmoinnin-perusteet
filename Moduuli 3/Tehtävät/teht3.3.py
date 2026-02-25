#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

sukupuoli = input("Oletko mies vai nainen? ")
hemo = float(input("Mikä on hemoglobiiniarvosi? "))

if sukupuoli == "mies":

    if hemo > 195:
        print("korkea hemoglobiiniarvo")

    elif 134 <= hemo <= 195:
        print("normaali hemoglobiiniarvo")

    else:
        print("alhainen hemoglobiiniarvo")

else:

    if hemo > 175:
        print("korkea hemoglobiiniarvo")

    elif 117 <= hemo <= 175:
        print("normaali hemoglobiiniarvo")

    else:
        print("alhainen hemoglobiiniarvo")