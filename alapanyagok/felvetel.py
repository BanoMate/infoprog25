import re

def create_new():
    cikkszamok = set([])

    with open("alapanyagok.txt", "r") as lista:
        for line in lista:
            sor = line.split(";")
            cikkszamok.add(sor[0])


    cikkszam = input("Alapanyag felvételéhez add meg a cikkszámot: ")
    if cikkszam in cikkszamok:
        print('Már van ilyen számú termék')
        return

    if not bool(re.match(r'^[A-Za-z0-9]{6}$', cikkszam)):
        print('Hibás szám')
        return

    nev = input("Add meg a termék nevét: ")

    mertekegyseg = input("Add meg a termék mértékegységét: ")

    ar = input("Add meg a termék árát: ")

    with open("alapanyagok.txt", "a") as lista:
        lista.write(cikkszam)
        lista.write("; ")
        lista.write(nev)
        lista.write("; ")
        lista.write(mertekegyseg)
        lista.write("; ")
        lista.write(ar)
        lista.write(";\n")