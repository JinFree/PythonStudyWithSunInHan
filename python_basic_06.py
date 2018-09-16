numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:  # 2로 나눴을 때 1이 남으면 홀수입니다.
        odd_numbers.append(number)

print(odd_numbers)

odd_numbers = [number for number in numbers if number % 2 == 1]

print(odd_numbers)