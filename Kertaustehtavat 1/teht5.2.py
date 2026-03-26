laskutapa = input("Haluatko laskea plus, miinus, kerto vai jako laskun? ")
luku_1 = float(input("Anna luku 1: "))
luku_2 = float(input("Anna luku 2: "))

while True:
    if laskutapa == "plus":
        print(luku_1 + luku_2)
    elif laskutapa == "miinus":
        print(luku_1 - luku_2)
    elif laskutapa == "kerto":
        print(luku_1 * luku_2)
    elif laskutapa == "jako":
        print(luku_1 / luku_2)
    else:
        break

    laskutapa = input("Haluatko laskea plus, miinus, kerto vai jako laskun? ")
    luku_1 = float(input("Anna luku 1: "))
    luku_2 = float(input("Anna luku 2: "))