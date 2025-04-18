#Delete an element of a tuple.

tpl = (1,2,3,4,5)

temp_lst = list(tpl)

temp_lst.remove(2)

new_tpl = tuple(temp_lst)

print(new_tpl)
