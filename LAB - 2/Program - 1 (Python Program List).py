def check_val(x,y):
    if x>y:
        print(f"Largest Number : {x}")
        print(f"Smallest Number : {y}")
    else:
        print(f"Largest Number : {y}")
        print(f"Smallest Number : {x}")
        
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
check_val(num1,num2)
