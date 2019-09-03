scores = []

choice = None

while choice != "0":
    print("""
    Najlepsze wyniki

    0 - zakończ
    1 - wyświetl
    2 - dodaj
    """)

    choice = input("Wybierz: ")
    print()

    if choice == "0":
        print("koniec")
    elif choice == "1":
        print("Gracz\tWynik")
        for entry in scores:
            name, score = entry
            print(name, "\t", score)
    elif choice == "2":
        addName = input("Podaj name: ")
        addScore = int(input("Podaj wynik: "))
        entry = (addName, addScore)
        scores.append(entry)
        scores.sort(reverse=True)
    else:
        print("Wynik z poza menu")
        
