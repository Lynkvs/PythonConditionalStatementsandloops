def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temperatures = [(60, 'Celsius'), (45, 'Fahrenheit')]
for temp, unit in temperatures:
    if unit.lower() == 'celsius':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp} in Fahrenheit")
    elif unit.lower() == 'fahrenheit':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted_temp} in Celsius")
    else:
        print("Invalid unit specified.")
