
def neliosumma(a, b):
    _tulos = a**2 + b**2
    return _tulos

luku1 = float(input("Luku 1: "))
luku2 = float(input("Luku 2: "))

# Tallennetaan funktion palauttama arvo globaaliin "tulos" muuttujaan
tulos = neliosumma(luku1, luku2)

print("Laskun tulos on", tulos)

# Funktion palauttama arvo tulostetaan, mutta ei tallenneta, joten sitä ei voi käyttää uudelleen
print(neliosumma(tulos, luku1))