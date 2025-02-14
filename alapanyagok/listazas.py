def listazas():

    with open("alapanyagok.txt", "r") as lista:
        for line in lista:
            print(line[:-1])