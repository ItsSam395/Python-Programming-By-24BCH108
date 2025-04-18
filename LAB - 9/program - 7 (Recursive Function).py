def avg(num, index=0, total_sum=0, count=0):
    if len(num) == index:
        return total_sum / count if count > 0 else 0
    
    return avg(num, index + 1, total_sum + num[index], count + 1)

lst = [10, 20, 30, 40, 50] 

print(f"The average of the list {lst} is: {avg(lst)}")
