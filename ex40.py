def find_median(x, z, y):
    if x >= z:
        if z >= y:
            return z
        elif x <= y:
            return x
        else:
            return c
    elif x > y:
        return x
    elif z > y:
        return y
    else:
        return z
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
num3 = float(input("Input third number: "))

median = find_median(num1, num2, num3)

print("The median is", median)
