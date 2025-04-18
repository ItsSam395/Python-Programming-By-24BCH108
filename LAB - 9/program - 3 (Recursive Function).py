def count_vowels(s):
    if len(s) == 0:
        return 0
    
    first_char = s[0].lower()
    if first_char in 'aeiou':
        return 1 + count_vowels(s[1:])  
    else:
        return count_vowels(s[1:]) 

Str = input("Enter a string : ")

print(f"The number of vowels in the string is: {count_vowels(Str)}")
