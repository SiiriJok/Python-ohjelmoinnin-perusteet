
luku = int(input("Anna luku: "))

if luku < 2:
    print("Ei ole alkuluku")
else:
    for i in range(2, luku):
        if luku % i == 0:
            print("Ei ole alkuluku")
            break
    else:
        print("Luku on alkuluku")