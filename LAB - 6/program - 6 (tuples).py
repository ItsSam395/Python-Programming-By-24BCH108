#Modify an element of a tuple.

tpl = (1,2,3,4)

temp_lst = list(tpl)
temp_lst[1] = 5

new_tpl = tuple(temp_lst)

print(new_tpl)
