from felvetel import create_new
from szerkesztes import edit_data
from torles import delete_data

def create_main_menu():
    print("ADATKEZELŐ FELÜLET")
    print("Alapanyag felvétele: [1]")
    print("Alapanyag szerkesztése: [2]")
    print("Alapanyag törlése: [3]")

    val = input("Add meg az értéket: ")

    if val == "1":
        create_new()

    elif val == "2":
        edit_data()

    elif val == "3":
        delete_data()

    else:
        print("Hibás bemenet!")
        create_main_menu()

create_main_menu()

