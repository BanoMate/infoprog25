def edit_data():
    cikkszam = input("Alapanyag szerkesztéséhez add meg a cikkszámot: ")

    with open("alapanyagok.txt", "r") as lista:
        for line in lista:
            sor = line.split(";")
            if cikkszam == sor[0]:
                mertekegyseg = sor[2]
                nev = sor[1]
                ar = sor[3]

    ujnev = input("Add meg az új nevet ["+ nev.strip() + "]: ")
    ujmertekegyseg = input("Add meg az új mértékegységet ["+ mertekegyseg.strip() + "]: ")
    ujar = input("Add meg az új árat ["+ ar.strip() + "]: ")

    ujadatok = [ujnev, ujmertekegyseg, ujar]

    with open('alapanyagok.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        sor = line.strip().split(';')

        if sor[0] == cikkszam:
            sor[1:] = ujadatok
            lines[i] = '; '.join(sor) + ';\n'

    with open('alapanyagok.txt', 'w') as file:
        file.writelines(lines)