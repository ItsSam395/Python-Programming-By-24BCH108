def prime_factors(n, divisor=2):
    if n == 1:
        return []
    
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

try:
    num = int(input("Enter a positive integer: "))
    if num>=0:
        factors = prime_factors(num)
        print(f"Prime factors of {num} are: {factors}")
    else:
        print("Invalid Input")
    
except ValueError as e:
    print(e)
    
