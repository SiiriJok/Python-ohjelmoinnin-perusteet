tarina = ""
edellinen_sana = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")
    if sana == "loppu":
        break
    elif sana == edellinen_sana:
        break
    elif sana != "loppu":
        tarina = tarina + " " + sana
    edellinen_sana = sana
print(tarina)

