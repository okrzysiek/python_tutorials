scores = []

choice = None

while choice != "0":
    print("""
    Najlpesze wyniki

    0 - zakończ
    1 - pokaż wyniki
    2 - dodaj wyniki
    3 - usuń wyniki
    4 - posortuj wyniki
    """)

    choice = input("Wybierasz: ")
    print()

    
    if choice == "0":
        print("Do widzenia")
    elif choice == "1":
        print("Wyniki:")
        for score in scores:
            print(score)
    elif choice == "2":
        score = int(input("Dodaj wynik:"))
        scores.append(score)
    elif choice == "3":
        score = int(input("Który wynik usunąć:"))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "nie ma na liście wyników")
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("Wybór z poza dostępnej listy")
