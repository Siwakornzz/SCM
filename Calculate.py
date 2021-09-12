class Calculate:

    def getid(self):
        return self.id

    def setmonthsell(self,monthsell):
        self.monthsell = monthsell

    def getmonthsell(self):
        return self.monthsell

    def setsalary(self,salary):
        self.salary = salary

    def getsalary(self):
        return self.salary

    def cal(self):
        if self.salary <= 10000:
            if self.monthsell >= 50001:
                total = self.monthsell * 0.10
            elif self.monthsell <= 50000:
                total = self.monthsell * 0.05
            else:
                total = 0
            total = self.salary + total
            
            return total
        else:
            if self.monthsell > 100000:
                total = self.monthsell * 0.10
            elif self.monthsell <= 100000:
                total = self.monthsell * 0.05
            else:
                total = 0
            total = self.salary + total
            
            return total
