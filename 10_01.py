# program kółko i krzyżyk
import random

# definicje Stałych
# komputer
# gracz
zaczyna = ["Gracz", "Komputer"]

plansza = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

def instructions():
    """Wyświetl instrukcję gry"""
    print("""
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """)

def losowanie_kolejnosci():
    """Kto zaczyna grę"""
    wybor = random.randrange(0, 2)
    print("Grę zaczyna ", zaczyna[wybor])
    return wybor

def pokaz_plansze():
    """Wyświetl plansze"""
    print(plansza[0] ," | ", plansza[1], " | ", plansza[2])
    print("-------------")
    print(plansza[3] ," | ", plansza[4], " | ", plansza[5])
    print("-------------")
    print(plansza[6] ," | ", plansza[7], " | ", plansza[8])

def strzal(kto, gdzie):
    if kto == "O":
        plansza[gdzie] = "O"
    elif kto == "X":
        plansza[gdzie] = "X"

def main():
    """Funkcja main"""


    pokaz_plansze()

    pifpaf = int(input("Strzał: "))
    strzal("O", pifpaf)

    pifpaf = int(input("Strzał: "))
    strzal("X", pifpaf)

    pokaz_plansze()


    

main()
