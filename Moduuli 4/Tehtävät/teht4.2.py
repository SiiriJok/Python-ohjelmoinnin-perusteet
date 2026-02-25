#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = (float(input("Anna tuumat (negatiivinen lopettaa): ")))

while tuuma > 0:
    if tuuma < 0:
        break
    cm = tuuma * 2.54
    print("On senttimetreinä ", cm,)
    tuuma = (float(input("Anna tuumat (negatiivinen lopettaa): ")))

print("Loppu")