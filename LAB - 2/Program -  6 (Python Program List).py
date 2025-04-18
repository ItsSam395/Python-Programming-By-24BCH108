def dgt_cnt(num):
    cnt=0
    if num<0:
        num=-num
    if num==0:
        cnt=1
    else:
        while num>0:
            num//=10
            cnt+=1
    return cnt

val=int(input("Enter a number : "))
print(f"The number of digits in {val} is: {dgt_cnt(val)}")
