uppercase_count = 0
lowercase_count = 0
digit_count = 0
symbol_count = 0
password_length = 0

password = input("Enter a password: ")

for char in password:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
password_length = len(password)

print("Uppercase:", uppercase_count, "Lowercase:", lowercase_count, "Digits:", digit_count, "Symbols:", symbol_count, "Length:", password_length)