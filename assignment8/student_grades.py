from grade import Grade
from student import Student

def main():
    student = Student("Sally Record", "1234")
    cont ='y'
    while cont == 'y':
        className = input("Enter the class name: ")
        credit = int(input("Enter the credits for the class: "))
        gradePoint = float(input("Enter the grade points for the class: "))
        grade = Grade(className,credit,gradePoint)
        cont = input("Do you want to add another class grade?: ")
    print(student)

main()