lst = [1,2,3,4,5,6,7,8,9,10,1,2,4,5,6,7,8,9,20,16]
pos = []

num = int(input("Enter a number to find its positions in the list: "))

for index, item in enumerate(lst):
    if item == num:
        pos.append(index + 1)

if pos:
    print(f"Occurrences of {num} in the list are at positions: {pos}")
else:
    print(f"The number {num} does not occur in the list.")
