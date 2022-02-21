#f = open("proba.txt", "w")
#f.write("Helló")
#f.close()

def file_kiír(file_nev):
    f = open(file_nev)

    print(f.read())
    f.close()

f = open("adatok.txt", "w")

be = "qwe"
while be != "":
    be = input("Kérek egy szöveget: ")
    if be != "":
        f.write(be + "\n")

f.close()

file_kiír("adatok.txt")
