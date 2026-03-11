nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(nimet)

nimet2 = ["Allu", "Ninni"]

nimet.append("Matti")
nimet.insert(4, "Siiri")

print(nimet)
print(nimet[1])
print(nimet[1:3])

print(nimet2)


#-----


nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(nimet)

"""
if "Matti" in nimet:
    print("Matti Löytyi")

else:
    print("Ei Mattia")
"""

nimet.sort()
print(nimet)
