employee_data = {
    101: [(1, 50000), (2, 60000), (3, 55000)],  
    102: [(4, 70000), (5, 80000)],              
    103: [(6, 45000), (7, 50000), (8, 48000)]   
}

depart_salary_stats = {}

for dept_no, employees in employee_data.items():
    salaries = [salary for roll_no, salary in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)
    depart_salary_stats[dept_no] = {
        'min_salary': min_salary,
        'max_salary': max_salary
    }

for dept_no, stats in depart_salary_stats.items():
    print(f"Department {dept_no}: Min Salary = {stats['min_salary']}, Max Salary = {stats['max_salary']}")
