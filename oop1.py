#Osztály definíció

class Kutya:
    #Konstruktor
    def __init__(self, nev):
        self.nev = nev
    #Osztály függvény
    def ugat(self):
        print("VAU-VAU(" + self.nev + ")")

#Példányosítás
egyKutya = Kutya("Armageddon")
print(egyKutya.nev)
egyKutya.ugat()

#Osztályváltozó értékadása
egyKutya.nev = "Bruno"
print(egyKutya.nev)

#Öröklés, leszármaztatás
class NemetJuhasz(Kutya):
    #Új függvény
    def pitiz(self):
        print(self.nev + ": Nein!")
    #Függvény felülírás
    def ugat(self):
        print("WAU-WAU")

n =  NemetJuhasz("Rex")
n.ugat()
n.pitiz()

n2 = NemetJuhasz("Kondér")
n2.pitiz()
