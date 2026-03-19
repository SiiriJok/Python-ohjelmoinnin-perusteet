def inventaario(tavarat):
    print("Repussasi on: ")
    for t in tavarat:
        print("-", t)
    return

reppu = ["juomapullo", "kynä", "avaimet"]
inventaario(reppu)
reppu.append("leipä")
inventaario(reppu)