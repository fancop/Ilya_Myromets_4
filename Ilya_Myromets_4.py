import os

name = input("как зовут персонажа? ")
if not name: name = "Илья Муромец"

way_1 = True
way_2 = True
way_3 = True
game = True
key = ""

while game:

    #камень
    if (way_1 or way_2 or way_3) and key == "":
        key = ""
        os.system("cls")
        print(f"{name} у камня")
        if way_1:
            print("1 вариант")
        if way_2:
            print("2 вариант")
        if way_3:
            print("3 вариант")
        user_choice = input("какой вариант? ")

        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            key += user_choice

    # 1 дорога
    if key == "1" and way_1:
        os.system("cls")
        print("дорога 1")
        print("1 вариант")
        print("2 вариант")
        user_choice = input("какой вариант")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    # 1 дорога 1 выбор
    if key == "11":
        os.system("cls")
        print("дорога 1 - хороший выбор")
        way_1 = False
        key = ""
        input("ENTER - дальше")

    # 1 дорога 2 выбор
    if key == "12":
        os.system("cls")
        print("дорога 1 - плохой выбор")
        game = False

    # 2 дорога
    if key == "2" and way_2:
        os.system("cls")
        print("дорога 2")
        print("1 вариант")
        print("2 вариант")
        user_choice = input("какой вариант")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    # 2 дорога 1 выбор
    if key == "21":
        os.system("cls")
        print("дорога 2 - хороший выбор")
        way_2 = False
        key = ""
        input("ENTER - дальше")

    # 2 дорога 2 выбор
    if key == "22":
        os.system("cls")
        print("дорога 2 - плохой выбор")
        game = False

    # 3 дорога
    if key == "3" and way_3:
        os.system("cls")
        print("дорога 3")
        print("1 вариант")
        print("2 вариант")
        user_choice = input("какой вариант")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    # 3 дорога 1 выбор
    if key == "31":
        os.system("cls")
        print("дорога 3 - хороший выбор")
        way_3 = False
        key = ""

    # 3 дорога 2 выбор
    if key == "32":
        os.system("cls")
        print("дорога 3 - плохой выбор")
        game = False

    if way_1 == way_2 == way_3 == False:
        print("ура мы победили")
        game = False

print("Конец")