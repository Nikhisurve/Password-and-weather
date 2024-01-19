import re

def is_valid_password(password):
    # i have used regular expression pattern matching (positive assertion) syntax :(?= ... )
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_@$]).{8,}$')


    return bool(pattern.match(password))

password_to_check = input("Enter the password to check: ")
if is_valid_password(password_to_check):
    print("Password is valid.")
else:
    print("Password is invalid.")
