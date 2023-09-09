class Student:

    schoolName = "JP"
    schoolCity = "Edison"

    def __init__(self, firstName, id):
        self.firsName = firstName
        self.id = id

    @classmethod
    def getSchool(cls):
        return cls.schoolName
    def getCity(cls):
        return cls.schoolCity

s1 = Student("Samarth", 3005485)
s2 = Student("Jimi", 12345)

print(Student.getSchool())
print(Student.getCity(Student))