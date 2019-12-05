'''
Grade Class
1. get the class name
2. get the credits
3. get the grade points
Gene Rocha
12/4/2019
'''
class Grade():
    def __init__(self, class_name, class_credits, grade_point):
        self.class_name = class_name
        self.class_credits = class_credits
        self.grade_point = grade_point

    def getClassName(self):
        return self.class_name

    def getCredits(self):
        return self.credits

    def getGradePoint(self):
        return self.grade_point
