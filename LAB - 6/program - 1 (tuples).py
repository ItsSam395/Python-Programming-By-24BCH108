names_list = [('Somya',),('Shikhar',),('Himanshu',), 'Alia', 'Kriti', ('Krishh',), 'Kajol']

boys_cnt = 0
girls_cnt = 0

for item in names_list:
    if isinstance(item,tuple):
        boys_cnt += 1
    elif isinstance(item,str):
        girls_cnt += 1


print("Number of boys: ", boys_cnt)
print("Number of girls: ", girls_cnt)
