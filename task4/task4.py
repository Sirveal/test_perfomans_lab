import sys
import math


if len(sys.argv) != 2:
    print("Использование: python task4.py <numbers.txt>")
    sys.exit(1)

numbers_file = sys.argv[1]

with open(numbers_file, 'r') as file:
    lines = file.readlines()

numbers = [int(lin.strip()) for lin in lines]

numbers.sort()
n = len(numbers)
median = (numbers[n//2 - 1] + numbers[n//2])/2 if n % 2 == 0 else numbers[n//2]

sum_nums = math.floor(median) if median < 0 else math.ceil(median)
print(sum(abs(sum_nums - num) for num in numbers))
