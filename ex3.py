import random

# generowanie liczby z zakresu 1 do 9
random_number = random.randint(1, 9)
while True:
    # zapytanie usera o liczbe
    guess = int(input("Guess a number between 1 and 9: "))
    # sprawdz poprawność
    if guess == random_number:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again.")
