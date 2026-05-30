passwords = []
total_chars = 0
only_letters = 0
only_numbers = 0

with open ('rockyou-75.txt', encoding='latin-1') as f:
	for line in f:
		line = line.strip()
		total_chars += len(line)
		passwords.append(line)
		if line.isalpha():
			only_letters += 1
		if line.isdigit():
			only_numbers += 1
	
average_length = round(total_chars / len(passwords), 2)

print ("Passwords:", len(passwords), "Average Length", average_length, "Letters Only", only_letters, "Numbers Only", only_numbers)
