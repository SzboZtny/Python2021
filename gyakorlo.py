print("1. feladat: Kisebb-nagyobb meghatározása")

#elso = int(input("Kérem az első számot: "))
#masodik = int(input("Kérem a második számot: "))

elso = ""
while elso == "":
    sz = input("Kérem az első számot: ")
    try:
        elso = int(sz)
    except:
        pass

masodik = ""
while masodik == "":
    sz_ = input("Kérem a második számot: ")
    try:
        masodik = int(sz_)
    except:
        pass

if elso > masodik:
    print("A nagyobb szám a(z) " + str(elso) + ", a kisebb a(z) " + str(masodik) + ".")
else:
    print("A nagyobb szám a(z) " + str(masodik) + ", a kisebb a(z) " + str(elso) + ".")
