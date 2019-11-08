'''
This program will calculate how long it will take an investment to double
1. get the initial investment amount
2. get the interest rate
3. calculate the interest 
4. output the result
Gene Rocha
11/7/2019
'''
# get the initial investment amount 
def initialAmount():
    amount = int(input("Enter the amount of the initial investment: "))
    return amount
# get the interest rate
def interestRate():
    rate = int(input("Enter the interest rate: "))
    return rate
# calcaulate the interest and inkove the functions initialAmount and interestRate
def calculateInterest():
    years = 0
    amount = initialAmount()
    rate = interestRate()
    ratePercent = rate * .01
    double = amount * amount
    # until the amount is doubled add the yearly rate percent to the amount and increment the year
    while amount < double:
        amount = amount + (amount * ratePercent)
        years += 1
    return(years)
# invoke the function calculateInterest and return the result
def main():
    years = calculateInterest()
    print("The initial investment will take",years,"years to double")
main()