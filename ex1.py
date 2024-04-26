result = []
# Iteruj przez zakres od 1500 do 2700 (oba uwzględnione)
for num in range(1500, 2701):
    # Sprawdź, czy liczba jest podzielna przez 7 i jest wielokrotnością 5.
    if num % 7 == 0 and num % 5 == 0:
        result.append(num)
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:")
print(result)
