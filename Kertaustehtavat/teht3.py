import math

while True:
    numero = int(input("Anna numero: "))
    if numero == 0:
        break
    elif numero < 0:
        print("Virheellinen numero")
    elif numero > 0:
        from math import sqrt
        print(sqrt(numero))

