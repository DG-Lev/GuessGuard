passwords = []
total_chars = 0
only_letters = 0
only_numbers = 0
uppercase = 0
lowercase = 0
has_number = 0
has_symbol = 0

with open ('rockyou-75.txt', encoding='latin-1') as f:
	for line in f:
		line = line.strip()
		total_chars += len(line)
		passwords.append(line)
		if line.isalpha():
			only_letters += 1
		if line.isdigit():
			only_numbers += 1
		if any(char.isupper() for char in line):
		    uppercase += 1
		if any(char.islower() for char in line):
		    lowercase += 1
		if any(not char.isalpha() and not char.isdigit() for char in line):
		    has_symbol += 1
		if any(char.isdigit() for char in line):
		    has_number += 1
	
average_length = round(total_chars / len(passwords), 2)

print ("Passwords:", len(passwords), "Average Length:", average_length, "Letters Only:", only_letters, "Numbers Only:", only_numbers, "Passwords have Uppercase:", uppercase, "Passwords have Lowercase:", lowercase, "Passwords have Number:", has_number, "Passwords have Symbol:", has_symbol)
