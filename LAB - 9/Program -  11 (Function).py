def create_list(lst1, lst2):
    intersection = list(set(lst1) & set(lst2))
    return intersection

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

print("Intersection of the two lists:", create_list(lst1, lst2))
