employees=[]    #[(id, name,age, salary, status, is_active)]

def create_employee(employee):
    global employees
    employees.append(employee)

def read_all_employee():
    return employees

def read_by_id(id):
    for employee in employees:
        if employee[0]==id:
            return employee
    return None

def update(id, new_employee):   #new_employee is update at id
    I=0
    for employee in employees:
        if employee[0]==id:
            employees[I]=new_employee
            break
        I+=1

def delete_employee(id):
    index=-1
    I=0
    for employee in employees:
        if employee[0]==id:
            index=I
            break
        I+=1
    if index!=-1:
        employees.pop(index)