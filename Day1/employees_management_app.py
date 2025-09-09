employees=[] #list() array

employee = ('Banu', 22, 50000, True)
employees.append(employee)

employee=('Mahesh', 40, 40000, True)
employees.append(employee)

employee = ('Vaish', 22, 55000, True)
employees.append(employee)

print('After adding all employees', employees)



I=0
search='Vaish'
index=-1
for emp in employees:
    if emp[0]==search:
            index=I
            break
    I+=1





if index==-1:
      print('Employee not found')
else:
      search_employee=employees[index]
      print(employees[index])
      salary=float(input('Salary'))
      employee=(search_employee[0], search_employee[1], salary, search_employee[3])
      employees[index]=employee
print('After search and update', employees)

employee=('Dravid', 50, 200.75, True)
employees.append(employee)
print('After add Dravid:', employees)
employees.pop()
print('After delete Dravid:', employees)

#delete employee Mahesh by position
position =1
employees.pop(position)
print('After delete Mahesh:', employees)

    