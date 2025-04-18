Set = {"Akhbar", "Birble", "Charlie", "Ananya", "Somya", "Himanshu", "Anushka", "Ben10"}

a_names = set()
b_names = set()

for name in Set:
    if name.startswith('A'):
        a_names.add(name)
    elif name.startswith('B'):
        b_names.add(name)

print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
