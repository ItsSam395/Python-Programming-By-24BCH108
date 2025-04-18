Str=input("Enter a string : ")
sub_str=input("Enter a sub string to be removed: ")
print()
if sub_str in Str:
    print("Original String : ",Str)
    print("Modified String : ",Str.replace(sub_str,""))
else:
    print(f"{Str} does not contain {sub_str}")
    
