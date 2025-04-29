# n = int(input("Введите n: "))
# m = int(input("Введите m: "))
n, m = map(int, input().split())

mass = list(range(1, n + 1))
res = []
val = 0
flag = True

while flag or mass[val] != 1:
    if val + m <= n:
        res.append(mass[val:val + m])
    else:
        res.append(mass[val:] + mass[0: (val + m) % n])

    val = ((val + m) % n)-1 if ((val + m) % n)-1 != -1 else n - 1
    flag = False

print(f"{''.join(str(i[0]) for i in res)}")

# print("Решение:")
# print("Круговой массив: ", *mass, sep="")
# print(f"При длинне обхода {m} получаем интервалы: {', '.join(''.join(map(str, i)) for i in res)}")
# print(f"Полученный путь: {''.join(str(i[0]) for i in res)}")


