def check(lst):
    less_than = 0
    greater_than = 0
    equal_to = 0
    for i in lst:
        if i > 5:
            greater_than += 1
        elif i == 5:
            equal_to += 1
        else:
            less_than += 1
    return less_than, greater_than, equal_to

lst = []

for i in range(5):
    x = int(input("Enter a value: "))
    lst.append(x)

less_than, greater_than, equal_to = check(lst)
print("Less than 5: ", less_than)
print("Greater than 5: ", greater_than)
print("Equal to 5: ", equal_to)