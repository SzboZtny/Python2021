#Standard placeholder
f1 = "Ide jön a szám: {}"

print(f1.format(2))
print(f1.format("kettő"))

szam = input("Kérek egy számot: ")
print(f1.format(szam))

#Sorszámozott placeholder
f2 = "Ide is jön valami {1}, ide meg már {0}."
print(f2.format(123, 321))

f3 = "My name is {surname}, {firstname} {surname}."
print(f3.format(firstname = "James", surname = "Bond"))

f4 = "Az én nevem {surname}, {surname} {firstname}."
print(f4.format(firstname = "James", surname = "Bond"))
print(f4.format(firstname = "Jakab", surname = "Kötés"))
