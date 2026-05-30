from zxcvbn import zxcvbn
import csv

dataset = []

with open ('rockyou-75.txt', encoding='latin-1') as f: 
    for line in f:
        uppercase_count = 0
        lowercase_count = 0
        digit_count = 0
        symbol_count = 0
        line = line.strip()
        if not line:
            continue
        result = zxcvbn(line)
        for char in line:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1
            else:
                symbol_count += 1
        password_length = len(line)
        dataset.append({
            "uppercase": uppercase_count,
            "lowercase": lowercase_count,
            "digits": digit_count,
            "symbols": symbol_count,
            "length": password_length,
            "label": result['guesses_log10']
        })

with open('dataset.csv', 'w', newline='') as csvfile:
    fieldnames = ['uppercase', 'lowercase', 'digits', 'symbols', 'length', 'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dataset)

print(dataset[0])