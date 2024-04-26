# Przyjęcie słowa ud usera
word = input("Enter a word: ")
# inicjalziacja miejsca na odwrócone słowo
reversed_word = ""
# Iteracja po znakach słowa w odwrotnej kolejności
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print("Reversed word:", reversed_word)
