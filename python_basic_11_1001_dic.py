my_dict = {}  # {}
print(my_dict)
my_dict[1] = 'a'  # {1: 'a'}
print(my_dict)
my_dict['b'] = 2  # {1: 'a', 'b': 2}
print(my_dict)
my_dict['c'] = 'd'  # {1: 'a', 'b': 2, 'c': 'd'}
print(my_dict)

students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
for student in students.values():
    print(student)

students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
for key in students.keys():
    print(key)

students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
for key, val in students.items():
    print(key, val)