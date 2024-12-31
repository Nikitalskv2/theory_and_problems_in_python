'''
Поиск суммы двух чисел
Даны массив и целевое число.
Найти два числа в массиве, которые в сумме дают целевое число.
'''

l = [1, 2, 5, 7, 1, 4, 9]


def func(l: list, k: int) -> list[int]:
    s = {}
    sum = []
    for i, num in enumerate(l):
        s[i] = num
    for _, i in s.items():
        sum.append(i)
        if len(sum) == 2:
            if sum[0] + sum[1] == k:
                return sum
            else:
                sum.pop()
    return sum


print(func(l, 6))
