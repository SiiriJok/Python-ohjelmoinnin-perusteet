"""
summa = 0

while True:
    numero = int(input("Anna luku jonka haluat lisätä, -1 lopettaa: "))
    if numero == -1:
        break
    elif numero >= 10:
        continue
    summa += numero

print("Summa on:", summa)
"""


kasky = input("Annetaanko lisää kolikoita? ")

while kasky != "ei":
    if kasky == "ryöstö":
        print("Kolikot on ryöstetty")
        break
    print("Annetaan kolikko.")
    kasky = input("Annetaanko lisää kolikoita? ")

else:
    print("Ohjelma loppuu")