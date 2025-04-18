def check_val(x,y,z):
    largest = x
    smallest = x

    if y > largest:
        largest = y
    if z > largest:
        largest = z

    if y < smallest:
        smallest = y
    if z < smallest:
        smallest = z

    return largest, smallest

num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
num3=int(input("Enter num3 : "))
Max,Min=check_val(num1,num2,num3)
print(f"Largest Number : {Max}")
print(f"Smallest Number : {Min}")
