# Kysytään pituus ja paino
pituus = float(input("Kuinka pitkä olet? "))
paino = float(input("Kuinka paljon painat? "))

bmi = paino / (pituus / 100) **2

print("BMI:si on", bmi)
