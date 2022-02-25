import random

#1. feladat
f = open("ajto.txt", "r")

kodok = []
for egySor in f:
    kodok.append(egySor[:-1])
    #kodok.append(egySor.strip())

f.close()

print(kodok)

#239451
#2. feladat
be = input("Adja meg, mi nyitja a zárat! ")

#3. feladat
sorszam = 1
talalat = []
for kod in kodok:
    if kod == be:
        talalat.append(sorszam)    
    sorszam += 1
    
#Számlista összefűzése
print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))

#A nyitó kódszámok sorai: 1 4 5 8 10…

#Kicsit más megoldás
talalat = []
for index,kod in enumerate(kodok, 1):
    if kod == be:
        talalat.append(index)
    
#Számlista összefűzése
print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))

#4. feladat
dupla = []
for index,kod in enumerate(kodok, 1):
    for karakter in kod:
        if kod.count(karakter) > 1:
            dupla.append(index)

if len(dupla) > 0:
    print(dupla[0])
else:
    print("Nem volt ismétlődő számjegy")

#5. feladat
ujkod = ""
valaszthato = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while len(ujkod) < len(be):
    szam = random.randint(0,len(valaszthato)-1)
    ujkod += valaszthato[szam]
    print(ujkod)
    valaszthato.pop(szam)

#5. feladat 2.0
print("Egy " + str(len(ujkod)) + " hosszú kódszám: " + ujkod)









        




















