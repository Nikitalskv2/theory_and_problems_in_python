'''
Физз-Базз
Для чисел от 1 до N:

Если число делится на 3, вывести "Fizz".
Если делится на 5, вывести "Buzz".
Если делится на 3 и 5, вывести "FizzBuzz".
'''

l = [1, 9, 3, 4, 5, 5, 7, 15, 20, 30]


def func(l: list) -> list:
    result = []
    for i in l:
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = 'Fizz'
        elif i % 5 == 0:
            i = "Buzz"
        result.append(i)
    return result


print(func(l))
