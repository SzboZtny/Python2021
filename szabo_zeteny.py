#Kérj be egy szót. Amíg ez a szó nem üres, addig rakd bele a szót a listába, és kérj be egy szót!

lista = []
szo = input("Kérek szavakat, szöveget: ")
print(szo)

while szo != "":
    lista.append(szo)
    szo = input("Kérek szavakat, szöveget: ")
    print(szo)

def forditas(lista):
    lista.reverse()
    print(lista)
    for i in lista:
        print(i)

forditas(lista)

 
def uppercase(szoveg):
    x = szo.title()
    return x

uppercase()

def elozo(kezdoelem, darabszam):
    lista2 = []
