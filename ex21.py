def print_pattern_L():
    for row in range(7):
        for col in range(5):
            if col == 0 or row == 6:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_pattern_L()
