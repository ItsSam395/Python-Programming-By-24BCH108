def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

tot_marks, avg_marks = sum_avg(marks)

print(f"Total Marks: {tot_marks}")
print(f"Average Marks: {avg_marks:.2f}")
