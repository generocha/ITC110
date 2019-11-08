'''
This program will calculate a students class standing
1. get credits earned
2. calculate students classification 
3. return the results
Gene Rocha
11/7/2019
'''
# get the earned credits from the input and return
def getCredits():
    earnedCredits = int(input("Enter your total credits earned:"))
    return earnedCredits
# freshman < 7, sophomore >= 7, junior > 16, senior >= 26
# calculate the student classification and return
def classification():
    classLevel = ""
    # invoke the function getCredits
    earnedCredits = getCredits()
    if earnedCredits > 25:
        classLevel = "Senior"
    elif earnedCredits >= 7:
        if earnedCredits >= 16:
            classLevel = "Junior"
        else:
            classLevel = "Sophomore"
    else:
        classLevel = "Freshman"
    return classLevel
def main():
    # invoke the function classification
    classLevel = classification()
    print("Congrats your'e a",classLevel)
main()