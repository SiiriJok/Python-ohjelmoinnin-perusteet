palkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ")

if paiva != "Sunnuntai":
    paivapalkka = palkka * tunnit
    print("Päiväpalkka: ", paivapalkka)

else:
    paivapalkka = (palkka * 2) * tunnit
    print("Päiväpalkka: ", paivapalkka)
