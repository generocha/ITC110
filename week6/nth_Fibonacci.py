'''
This program will return the nth Fibonacci number that the user submits
1. get the nth number from the input
2. Add a function Fibonacci that will create the Fibonacci sequence and return the nth number
3. Add a for loop the iterate through the numbers and return the nth number
4. return the result
Gene Rocha
10/31/19
'''
# Add the function getN to get the nth Fibonacci number from the input
def getN():
    n = int(input("Enter the nth Fibonacci number you would like to be returned:"))
    # return the nth Fibonacci number
    return n
# Add the function Fibonacci to calculate the Fibonacci sequence
def Fibonacci():
    # Invoke the function getN and add the input vale of n to the variable nth
    nth = getN()
    # n1 is the first number in the Fibonacci sequence 0(0 + 1 = 1)
    n1 = 0
    # n2 is the second number in the Fibonacci sequence 1
    n2 = 1
    # Add for loop range 1 - nth number from the input
    for i in range(1,nth):
        #print(n2) this would print the Fibonacci sequence up to the nth number
        # add the value of n1 to previousN1 before n1 is updated 
        previousN1 = n1
        # add the value of n2 to n1 before n2 is updated
        n1 = n2
        # n2 is now the sum the two pervious numbers
        n2 = previousN1 + n1
    # print the nth number
    print(n2)
    # return the result
    return Fibonacci
# Add the function main
def main():
    # invoke the function Fibonacci
    Fibonacci()
# invoke the function main
main()
