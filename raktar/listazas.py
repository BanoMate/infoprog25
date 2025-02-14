def listazas():

    with open("raktar.txt", "r") as lista:
        for line in lista:
            print(line[:-1])