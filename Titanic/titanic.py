#1. feladat:
f = open("titanic.txt")
adatok = f.read().split("\n")
f.close()

print("2. feladat: " + str(len(adatok)) + " db")

print("3. feladat: " + str(sum(int(e.split(";")[1]) + int(e.split(";")[2]) for e in adatok)) + " fő")

for e in adatok:
    temp = e.split(";")
    tulelo = int(temp[1])
    eltunt = int(temp[2])
    ossz += tulelo
    ossz += eltunt

kulcsszo = input("4. feladat: Kulcsszó: ")
van = False
nincs = True
#find()









