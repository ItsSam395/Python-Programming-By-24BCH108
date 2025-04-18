def convert_lower(Str):
    str_lower=""
    for ch in Str:
        if 'A'<=ch<='Z':
            str_lower+=chr(ord(ch)+32)
        else:
            str_lower+=ch
    return str_lower

def convert_upper(Str):
    str_upper=""
    for ch in Str:
        if 'a'<=ch<='z':
            str_upper+=chr(ord(ch)-32)
        else:
            str_upper+=ch
    return str_upper

def convert_toggle(Str):
    str_toggle=""
    for ch in Str:
        if 'A'<=ch<='Z':
            str_toggle+=chr(ord(ch)+32)
        elif 'a'<=ch<='z':
            str_toggle+=chr(ord(ch)-32)
        else:
            str_toggle+=ch
    return str_toggle

str_org=input("Enter a string : ")
print()
print("Original String : ",str_org)
print("Lowercase String : ",convert_lower(str_org))
print("Uppercase String : ",convert_upper(str_org))
print("Togglecase String : ",convert_toggle(str_org))
