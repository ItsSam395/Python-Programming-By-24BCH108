Set={15, 20, 25, 30, 35, 40, 45, 18, 22, 29}

print("Original Set:",Set)

cnt = sum(1 for num in Set if num < 30)
print("Count of numbers less than 30:", cnt)

new_set={num for num in Set if num <= 35}

print("Modified set : ", new_set)
