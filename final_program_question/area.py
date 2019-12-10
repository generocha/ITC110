'''
Create a class called "area", that takes in two parameters 
"side1", and "side2". The measurements are in feet. 
Inside the class there is a function that calculates the total 
area by multiplying side1 and side2 There should be a function 
that returns the total area. There should be a __str__ function 
that returns "The total area is " + [area in square feet] (put your variable here). 
Call the class in the main function, and print the string. 
Gene Rocha
12/9/10
'''
class Area(): 
    # Class initiallization. Pass in
    # and set the values
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    # calculate the area
    def calculateArea(self):
        area = self.side1 * self.side2
        return area
    # return the total area
    def totalArea(self):
        total = self.calculateArea()
        return total
    # return a string with the total area in feet
    def __str__(self):
        return "The total area is {:0,} feet".format(int(self.totalArea()))
        
def main():
    total = Area(200,200)
    print(total)
main()