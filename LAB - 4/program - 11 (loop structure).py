import math

deg = float(input("Enter the angle in degrees: "))

rad = deg * (math.pi / 180)

sin_x = 0
terms = 10  

for n in range(terms):
    term = ((-1) ** n) * (rad ** (2 * n + 1)) / math.factorial(2 * n + 1)
    sin_x += term

print(f"sin({deg} degrees) = {sin_x}")
