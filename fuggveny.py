"""
def negyzet(a):
    return a**2

q = negyzet(10)
print(q)
print(negyzet(8))

osszeg = 0
for i in range(10):
    osszeg += negyzet(i+1)

print(osszeg)

"""
import random

def koszon(nev="kedves barátom"):
    koszonesek = ("Jó napot kívánok","Szevasz","Hello","Csá","Szia")

    print(random.choice(koszonesek),nev)

koszonCount = 0
def koszon2(nev="kedves barátom"):
    koszonesek = ("Jó napot kívánok","Szevasz","Hello","Csá","Szia")

    print(koszonesek[koszonCount],nev)
    koszonCount += 1

koszon("Józsi")
koszon("Béla")
koszon("Juci")
koszon2()

koszon2("Elemér")
