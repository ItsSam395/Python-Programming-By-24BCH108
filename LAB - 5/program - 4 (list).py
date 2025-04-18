lst=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-11,-12,-13,-14,-15]
pos_lst=[]
neg_lst=[]

for item in lst:
    if item>=0:
        pos_lst.append(item)
    else:
        neg_lst.append(item)

print("Positive list : ",pos_lst)
print("Negative list : ",neg_lst)
