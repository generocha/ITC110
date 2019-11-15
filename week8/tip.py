'''
This prgram will calculate the amount for a tip using a class with accesor and mutator methods 
1. create a class called tip
2. accesors methods to get the amount of the charge and tip
3. mutators methods to calculate the total tax rate and the total charge
4. method to return the tip amount and the tax amount and the total.
Gene Rocha 
11/14/20190
'''
class Tip:
    def __init__(self,charge,tip,tax):
        self.charge = float(charge)
        self.tip = float(tip)
        self.tax = float(tax)

    # accesor methods

    def getCharge(self):
        return self.charge

    def getTip(self):
        return self.tip
    
    def getTax(self):
        return self.tax

    # mutator methods

    # calculate the tip amount
    def setTip(self):
        tip = self.getTip() * self.getCharge()
        return tip
    # calculate the tax amount
    def setTax(self):
        tax = self.getCharge() * self.getTax()
        return tax
    # calculate the total
    def total(self):
        total = self.setTip() + self.setTax() + self.getCharge()
        return total
    # return the tip, tax, total and format
    def __repr__(self):
        return "The tip amount is ${0:.2f}, the tax is ${1:.2f} and the total is ${2:.2f}".format(self.setTip(), self.setTax(), self.total())

def main():
    c1 = Tip(35,.10,.10)
    print(c1)

main()