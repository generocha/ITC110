'''
Student Class
1. set the student name
2. set the id number
3. calculate a GPA
Gene Rocha
12/4/2019
'''
class Student():
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.grades = []

    def setStudentName(self):
        return self.student_name

    def setStudentID(self):
        return self.student_id

    def setGrade(self, grade_point):
        return self.grades.append(grade_point)

    #(GPAs are what is called "weighted averages." 
    # To calculate a GPA you get a weight by multiplying the 
    # grade by the credits. Then you divide the sum of the 
    # weights by the sum of the credits.)

    def calculateGPA(self):
        weight = 0
        total = 0
        self.gpa = 0
        if len(self.grades) != 0:
            for grade in self.grades:
                print(self.grade)
    
    def __str__(self):
        self.calculateGPA()
        return self.student_id

