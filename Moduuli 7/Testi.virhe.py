try:

    luku = int(input("Anna luku jolla jaetaan: "))
    tulos = 10/luku
    print("tulos on", tulos)
except ZeroDivisionError:
    print("Nollalla ei voi jakaa")

print("Ohjelma suoritettu")