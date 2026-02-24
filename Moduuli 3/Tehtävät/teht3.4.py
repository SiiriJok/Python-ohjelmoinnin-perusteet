#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi,
# jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

karkausvuosi = int(input("Ilmoita vuosiluku: "))

if karkausvuosi % 4 == 0:
    print("On karkausvuosi")

elif karkausvuosi % 100 == 0 and karkausvuosi % 400 == 0:
    print("On karkausvuosi")

else:
    print("Ei ole karkausvuosi")