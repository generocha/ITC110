'''
Grade Class
1. get the class name
2. get the credits
3. get the grade points
Gene Rocha
12/5/2019
'''
# Class initiallization. 
# Pass in and set the values
class Grade():
    def __init__(self, class_name, class_credits, grade_point):
        self.class_name = class_name
        self.class_credits = class_credits
        self.grade_point = grade_point
    # get the class name
    def getClassName(self):
        return self.class_name
    # get the class credits
    def getCredits(self):
        return self.credits
    # get the grade points given for the class
    def getGradePoint(self):
        return self.grade_point
