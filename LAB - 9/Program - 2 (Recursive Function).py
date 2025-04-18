def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    return decimal_to_binary(n // 2) + str(n % 2)

try:
    num = int(input("Enter a positive integer: "))
    
    if num < 0:
        print("Invalid Input.")
    else:
        binary_representation = decimal_to_binary(num)
        print(f"Binary equivalent of {num} is: {binary_representation}")
except ValueError:
    print("Invalid Input. Please enter a valid integer.")
