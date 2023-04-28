#property agency commission calculator

employees = []  #a list of the employees each employee
                #is a list inside this [name,ID,sales]
#example data
#[ ["paul", "123", 3]   ,   ["bob","432", 2]   ,    ["yosh","032", 5] ]

#input how many employees
while True:
    num_employees = input("How many employees are working this week: ")
    try:
        num_employees = int(num_employees)
        if num_employees >= 2 and num_employees <=5:
            print("Number of employees: " + str(num_employees))
            break
        else:
            print("Please enter a number 2-5")
    except:
        print("Please enter a valid number(2 - 5)")

#input employee data (in loop)
for i in range(0, num_employees):
    employee = [] #a list to store an employee

    #name
    while True:
        name = input("Employee name: ")
        if len(name) > 0:  #presence check
            employee.append(name) #add the name to the employee
            print("Name accepted: " + name)
            break  #continue
        else:
            print("Please Enter a valid name")

    #id
    while True:
        id = input("Employee id: ")
        if len(id) > 0:  #presence check
            employee.append(id) #add the name to the employee
            print("ID accepted: " + id)
            break  #continue
        else:
            print("Please Enter a valid id")

    #sales
    while True:
        sales = input("Employee sales: ")
        try:
            sales = int(sales)
            print("Sales made: " + str(sales))
            employee.append(sales) #add the name to the employee
            break
        except:
            print("Please Enter a valid number of sales")


    #add the employee to the list
    employees.append(employee)

#rank employees by sales
def myFunc(e):
  return e[2] 

employees.sort(reverse=True, key=myFunc)  #use the function to sort by sales

#output
print("------------Output Follows-------------")

#apply 15% bonus for the top seller
bonus = round(employees[0][2] * 500 *  0.15 , 2) #bouns of 15%

#print total commision to pay including bonus
print("Rank of Employees for this period:")

total_commission = 0
for i in range(0, num_employees):
    if i == 0:
        temp_commission = employees[i][2] * 500 + bonus
        print(str(i+1) + ") " + employees[i][0] + 
        "  ID:" + employees[i][1] + ", Commission: £" + 
        str(temp_commission) + " (Includes bonus of £" + str(bonus)+")")
    else:
        temp_commission = employees[i][2] * 500 
        print(str(i+1) + ") " + employees[i][0] +
        "  ID:" + employees[i][1] + ", Commission: £" + 
        str(temp_commission))
    total_commission += temp_commission


print("Total Commision to pay: £" + str(total_commission + bonus))

#suggestions for further improvements
#  Do you want to exit or run another calculation



        
        

