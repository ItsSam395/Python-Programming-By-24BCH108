num=input("Enter 10 numbers between -15 and 15 : ")
lst=list(map(lambda x: int(x),num.split()))

new_lst=list(map(lambda x: x**2,lst))

print("Original List : ",lst)
print("Squares List:",new_lst)
