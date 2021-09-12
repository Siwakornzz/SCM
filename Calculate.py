class Calculate:

    def getid(self):
        return self.id

    def setmonthsell(self,monthsell):
        self.monthsell = monthsell

    def getmonthsell(self):
        return self.monthsell

    def cal(self):
        if self.monthsell >= 50001:
            total = self.monthsell * 0.10
        elif self.monthsell <= 50000:
            total = self.monthsell * 0.05
        else:
            total = 0
        total = self.salary + total
        
        return total
