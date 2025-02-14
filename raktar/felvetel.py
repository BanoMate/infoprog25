import re

def create_new():
    cikkszamok = set([])

    with open("../alapanyagok/alapanyagok.txt", "r") as lista:
        for line in lista:
            sor = line.split(";")
            cikkszamok.add(sor[0])


    cikkszam = input("A termék felvételéhez add meg a cikkszámot: ")
    if cikkszam not in cikkszamok:
        print('Nem létezik ilyen számú termék!')
        return

    with open("../alapanyagok/alapanyagok.txt", "r") as lista:
        for line in lista:
            sor = line.split(";")
            if cikkszam == sor[0]:
                mertekegyseg = sor[2]
                nev = sor[1]

    mennyiseg = input("Add meg a(z)" + nev + " mennyiségét: ")

    if mennyiseg.isdigit():
        pass
    else:
        return

    with open("raktar.txt", "a") as lista:
        lista.write(nev.strip())
        lista.write("; ")
        lista.write(mennyiseg)
        lista.write("; ")
        lista.write(mertekegyseg.strip())
        lista.write(";\n")