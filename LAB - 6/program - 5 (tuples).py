tpl = ((1, 2), (), (3, 4), (), (5,))
new_tpl=tuple(t for t in tpl if t)
print(new_tpl)
