def student_info(name, **info):
    print("Name: " + name)
    for i, j in info.items():
        print(str(i) + ': ' + str(j) + '\n\n')


student_info('Samarth', ID = 3005485, Section = '9-22')


a = 10
print(id(a))
def something():
    a = 5
    x = globals()['a']
    print(id(x), x)
    print('inside', a)
    globals()['a'] = 15
    print(id(a))
something()
print("\n\n\n", a)