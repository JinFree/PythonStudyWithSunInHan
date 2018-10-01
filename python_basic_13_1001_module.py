import random
students = ['Tom', 'Sally', 'Betty', 'Eric', 'Angela', 'Stephany'] 
print(random.choice(students))
print(random.choice(students))
print(random.choice(students))

fruits = ['apple', 'banana', 'lemon']
my_fruit = random.sample(fruits, 2)
print(my_fruit)

my_int = random.randint(0, 10)
print(my_int)  # 0~10

import datetime
datetime.datetime.now()
print(datetime.datetime.now())