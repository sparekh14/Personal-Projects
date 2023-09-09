class Student_Info:
    def name(self, last, first):
        print(last + ", " + first)
    def dob(self, month, date, year):
        print(month + "/" + date + "/" + year)
    def grade_section(self, grade, section):
        print(grade + "-" + section)
    def state_id(self, st_id):
        print(st_id)
    def school_id(self, sc_id):
        print(sc_id)

student = Student_Info()

num_students = int(input("For how many students are you entering data: "))

for i in range(num_students):
    last = input("Enter your last name: ")
    first = input("Enter your first name: ")
    month = input("Enter your DOB month: ")
    date = input("Enter your DOB date: ")
    year = input("Enter your DOB year: ")
    grade = input("Enter your grade: ")
    section = input("Enter your section: ")
    stateID = input("Enter your state ID: ")
    schoolID = input("Enter your school ID: ")

    print("\n\nStudent Information")
    print("```````````````````\n")

    print("Name: ", end="")
    student.name(last, first)
    print("Date of Birth: ", end="")
    student.dob(month, date, year)
    print("Grade-Section: ", end="")
    student.grade_section(grade, section)
    print("State ID Number: ", end="")
    student.state_id(stateID)
    print("School ID Number: ", end="")
    student.school_id(schoolID)
    print("\n\n")