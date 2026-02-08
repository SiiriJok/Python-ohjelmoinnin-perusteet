#funktio
def tervehdi():
    print("Moi! \n")
    return
tervehdi()

def tervehdi():
    print("Moi!")
    return

print("Päivä alkaa tervehdyksellä.")
tervehdi()
print("Sitten siirrytään muihin asioihin.")

print("")

def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print ("Tervehditään lisää.\n")
tervehdi(2)

import random

# Arpoo luvun väliltä 1-10 (1 ja 10 mukaan lukien)
luku = random.randint(1, 10)
print(luku)
