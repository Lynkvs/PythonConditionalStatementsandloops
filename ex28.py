def print_pattern_U():
    for row in range(7):
        for col in range(5):
            if (col == 0 or col == 4) and row < 6 or row == 6 and (col > 0 and col < 4):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_pattern_U()
