szam = 100

if szam > 20:
    print("nagyobb")
    print("mint 20")
print("vizsg�lat v�ge")

if szam % 2 == 0:
    print("p�ros")
else:
    print("p�ratlan")

#bek�r�s j�n itten bizony
be=input("K�rek egy sz�mot: ")
print(be)

if be % 2 == 0:
    print("p�ros")
else:
    print("p�ratlan")

szam = int(input("K�rek m�g egy sz�mot: "))
if szam > 10:
    if  szam % 12 == 0:
        print(str(szam + "oszthat� 12-vel"))
    else:
        print(str(szam + "nem oszthat� 12-vel"))

ora=int(input("H�ny �ra van?"))
if ora <= 8:
    print("J� reggelt!")
elif ora <= 17:
    print("J� napot!")
elif ora <= 21:
    print("J� est�t!")
else:
    print("J� �jszak�t!")
