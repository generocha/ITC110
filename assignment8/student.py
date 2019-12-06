'''
Student Class
1. set the student name
2. set the id number
3. calculate a GPA
Gene Rocha
12/5/2019
'''
# Class initiallization. 
# Pass in and set the values
# add the an empty list for grades
class Student():
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.grades = []
    # set student name
    def setStudentName(self):
        return self.student_name
    # set student id
    def setStudentID(self):
        return self.student_id
    # set the grade point
    def setGrade(self, grade_point):
        return self.grades.append(grade_point) # append the grade point to the grades list

    #(GPAs are what is called "weighted averages." 
    # To calculate a GPA you get a weight by multiplying the 
    # grade by the credits. Then you divide the sum of the 
    # weights by the sum of the credits.)

    # method to calcute the gpa
    def calculateGPA(self):
        weight = 0 
        total = 0
        self.gpa = 0
        if len(self.grades) != 0:
            for g in self.grades:
                weight += g.grade_point * g.class_credits
                total += g.class_credits
            self.gpa = round(weight/total,2)
    # return the name, id and the gpa for the student
    def __str__(self):
        self.calculateGPA()
        return self.student_name + " " + self.student_id  + " " + str(self.gpa)

