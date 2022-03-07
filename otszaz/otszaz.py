f = open("penztar.txt", "r")
kosar = []
#szoveg = f.read()
#print(szoveg)
for sor in f:
    kosar.append(sor.strip())

f.close()

print("A fizetések száma: " + str(kosar.count("F")))

print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárolt.")

sorszam = int(input("Vásárlás sorszáma: "))
arunev = input("Árucikk neve: ")
darab = int(input("Darabszám: "))

aruIndex = kosar.index(arunev)
darabLista = kosar[:aruIndex]
print(darabLista)
vasarlasDb = darabLista.count("F") + 1
print(vasarlasDb)

print("Az első vásárlás sorszáma: " + str(vasarlasDb))
