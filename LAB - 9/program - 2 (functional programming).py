lst1 = [1,2,3,4,5,6]
lst2 = [6,5,4,3,2,1]

res_lst = list(map(lambda x,y : x + y, lst1,lst2))

print("Resulting list after adding corresponding elements of both the list : ")
print(res_lst)
