count = 0
with open ('rockyou-75.txt', encoding='latin-1') as f:
	for line in f:
		print(line)
		count += 1
		if count == 10:
			break
