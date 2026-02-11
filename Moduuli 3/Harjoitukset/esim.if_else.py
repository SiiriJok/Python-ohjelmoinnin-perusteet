raha = float(input("Kuinka paljon sinulla on rahaa? "))

if raha >= 5:
    print("Tässä kahvisi ole hyvä!")

else:
    puuttuva = 5 - raha
    print("Sori, sinulta puuttuu", puuttuva)

print("Kiitos hei!")


numero = int(input("Anna kokonaisluku: "))

if numero > 0:
    print(" Luku on positiivinen")

else:
    print(" Luku on negatiivinen")