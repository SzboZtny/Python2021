import valasztasmodul

f = open("szavazatok.txt")
adatok = f.read().split("\n")[:-1]
f.close()

print("1. feladat:")
print(adatok)


print("2. feladat:")
szam = 0
for i in range(0, len(adatok)):
    adatok.count(valasztasmodul.val_adatok(keresztnev))
    szam += 1
    
print("A helyhatósági választáson {} képviselőjelölt indult.".format(szam))


print("3. feladat:")
jelolt = input("Adja meg egy jelölt vezetéknevét és utónevét: ")
print(jelolt)
if jelolt == valasztasmodul.val_adatok(vezeteknev, keresztnev):
    print(valasztasmodul.val_adatok(e[1]))
else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")


print("4. feladat:")


print("5. feladat:")
