# zadanie 2
# Kreator postaci

MAX_XP = 30

Str = 0
DEX = 0
INT = 0
LUC = 0

##############

print("Tworzenie postaci")

choice = ""
while choice != "0" and MAX_XP > 0:
    print("Pozostało punktów: ", MAX_XP)
    print("\nSiła: ", Str, ", Zręczność: ", DEX, ", Inteligencja: ", INT, ", Szczęście: ", LUC)

    print(
    """
    0 - Koniec
    1 - Siła
    2 - Zręczność
    3 - Inteligencja
    4 - Szczęście

    """
    )

    choice = input(">>> ")

    if choice == "0":
        print("Koniec")
    elif choice == "1":
        print("Siła!")
        print("""
            1 - dodaj
            2 - odejmij
        """)

        silaChoice = input(">> ")

        if silaChoice == "1":
            Str = Str + 1
            MAX_XP = MAX_XP - 1
        elif silaChoice == "2":
            Str = Str - 1
            MAX_XP = MAX_XP + 1
        else:
            print("Brak w menu")


    else:
        print("Wartość z poza dostępnej puli.")
