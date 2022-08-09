from functools import reduce


numbers = [
    int(input()),
    int(input()),
    int(input()),
    int(input())
]

if numbers[3] <= numbers[1]:
    print(numbers[0])
else:
    print(numbers[0] + (numbers[3] - numbers[1]) * numbers[2])