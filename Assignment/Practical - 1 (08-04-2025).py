f1=open("Myname.txt")
cnt=0
for line in f1.readlines():
    for word in line.split():
        if word.upper()=="SOMYA":
            cnt+=1
        else:
            pass
print("Occurance of My Name(Somya) is : ",cnt)
