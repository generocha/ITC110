'''
This program returns a letter grade for an exam score
1. create a list for A,B,C,D,F and combine the list
2. create the function get score and get the exam score from the input
3. create the function get grade and get the letter grade from the list
4. return the result
Gene Rocha
10/31/19
'''
# exam grades 90 -100: A, 80 - 89: B, 70 - 79: C, 60 - 69: D, < 60: F
# create list for A,B,C,D,F
A = ["A"] * 11
B = ["B"] * 10
C = ["C"] * 10
D = ["D"] * 10
F = ["F"] * 60
# combine the list
grades = F + D + C + B + A
# create the function getScore
def getScore():
    # prompt the user for the exam score
    score = (int(input("Enter your exam score: ")))
    # return the score
    return score
# create the function getGrade
def getGrade():
    # invoke the function getScore and get the score 
    score = getScore()
    # get the index of the score
    grade = grades[score]
    # return the grade
    return grade
# create the function main. This will return the result
def main():
    # invoke the function getGrade
    grade = getGrade()
    # return the result and print the letter grade for the exam
    print("Your letter grade for the CS exam is a",grade)
# invoke the function main
main()




