'''
This program will square each number in a list
1. Add a list of numbers
2. Add a function square
3. Add a for loop that will iterate through each number in the list and and the result to the variable squareNumbers
4. Print the square of each number in the for loop
5. Return the variable squareNumbers
6. Add a function Main and invoke the function square with one parameter the nums list
7. Invoke the function Main
Gene Rocha
10/31/19
'''
# nums list
nums = [1,2,3,4]
# function square with one parameter
def square(numbers):
    # for loop to iterate through each number in the nums list
    for i in nums:
        # add the result to the variable squareNumbers
        squareNumbers = i ** 2
        # print the variable squareNumbers
        print(squareNumbers)
    # return the variable squareNumbers
    return squareNumbers
# add the function main
def main():
    # invoke the function square with one parameter the nums list
    square(nums)
# invoke the function main
main()
