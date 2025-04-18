def check_rect():
    length=int(input("Enter length of rectangle : "))
    breadth=int(input("Enter breadth of rectangle : "))
    Area=length*breadth
    Perimeter=2*(length+breadth)
    if Area>Perimeter:
        print("Area is greater than the perimeter")
    else:
        print("Perimeter is greater than the area")

check_rect()
