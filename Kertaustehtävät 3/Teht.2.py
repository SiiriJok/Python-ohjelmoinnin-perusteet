"""
2.
Luo sanakirja, jossa oppilaiden nimet ovat avaimina ja listat arvoina.
Jokaisen listan tulee sisältää: [nimi, vuosiluokka, lempiaine]
•Hae ja tulosta yhden oppilaan vuosiluokka sekä toisen oppilaan lempiaine.
•Muokkaa sanakirjaa vaihtamalla yhden oppilaan lempiaine.
•Lisää uusi oppilas sanakirjaan.
•Poista yksi olemassa oleva oppilas sanakirjasta.
•Tulosta päivitetty sanakirja.
"""

oppilaat = {
    "Siiri": ["Siiri", 7, "Liikunta"],
    "Sara": ["Sara", 8, "Historia"],
    "Oona": ["Oona", 9, "Musiikki"]}

print("Siirin vuosiluokka on", oppilaat["Siiri"][1])
print("Saran lempiaine on", oppilaat["Sara"][2])

oppilaat["Sara"][2] = "Liikunta"

oppilaat["Nooa"] = ["Nooa", 1, "Välitunti"]

del oppilaat["Siiri"]

print(oppilaat)