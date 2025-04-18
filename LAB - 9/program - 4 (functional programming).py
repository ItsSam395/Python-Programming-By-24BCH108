lst=['madam','Python','malayalam',12321]

palin_lst=list(filter(lambda x: isinstance(x, str) and x == x[::-1], lst))

print("Palindrome strings :",palin_lst)
