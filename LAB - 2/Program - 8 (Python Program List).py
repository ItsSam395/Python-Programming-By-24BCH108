def check_validity(x,y,z):
    if x+y+z==180:
        return True
    else:
        return False

ang1=float(input("Enter Angle1 : "))
ang2=float(input("Enter Angle2 : "))
ang3=float(input("Enter Angle3 : "))
if check_validity(ang1,ang2,ang3):
    print("Triangle is valid")
else:
    print("Triangle is not valid")
