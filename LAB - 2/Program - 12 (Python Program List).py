import math
def check_pos(x,y,z):
    h,k=float(x.split()[0]),float(x.split()[1])
    x1,y1=float(z.split()[0]),float(z.split()[1])
    dist=math.sqrt(math.pow((x1 - h),2) + math.pow((y1 - k),2))
    if dist<float(y):
        return "inside"
    elif dist==float(y):
        return "on"
    else:
        return "outside"
    
    

pos_center=input("Enter x and y coordinate of center of circle(x y) : ")
rad=input("Enter radius of circle : ")
pos_point=input("Enter x and y coordinate of the point(x y) : ")

print(f"The point ({pos_point.split()[0]}, {pos_point.split()[1]}) lies {check_pos(pos_center,rad,pos_point)} the circle.")

