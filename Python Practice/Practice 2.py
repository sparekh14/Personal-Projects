class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print()

person1 = Person("Samarth", 15)
person2 = Person("Jimi", 43)

person1.print()
person2.print()

if person1.age != person2.age:
    print("Not the same age")