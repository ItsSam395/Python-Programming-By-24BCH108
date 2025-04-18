def frequency(input_str):
    freq_dict = {}

    for word in input_str.split():
        if word.lower() in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    sorted_freq = sorted(freq_dict.items())
    
    return sorted_freq

Str = "Virat is an Indian player and he is Worls's best batsman."
result = frequency(Str)

print("Word frequencies (sorted):")
for word, cnt in result:
    print(f"{word}: {cnt}")
