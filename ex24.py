def print_pattern_P():
    for row in range(7):
        for col in range(5):
            if col == 0 or ((row == 0 or row == 3) and col < 4) or ((row == 1 or row == 2) and col == 4):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_pattern_P()
