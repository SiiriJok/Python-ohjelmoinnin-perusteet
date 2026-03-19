def tervehdys(nimi):
    print("Hello,", nimi)
    return

def tervehdi_monesti(name, kerrat):
    while kerrat > 0:
        tervehdys(name)
        kerrat -= 1
    return

tervehdi_monesti("Siiri", 3)