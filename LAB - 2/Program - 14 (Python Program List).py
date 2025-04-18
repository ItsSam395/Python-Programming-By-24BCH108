phy_marks=float(input("Enter Physics Marks : "))
chem_marks=float(input("Enter Chemistry Marks : "))
math_marks=float(input("Enter Biology Marks : "))
total=(phy_marks+chem_marks+math_marks)
avg=total/3
print(f"Total Marks : {total}")
print(f"Average Marks : {avg}")
if avg>=80:
    print("Status : Pass")
    print("Grade : O")
elif avg>=70 and avg<79:
    print("Status : Pass")
    print("Grade : A+")
elif avg>=60 and avg<69:
    print("Status : Pass")
    print("Grade : A")
elif avg>=55 and avg<59:
    print("Status : Pass")
    print("Grade : B+")
elif avg>=50 and avg<54:
    print("Status : Pass")
    print("Grade : B")
elif avg>=45 and avg<49:
    print("Status : Pass")
    print("Grade : c")
elif avg>=40 and avg<44:
    print("Status : Pass")
    print("Grade : p")
else:
    print("Status : Fail")
    print("Grade : F")
