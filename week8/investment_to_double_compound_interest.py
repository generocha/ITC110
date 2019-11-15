'''
This program will calculate the time an investment will take to double with compound interest
1. get the initial investment amount
2. get the interest rate
3. calculate the interest per year
4. output the result
Gene Rocha
11/14/2019
'''
#The formula for compound interest, including principal sum, is:
# A = P (1 + r/n) (nt)
class Double:
    def __init__(self,investment,intrest):
        self.investment = float(investment)
        self.intrest = float(intrest)

    # accesor methods

    def getInvestment(self):
        return self.investment
    
    def getIntrestRate(self):
        return self.intrest

    # mutator methods
    def setCompound(self):
        investment = self.getInvestment()
        rate = self.getIntrestRate()
        years = 0
        total = 0
        while total < investment * 2:
            total = investment * (1 + rate)** years
            years = years + 1
        return years

    def __repr__(self):
        return "The initial investment will take {0} years to double".format(self.setCompound())
def main():
    I1 = Double(1000.00,.05)
    print(I1)
main()



