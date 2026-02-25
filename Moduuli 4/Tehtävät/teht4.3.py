#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku1 = input("Anna luku: ")

luku = int(luku1)
pienin = luku
suurin = luku

while True:
    luku1 = input("Anna luku: ")
    if luku1 == "":
        break
    luku = int(luku1)
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku
print(f"Pienin luku on {pienin} ja suurin luku on {suurin}")

