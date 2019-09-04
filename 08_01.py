#szubienica
import random

# stałe
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
---------
""",
"""
------
|    |
|    O
|
|
|
|
|
|
---------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
---------
""",
"""
------
|    |
|    O
|   -+-
|  / | \
|
|
|
|
---------
""",
"""
------
|    |
|    O
|   -+-
|  / | \
|    |
|
|
|
---------
""",
"""
------
|    |
|    O
|   -+-
|  / | \
|    |
|   | |
|
|
---------
""",
"""
------
|    |
|    O
|   -+-
|  / | \
|    |
|   | |
|   | |
|
---------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("KROWA", "MAŁPA", "SŁONECZNIK", "JANOSIK", "ALA")

#zmienne
word = random.choice(WORDS)

print("***", word, " ****")

so_far = "-" * len(word)

print("!! ", so_far, "!!")

wrong = 0

used = []
#***************************

print("Start")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("Twoje znaki: ", used)
    print("Twoje słowo: ", so_far)

    guess = input("\nPodaj literę: ")
    guess = guess.upper()

    while guess in used:
        print("Litera już była wykorzystana", guess)

        guess = input("\nPodaj literę: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("Tak, ", guess, "znajduje się w szukanym słowie.")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nNiestety,", guess, "nie występuje w szukanym słowie.")
        wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
    else:
        print("Udało się!")
