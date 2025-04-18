def str_len(s):
    if s == "":
        return 0
    return 1 + str_len(s[1:])

Str=input("Enter a String : ")

print(f"The length of the string '{Str}' is: {str_len(Str)}")
