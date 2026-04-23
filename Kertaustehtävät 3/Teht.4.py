import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

x1 = float(input("Anna pisteen 1 x: "))
y1 = float(input("Anna pisteen 1 y: "))

x2 = float(input("Anna pisteen 2 x: "))
y2 = float(input("Anna pisteen 2 y: "))

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

d = distance(p1, p2)

print("Etäisyys:", d)