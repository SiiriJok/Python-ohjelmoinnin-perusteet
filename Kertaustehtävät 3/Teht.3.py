"""
3.
Luo sanakirja nimeltä kirjasto, jossa avaimina ovat kirjojen nimet (merkkijonoja) ja arvoina listat,
jotka sisältävät seuraavat tiedot: [kirjoittaja, julkaisuvuosi, genre]
•Hae ja tulosta yhden kirjan kirjoittaja sekä toisen kirjan genre.
•Muokkaa: vaihda yhden kirjan genre.
•Lisää uusi kirja sanakirjaan.
•Poista yksi olemassa oleva kirja sanakirjasta.
•Tulosta päivitetty sanakirja.
"""

kirjasto = {
    "Tuntematon sotilas": ["Väinö Linna", 1954, "Romaani"],
    "Harry Potter": ["J.K. Rowling", 1997, "Fantasia"],
    "Sinuhe egyptiläinen": ["Mika Waltari", 1945, "Historia"]}

print("Tuntemattoman sotilaan kirjoittaja on:", kirjasto["Tuntematon sotilas"][0])
print("Harry Potterin genre on:", kirjasto["Harry Potter"][2])

kirjasto["Harry Potter"][2] = "Seikkailu"
kirjasto["Nälkäpeli"] = ["Suzanne Collins", 2008, "Fantasia"]

del kirjasto["Sinuhe egyptiläinen"]

print(kirjasto)