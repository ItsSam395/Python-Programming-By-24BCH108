import pickle
from datetime import datetime

def serialize_employee(employee_data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee_data, file)
    print(f"Employee data serialized to {filename}")

def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        employee_data = pickle.load(file)
    return employee_data

employee_data = {
    'empcode': 101,
    'empname': 'Somya Srivastava',
    'date_of_joining': datetime(2025,4,18),
    'salary': 50000000
}

serialize_employee(employee_data, 'employee.dat')

deserialized_employee = deserialize_employee('employee.dat')
print("Deserialized Employee Data:", deserialized_employee)
    
