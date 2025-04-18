def convert(input_str):
    words = input_str.split()

    unique_words = set(words)

    sorted_words = sorted(unique_words)

    result_string = ' '.join(sorted_words)
    
    return result_string

Str = "virat msd rohit bumrah jadeja virat msd rohit bumrah"
result = convert(Str)

print("Original string:", Str)
print("Converted string:", result)
