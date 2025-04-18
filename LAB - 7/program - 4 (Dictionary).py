def char_freq(input_str):
    freq_dict = {}
    
    for char in input_str:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
            
    return freq_dict

Str = input("Enter a string: ")

frequency = char_freq(Str)

print("Character frequency in the string:")
for char, cnt in frequency.items():
    print(f"'{char}': {cnt}")
