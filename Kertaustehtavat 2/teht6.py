def plus(a, b):
    return a + b

def miinus(a, b):
    return a - b

def kerto(a, b):
    return a * b

def jako(a, b):
    return a / b


laskutapa = input("Haluatko laskea plus, miinus, kerto vai jako laskun? ")
luku_1 = float(input("Anna luku 1: "))
luku_2 = float(input("Anna luku 2: "))

while True:
    if laskutapa == "plus":
        print(plus(luku_1, luku_2))
    elif laskutapa == "miinus":
        print(miinus(luku_1, luku_2))
    elif laskutapa == "kerto":
        print(kerto(luku_1, luku_2))
    elif laskutapa == "jako":
        print(jako(luku_1, luku_2))
    else:
        break

    laskutapa = input("Haluatko laskea plus, miinus, kerto vai jako laskun? ")
    luku_1 = float(input("Anna luku 1: "))
    luku_2 = float(input("Anna luku 2: "))