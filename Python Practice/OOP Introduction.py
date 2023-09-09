class Computer:

    def add(self, a, b):
        return a + b

a = 2
b = 3
print("Outside " + str(a))

com1 = Computer()
com2 = Computer()
print(com1.add(a, b))