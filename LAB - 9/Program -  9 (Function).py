def count_alpha_digits(input_str):
    alpha_cnt = 0
    digit_cnt = 0
    result = {}

    for char in input_str:
        if char.isalpha():
            alpha_cnt += 1
        elif char.isdigit():
            digit_cnt += 1

    result = {
        'alphabets': alpha_cnt,
        'digits': digit_cnt
    }
    
    return result

Str = "Indian Cricket Team is world's No 1 Team."
result = count_alpha_digits(Str)

print("Input string:", Str)
print("Count of alphabets and digits:", result)
