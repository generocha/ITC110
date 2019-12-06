# import the grade and student classes
from grade import Grade
from student import Student
# add the student name and id
def main():
    student = Student("Sally Record", "1234")
    cont ='y'
    while cont == 'y':
        # get the name, credit and grade point given for the class
        className = input("Enter the class name: ")
        credit = int(input("Enter the credits for the class: "))
        gradePoint = float(input("Enter the grade points for the class: "))
        # pass the name, credit and grade point given for the class to the Grade class
        grade = Grade(className,credit,gradePoint)
        # pass grade info to the student setter
        student.setGrade(grade)
        cont = input("Do you want to add another class grade?: ")
        cont = cont.lower()
    print(student)

main()