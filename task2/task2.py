import sys
from fractions import Fraction


if len(sys.argv) != 3:
    print("Использование: python task2.py <circle.txt> <dot.txt>")
    sys.exit(1)

circle_file = sys.argv[1]
dot_file = sys.argv[2]

with open(circle_file, 'r') as file:
    lines = file.readlines()

x, y = map(Fraction, lines[0].strip().split())
r = Fraction(lines[1].strip())

with open(dot_file, 'r') as file:
    lines = file.readlines()

dots = [list(map(Fraction, lin.strip().split())) for lin in lines]

dot_in = lambda x0, y0: (((x-x0)**2 + (y-y0)**2) <= r**2)
dot_on = lambda x0, y0: (((x-x0)**2 + (y-y0)**2) == r**2)

print(*(0 if dot_on(dot[0], dot[1]) else 1
      if dot_in(dot[0], dot[1]) else 2 for dot in dots), sep="\n")
