def compute(n):
    
    nn = n ** 2
    nnn = n ** 3
    nnnn = n ** 4
    
    result = n + nn + nnn + nnnn
    return result

for digit in range(4, 8):
    result = compute(digit)
    print(f"The result for n = {digit} is: {result}")
