from Show import Show

name = input("Enter Ur name : ")
id = int(input("Enter Ur ID : "))
salary = int(input("Enter Ur Salary : "))
s = Show(id,name,salary)
monthsell = int(input("Enter Ur Monthsell : "))
s.setmonthsell(monthsell)

s.tostring()