'''
Peer Assignment 6
Calculate weekly wage with functions
1. Get hours worked
2. Get hourly wage
3. Calculate regular pay
4. Calculate overtime pay
5. Calculate weekly pay
6. Print result
Gene Rocha
11/5/2019
'''
REGHOURS = 40
# get the hours worked
def getHours():
    hours = int(input("Enter the hours worked for the week:"))
    return hours
# get the houlry wage
def getWage():
    wage = float(input("Enter the hourly wage:"))
    return wage
# calculate the reg pay
def calculateRegularPay(hours, wage):
    regularPay = 0
    if hours > REGHOURS:
        regPay = REGHOURS * wage
    else:
        regPay = hours * wage
    return regPay
# calculate overtime
def calculateOvertime(hours,wage):
    otPay = 0
    if hours > REGHOURS:
        otPay = wage * (hours - REGHOURS) * 1.5
    return otPay
# calculate weekly pay
def calculateWeeklyWage():
    h = getHours()
    w = getWage()
    reg = calculateRegularPay(h,w)
    ot = calculateOvertime(h,w)
    total = reg + ot
    printWages(reg,ot,total)
# print the result
def printWages(reg,ot,total):
    print("Your regular pay is ${0:0.2f}".format(reg))
    print("Your overtime pay is ${0:0.2f}".format(ot))
    print("Your weekly pay is ${0:0.2f}".format(total))
def main():
    calculateWeeklyWage()
main()
