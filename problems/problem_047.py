# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char == "$" or char == "!" or char == "@":
            has_special_char = True

    if has_special_char and has_digit and has_lower and has_upper:
        return True
    else:
        return False
