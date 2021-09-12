from Employee import Employee
from Calculate import Calculate
class Show(Employee,Calculate):

    def tostring(self):
        print("ID : " , self.getid())
        print('Name : ' , self.getname())
        print('Salary : ' , self.getsalary())
        print('total : ', self.cal())