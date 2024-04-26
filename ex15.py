import re
def validate_password(password):
    # Sprawdź, czy długość hasła wynosi od 6 do 16 znaków.
    if len(password) < 6 or len(password) > 16:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True

password = input("Enter password: ")

if validate_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
