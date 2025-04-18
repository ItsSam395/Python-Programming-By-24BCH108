def reverse_list(num):
    if len(num) == 0:
        return []
    elif len(num) == 1:
        return num
    else:
        return [num[-1]] + reverse_list(num[:-1])

lst = input("Enter a list : ")
reversed_lst = reverse_list([int(x) for x in lst.split()])

print(f"Original list: {[int(x) for x in lst.split()]}")
print(f"Reversed list: {reversed_lst}")
