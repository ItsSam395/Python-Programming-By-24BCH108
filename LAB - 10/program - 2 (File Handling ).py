stud_dict = {}

with open('student.csv', 'r') as file:
    header = file.readline().strip().split(',')
    for line in file:
        values = line.strip().split(',')
        roll_no = int(values[0])
        name = values[1]
        marks_1 = int(values[2])
        marks_2 = int(values[3])
        marks_3 = int(values[4])
        
        tot_marks=marks_1 + marks_2 + marks_3
        
        stud_dict[roll_no] = {
            'Name': name,
            'Marks': {
                'Marks 1': marks_1,
                'Marks 2': marks_2,
                'Marks 3': marks_3,
            },
            'Total': tot_marks
        }
        
for roll_no, details in stud_dict.items():
    print(f"Roll No: {roll_no}, Details: {details}")

    
