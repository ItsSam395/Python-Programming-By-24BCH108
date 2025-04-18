phy_marks=float(input("Enter Physics Marks : "))
chem_marks=float(input("Enter Chemistry Marks : "))
bio_marks=float(input("Enter Biology Marks : "))
avg=(phy_marks+chem_marks+bio_marks)/3
print(f"Average Marks : {avg}")
if avg>=80:
    print(f"Grade : Distinction")
elif avg>=60 and avg<80:
    print(f"Grade : First Division")
elif avg>=45 and avg<60:
    print(f"Grade : Second Division")
elif avg>=40 and avg<45:
    print(f"Grade : Pass")
else:
    print(f"Grade : Promotion not granted")


