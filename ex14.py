# string od usera
input_string = input("Enter a string: ")
# Iinicjalizacja liczników dla liter i cyfr
letter_count = 0
digit_count = 0
# Iteruj przez każdy znak w stringu
for char in input_string:
    if char.isalpha():  # czy litera
        letter_count += 1
    elif char.isdigit():  # czy cyfra
        digit_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)
