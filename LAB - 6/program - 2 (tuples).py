students=[(101,'Somya',20),(102,'Shikhar',21),(103,'Himanshu',22),(104,'Krishh',23),
          (105,'Vedant',20)]

roll_numbers = []
names = []
ages = []

for item in students:
    roll_no, name, age = item  
    roll_numbers.append(roll_no)
    names.append(name)             
    ages.append(age)               
    
print("Roll Numbers: ", roll_numbers)
print("Names: ", names)
print("Ages: ", ages)
