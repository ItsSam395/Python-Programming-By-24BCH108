def check_collinear(x,y,z):
    x1,y1=float(x.split()[0]),float(x.split()[1])
    x2,y2=float(y.split()[0]),float(y.split()[1])
    x3,y3=float(z.split()[0]),float(z.split()[1])
    
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if area == 0:
        return True
    else:
        return False

pos1=input("Enter x and y coordinate of first point(x1 y1) : ")
pos2=input("Enter x and y coordinate of second point(x2 y2) : ")
pos3=input("Enter x and y coordinate of Third point(x3 y3) : ")

if check_collinear(pos1,pos2,pos3):
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")
