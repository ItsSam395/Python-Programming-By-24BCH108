def ispalindrome(s):
    cleaned_str = ''.join(s.split()).lower()
    
    return cleaned_str == cleaned_str[::-1]

test_str = [
    "abccba",
    "Was saw",
    "Hello World",
    "Meow woem"
]

for Str in test_str:
    if ispalindrome(Str):
        print(f'"{Str}" is a palindrome.')
    else:
        print(f'"{Str}" is not a palindrome.')
