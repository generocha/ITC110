'''
This program will output the gas mileage for a car based on the miles traveled and total gas used
Gene Rocha
11/6/2019
'''
def totalMiles():
    miles = float(input("Enter the total miles traveled:"))
    return miles
def totalGas():
    gas = float(input("Enter the total amount of gallons of gas used:"))
    return gas
def calcauteGasMileage():
    miles = totalMiles()
    gas = totalGas()
    gasMileage = float(miles/gas)
    return gasMileage
def main():
    gasMileage = calcauteGasMileage()
    print("Your gas mileage for this trip is",round(gasMileage,2), "miles per gallon")
main()