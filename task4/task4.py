import math

with open('numbers.txt', 'r') as file:
    lines = file.readlines()

numbers = [int(lin.strip()) for lin in lines]
median = sum(num for num in numbers) / len(numbers)

sum_nums = math.floor(median) if median < 0 else math.ceil(median)

print(sum(abs(sum_nums - num) for num in numbers))
