#1. feladat:
f = open("tancrend.txt")
sorok = f.read().split("\n")[:-1]
f.close()
#print(sorok)


print("2. feladat:")
tancok = []
for i in range(0,len(sorok), 3):
    tancok.append(sorok[i : i + 3])

#print(tancok)

elso = tancok[0][0]
utolso = tancok[-1][0]
print("Az első bemutatott tánc " + elso + ", az utolsó pedig " + utolso + " volt.")


print("3. feladat:")
samba = sorok.count("samba")
print(str(samba) + " pár mutatta be a sambát.")


print("4. feladat:")
vilma = []
for e in tancok:
    if e[1] == "Vilma":
        vilma.append(e[0])
print("Vilma a " + ", ".join(vilma) + " táncokban szerepelt.")


print("5. feladat:")

print("6. feladat:")

print("7. feladat:")

        

        



    








