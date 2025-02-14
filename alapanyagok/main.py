from felvetel import create_new
from szerkesztes import edit_data
from torles import delete_data
from listazas import listazas

def create_main_menu():
    print("ALAPANYAG KEZELŐ FELÜLET")
    print("Alapanyag felvétele: [1]")
    print("Alapanyag szerkesztése: [2]")
    print("Alapanyag törlése: [3]")
    print("Az alapanyagok listázásához: [4]")

    val = input("Add meg az értéket: ")

    if val == "1":
        create_new()

    elif val == "2":
        edit_data()

    elif val == "3":
        delete_data()

    elif val == "4":
        listazas()
        create_main_menu()

    else:
        print("Hibás bemenet!")
        create_main_menu()

create_main_menu()

