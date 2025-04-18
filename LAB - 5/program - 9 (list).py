list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

list3 = [num for num in list1 if num not in list2]

print("First List: ", list1)
print("Second List: ", list2)
print("Third List (numbers in first list not in second list): ", list3)
