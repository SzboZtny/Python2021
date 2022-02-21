f = open("adatok.txt")
f2 = open("adatoksorszam.txt", "w")

sorszam = 1
for egySor in f:
    f2.write(str(sorszam) + " " + egySor)
    sorszam += 1

f.close()
f2.close()
