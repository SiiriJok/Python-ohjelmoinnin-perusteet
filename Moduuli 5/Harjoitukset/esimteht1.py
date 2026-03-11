varit = ["Pinkki", "Sininen", "Keltainen", "Oranssi"]

lempivari = input("Mikä on lempivärisi? ")

if lempivari in varit:
    print("Hyvä valinta!")

else:
    print("Outo valinta...")

#------

varit = ["pinkki", "sininen", "keltainen", "oranssi"]

lempivari = input("Mikä on lempivärisi? ").lower()

loytyy = False

for v in varit:
    if lempivari == v:
        loytyy = True

if loytyy:
    print("Hyvä valinta!")
else:
    print("Outo valinta...")