my_tuple = (1, 2, 3)
print(type(my_tuple))
print(my_tuple)
my_tuple = 4,5,6
print( type(my_tuple))
print(my_tuple)

my_tuple = (1, 2, 3)
num1, num2, num3 = my_tuple
print(num1)
print(num2)

num1 = 1
num2 = 2
num1, num2 = num2, num1
print(num1)
print(num2)

animals = ['땅다람쥐', '바다코끼리', '스컹크', '아나콘다', '코알라', '하이에나', '바다소']
for animal in animals:
    print(animal)

for num in [1, 2, 3]:
    print(num)

for ch in '김왼손':
    print(ch)

for n in range(3):
    print(n)

for n in range(4, 6):
    print(n)

for i in range(1, 10):
    print('{}x{}={}'.format(2, i, 2 * 1))

for j in range(2, 10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j, i, j * i))