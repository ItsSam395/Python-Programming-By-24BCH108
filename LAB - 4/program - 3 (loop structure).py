Str = input("Enter a string: ")

alphabet_cnt = 0
digit_cnt = 0

for char in Str:
    if char.isalpha():
        alphabet_cnt += 1
    elif char.isdigit():
        digit_cnt += 1

print(f"Number of alphabets: {alphabet_cnt}")
print(f"Number of digits: {digit_cnt}")
