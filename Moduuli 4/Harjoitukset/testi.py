tuuma = (float(input("Anna tuumat (negatiivinen lopettaa): ")))

while tuuma > 0:
    cm = tuuma * 2.54
    print("On senttimetreinä ", cm, )
    tuuma = (float(input("Anna tuumat (negatiivinen lopettaa): ")))
    if tuuma < 0:
        break

print("Loppu")