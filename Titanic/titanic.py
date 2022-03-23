#1. feladat:
f = open("titanic.txt")
adatok = f.read().split("\n")
f.close()


print("2. feladat: " + str(len(adatok)) + " db")


print("3. feladat: " + str(sum(int(e.split(";")[1]) + int(e.split(";")[2]) for e in adatok)) + " fő")
ossz = 0
for e in adatok:
    temp = e.split(";")
    tulelo = int(temp[1])
    eltunt = int(temp[2])
    ossz += tulelo
    ossz += eltunt
    

kulcsSzo = input("4. feladat: Kulcsszó: ")
van = False

#find()
for e in adatok:
    if e.find(kulcsSzo) >= 0:
        van = True
        break

if van:
    print("Van találat!")
else:
    print("Nincs találat!")

adatok2 = []
for e in adatok2:
    temp = e.split(";")
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    adatok2.append(temp)
print(adatok2)

talalat = [e for e in adatok if e.find(kulcsSzo) > -1]
#print(talalat)
if len(talalat):
    print("Van találat!")
else:
    print("Nincs találat!")


print("5. feladat:")














