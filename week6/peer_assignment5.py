'''
Peer Assignment 5
Gene Rocha
1. Get a sentence from a user
2. Split the sentence to get an list of the words
3. Loop through the list of the words
4. Get the length of each word
5. Total the lengths of all the words
6. Divide the total lengths by number of words in the list
7. Print the average
Gene Rocha
10/29/19
'''
def main():
    print("This program returns the average numebr of words in a sentence")
    sentence = input("Enter a sentence:")
    words = sentence.split()
    totalLength = 0
    for w in words:
        totalLength += len(w)
    averageLength = totalLength/len(words)
    print("The avarage length of a word in the sentence is: {0:0.1f}".format(averageLength))
main()


