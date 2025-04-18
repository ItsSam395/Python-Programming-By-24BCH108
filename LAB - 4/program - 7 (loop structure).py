n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

numerator = 1
for i in range(1, n + 1):
    numerator *= i

denominator_r = 1
for i in range(1, r + 1):
    denominator_r *= i

denominator_n_r = 1
for i in range(1, n - r + 1):
    denominator_n_r *= i

nCr = numerator // (denominator_r * denominator_n_r)

nPr = numerator // denominator_n_r

print(f"nCr (Combinations) = {nCr}")
print(f"nPr (Permutations) = {nPr}")
