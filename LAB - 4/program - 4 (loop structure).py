num = int(input("Enter a number: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
is_perfect = (sum_of_divisors == num)

sum_of_cubes = 0
temp = num
num_digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** num_digits
    temp //= 10
is_armstrong = (sum_of_cubes == num)

is_palindrome = str(num) == str(num)[::-1]

square = num **2
is_automorphic = str(square).endswith(str(num))

print(f"Is Prime: {is_prime}")
print(f"Is Perfect: {is_perfect}")
print(f"Is Armstrong: {is_armstrong}")
print(f"Is Palindrome: {is_palindrome}")
print(f"Is Automorphic: {is_automorphic}")
