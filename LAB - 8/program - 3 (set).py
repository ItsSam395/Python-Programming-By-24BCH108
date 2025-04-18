Set=set()

for i in range(1,6):
    name=input("Enter name : ")
    Set.add(name)

print("Set after adding names : ",Set)

remove_name,new_name=input("Enter the name to remove and the new name : ").split()

if remove_name in Set:
    Set.discard(remove_name)
    Set.add(new_name)

print("Set after modifying a name : ",Set)

remove_name1,remove_name2=input("Enter name to be Removed : ").split()
if remove_name1 or remove_name2 in Set:
    Set.discard(remove_name1)
    Set.discard(remove_name2)

print("Final set after deleting names : ",Set)
