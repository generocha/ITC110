'''
This program creates a simple guessing game
The program genrate a random number between 1 -1000
and the user has 10 chances to guess the correct number
The program will let the user know if its too high or too low
The user starts out with 10 trys and looses 1 point for an incorrect guess
At the end of the game the user is asked if they would like to play again. If so, 
the game will restart and if not, the program will print out the average score and quit the game
1. Generate a random number
2. Loop 10 times
    a. get the users guess
    b. determine if the guess is too high or too low
    c. increment or decrement the score based on the guess
3. Display the user score
4. Add the score to the list of scores
5. Ask the user if they would like to play again
    a. If so, start a new game
    b. If no, print the average score and end the game
Gene Rocha
11/21/2019
'''
from random import randrange
# Introduction
def intro():
    print("---------------------------------------")
    print("This program is a simple guessing game.")
    print("The program will generate a random number between 1 - 1000")
    print("You will get 10 guesses and the game will tell you if you")
    print("are too high,too low, or correct. Each time you play you get")
    print("10 points. Each wrong guess 1 point is substracted.")
    print("---------------------------------------")
# 
def getRandom():
    number = randrange(1,1001)
    return number
def getUserGuess():
    guess = int(input("Enter a guess between 1 - 1000: "))
    return guess
# 
def evulateGuess(number, guess,score):
    state = 0
    if guess > number:
        print("Guess is too high. You have", score -1, "more guesses")
    elif guess < number:
        print("Guess is too low. You have", score -1, "more guesses")
    else:
        print("Congratulations, you got it!")
        state = 1
        return state
def play():
    number = getRandom()
    score = 10
    for i in range(1,11):
        guess = getUserGuess()
        state = evulateGuess(number,guess,score)
        if state == 1:
            break
        score = score -1
    return score,number
def game():
    choice = 'y'
    scores = []
    while choice =='y':
        score = play()
        print ("Your score is",score[0], "The number was",score[1])
        scores.append(score[0])
        choice = input("Do you want to play another game? y to continue: ")
        choice.lower()
    return scores
def getAverageScores(scores):
    total = 0
    for item in scores:
        total += item
    average = total/len(scores)
    return average
def printAverave(average):
    print("Your average score was", average)
def main():
    intro()
    scores = game()
    average = getAverageScores(scores)
    printAverave(average)
main()