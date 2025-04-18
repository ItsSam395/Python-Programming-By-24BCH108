def check_abs():
    num = float(input("Enter a number: "))
    if num < 0:
            absolute_value = -num
    else:
        absolute_value = num
    print(f"The absolute value of {num} is: {absolute_value}")
check_abs()
