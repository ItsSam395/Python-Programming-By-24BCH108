Str=input("Enter a string : ")
cnt=0
for ch in Str:
    if ch.upper() in ['A','E','I','O','U']:
        cnt+=1

print("Number of vowels in string are : ",cnt)
