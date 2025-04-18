def is_dict_empty(d):
    return len(d) == 0

dict1 = {}
dict2 = {'a': 1, 'b': 2}

dicts = [dict1, dict2]

for i in range(len(dicts)):
    if is_dict_empty(dicts[i]):
        print(f"dict{i + 1} is empty.")
    else:
        print(f"dict{i + 1} is not empty.")
