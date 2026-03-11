ostoslista = ["maito", "porkkana", "kala"]

print("\nOSTOSLISTA:", ostoslista)
print("Mennään kauppaan...\n")

while ostoslista:
    ostos = input("Kirjoita asia jonka ostit: ").lower()

    if ostos in ostoslista:
        ostoslista.remove(ostos)
        print("Jäljellä:", ostoslista)
    else:
        print("Tuo EI OLLUT listallasi!!")

print("Ostokset suoritettu")