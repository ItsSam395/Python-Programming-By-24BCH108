def power(a, b):
    
    if b == 0:
        return 1
    elif b > 0:
        return a * power(a, b - 1)
    else:
        return 1 / power(a, -b)

try:
    a = float(input("Enter the base (a): "))
    b = int(input("Enter the exponent (b): "))

    print(f"{a} raised to the power of {b} is: {power(a, b)}")
    
except ValueError:
    print("Invalid input. Please enter a valid number for the base and an integer for the exponent.")
