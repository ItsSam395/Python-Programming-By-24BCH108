def create_tuples_list(ending_val):
    lst = [(x, x**2, x**3) for x in range(1, ending_val + 1)]
    return lst

ending_val = int(input("Enter the ending value: "))
result = create_tuples_list(ending_val)
print(result)
