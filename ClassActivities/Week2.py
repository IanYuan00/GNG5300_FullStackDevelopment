'''
#Nested if statement
num = float(input("Enter a number:"))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
'''

#Functions: add student names; add grades for a existing student; print all grades for a student
student_grades = {}
#Add student names
def add_student(name):
    if name in student_grades:
        print("Student already exists")
    else:
        student_grades[name] = []
        print("Name added successfully")

#Add grades for a existing student
def add_grades(name, grade):
    if name in student_grades:
        student_grades[name].append(grade)
        print("Grade added successfully")
    else:
        print("Student not found")

#Print all grades for a student
def print_grades(name):
    if name in student_grades:
        print(f"The grade for {name} is: {student_grades[name]}")
    else:
        print("Student not found")

def main():
    while True:
        action = input("Do you want to add a student or add a grade or print grades for a student or exit? :").strip().lower()
        if action == "add a student":
            name = input("Enter the student name:").strip()
            add_student(name)
        elif action == "add a grade":
            name = input("Enter the student name:").strip()
            grade = float(input("Enter the grade:"))
            add_grades(name, grade)
        elif action == "print grades":
            name = input("Enter the student name:").strip()
            print_grades(name)
        elif action == "exit":
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()


#Demonstrate the difference between local and global variables in Python
# Global variable
global_var = 10

def my_function():
    # Local variable
    local_var = 5
    print("Local variable:", local_var)
    print("Global variable:", global_var)

my_function()
print("Global variable outside function:", global_var)



class StudentGrades:
    def __init__(self):
        self.student_grades = {}

    def add_student(self, name):
        if name in self.student_grades:
            print("Student already exists")
        else:
            self.student_grades[name] = []
            print("Name added successfully")

    def add_grades(self, name, grade):
        if name in self.student_grades:
            self.student_grades[name].append(grade)
            print("Grade added successfully")
        else:
            print("Student not found")

    def print_grades(self, name):
        if name in self.student_grades:
            print(f"The grade for {name} is: {self.student_grades[name]}")
        else:
            print("Student not found")

    def main(self):
        while True:
            action = input("Do you want to add a student or add a grade or print grades for a student or exit? :").strip().lower()
            if action == "add a student":
                name = input("Enter the student name:").strip()
                self.add_student(name)
            elif action == "add a grade":
                name = input("Enter the student name:").strip()
                grade = float(input("Enter the grade:"))
                self.add_grades(name, grade)
            elif action == "print grades":
                name = input("Enter the student name:").strip()
                self.print_grades(name)
            elif action == "exit":
                break
            else:
                print("Invalid action")

if __name__ == "__main__":
    student_grades = StudentGrades()
    student_grades.main()