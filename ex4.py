# górna część wzoru
for i in range(1, 6):  # Liczba wierszy dla górnej części
    for j in range(i):
        print("*", end=" ")
    print()
# dolna część
for i in range(4, 0, -1):  # Liczba wierszy dla dolnej części
    for j in range(i):
        print("*", end=" ")
    print()
