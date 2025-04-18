lst=input("Enter Faculty Names : ").split()

long_lst=list(filter(lambda name: len(name) > 8,lst))

print("Names with more than 8 characters:",long_lst)
