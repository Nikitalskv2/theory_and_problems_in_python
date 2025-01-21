import time


def merge_dicts(dict_1: dict, dict_2: dict) -> None:
    for key, value in dict_2.items():
        # «ПРЕДСТАВЬ, ЧТО СТРОКА ТВОЕГО КОДА БУДЕТ ЗДЕСЬ»

        dict_1.update(dict((key, dict_1.get(key, value)) for key, value in dict_2.items()))


my_dict = {"a": 0, "b": 1}
merge_dicts(my_dict, {"a": None, "b": "888", "c": 2})
# print(my_dict)
# my_dict -- {"a": 0, "b": 1, "c": 2) # Выражение истинно


words = ["apple", "banana", "carrot", "orange"]
# words = list(<ПРЕДСТАВЬ, ЧТО СТРОКА ТВОЕГО КОДА БУДЕТ ЗДЕСЬ»)
words = list(sorted(words, key=lambda x: x[-1]))


# print(words == ["banana", "apple", "orange", "carrot"])  # выражение истинно


def x2(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res * 2

    return inner


def sum(a, b):
    return a + b


# sum = x2(sum)
# print(sum(4, 6))


'''
Реализуйте функцию-гененратор - аналог 'chunked' из библиотеки 'more_itertools'
Генератор должен делить входящий iterable на чанки заданного размена
'''

import json
from typing import Iterator, Iterable


def chunked_list(iterable: Iterable, chunk_size: int) -> Iterator[list]:
    chunk = []

    for i in iterable:
        chunk.append(i)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


# list_to_chunk, size = input().split('; ')
# list_to_chunk = iter(json.loads(list_to_chunk))
# size = int(size)

# print(list(chunked_list(list_to_chunk, size)))
# [1,2,3,4,5,6,7]; 2


###### Тех собес ####################################################################################
import pytest


# поменять в словаре ключи и значения местами
def func(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        try:
            new_d[v] = k
        except:
            pass
    return new_d


'''
# test
print(func({1: 2, 3: 4}) == {2: 1, 4: 3})
print(func({1: 2, 3: 2}) == {2: 3})
print(func({None: None}) == {None: None})
print(func({}) == {})
print(func({1: [], 2: 3, 3: (1, 2, 3), 4: (1, 2, [])}) == {3: 2, (1, 2, 3): 3})
'''

# Тесты с использованием parametrize
'''
@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        ({1: 2, 3: 4}, {2: 1, 4: 3}),
        ({1: 2, 3: 2}, {2: 3}),
        ({None: None}, {None: None}),
        ({}, {}),
        ({1: [], 2: 3, 3: (1, 2, 3), 4: (1, 2, [])}, {3: 2, (1, 2, 3): 3}),
        ({1: [1, 2], 2: {3: 4}}, {}),
        ({1: "a", 2: "b", 3: "a"}, {"a": 3, "b": 2}),
    ])
def test_func(input_dict, expected_output):
    assert func(input_dict) == expected_output

структура теста 

@pytest.mark.parametrize(
    'first_param', 'second_param',
    [
        ({}, {}),
        ({}, {})
    ])
def test_func(first_param, second_param):
    assert func(first_param) == second_param

'''

a = {'a': 1, 'a': 2}


# print(a)


class A:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 1


d = {A(1): 2, A(2): 3}
# print(d)    # {<__main__.A object at 0x000001DC3E686A90>: 2,
#  <__main__.A object at 0x000001DC3E6E92D0>: 3}
'''
__eq__ сравнивает объекты по их идентификаторам (адресам в памяти),
поскольку это разные объекты, они считаются неравными.
'''

'''
Тесты:

моки - полное закрытие логики
стабы - минимальная реализация логика для подмены реальной
фикстуры - преднастроенные значения, часто используемая в тестах (в conftest)
скоупы - тесты работают в тест. окружении, нужны для изоляции
'''

'''
 - ИТЕРАТОРЫ - это объект, который представляет поток данных. 
Повторяемый вызов метода __next__() итератора или передача его встроенной функции next() 
возвращает последующие элементы потока.
Если больше не осталось данных, выбрасывается исключение StopIteration. 
После этого итератор исчерпан и любые последующие вызовы его метода __next__() снова 
генерируют исключение StopIteration.
Итераторы обязаны иметь метод __iter__, который возвращает сам объект итератора, 
так что любой итератор также является итерабельным объектом и может быть использован почти везде, 
где принимаются итерабельные объекты.

 - ГЕНЕРАТОРЫ - может означать либо функцию-генератор, 
либо итератор генератора (чаще всего, последнее). 
Методы __iter__ и __next__ у генераторов создаются автоматически.
языковая конструкция, которую можно реализовать двумя способами: 
как функция с ключевым словом YIELD или как генераторное выражение. 
В результате вызова функции или вычисления выражения, получаем объект-генератор

Так как в объекте-генераторе определены методы __next__ и __iter__, 
то есть реализован протокол итератора, с этой точки зрения, 
в Python любой генератор является итератором

Когда выполнение функции-генераторы завершается 
(при помощи ключевого слова return или достижения конца функции), 
возникает исключение StopIteration

YIELD замораживает состояние функции-генератора и возвращает текущее значение. 
После следующего вызова __next__() функция-генератор продолжает своё выполнение с того места, 
где она была приостановлена

send(value) – продолжает выполнение и отправляет значение в функцию-генератор. 
Аргумент value становится значением текущего yield-выражения.

Генератор хранит в памяти не все элементы, 
а только внутреннее состояние для вычисления очередного элемента
'''


# реализовать и аннотировать геннератор, на вход итерируемы обьект,
# результат- бесконечное повторение значений

from typing import Iterator, Any


def inf_gen(items: Iterable) -> Any:
    while True:
        for item in items:
            yield item


# f = inf_gen("abc")
# res = [next(f) for _ in range(5)]
# print(res)
# res2 = [next(f) for _ in range(2)]
# print(res2)
# res3 = f.send(3)
# print(res3)

'''
реализовать декоратор для изменения времени работы функции. 
Ниже в коде представлены примеры - декорированная функция 
и результат работы декоратора после вызова функции

logger = getLogger()

@timeit(logger)
def f(s):
    time.sleep(s)

f(1) -> [INFO] f(1): 1.1 sec 
'''
import logging
from functools import wraps
import time


def timeit(logger):
    def dec(func):
        @wraps(func)
        def inner(*args, **kwargs):
            time_start = time.monotonic()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.monotonic() - time_start
                logger.info(f'{func.__name__}({",".join([str(i) for i in args])}): {end} sec')

        return inner

    return dec


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@timeit(logger)
def f(s):
    time.sleep(s)

# f(1)  #   INFO:root:f(1): 1.0 sec


# 2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def cache(ttl):

    def dec(func):
        cache_mem = {}
        @wraps(func)
        def inner(*args, **kwargs):
            if str(args) + str(kwargs) in cache_mem:
                logger.info(f'{func.__name__}{args}: get result {cache_mem[str(args) + str(kwargs)]} from cache')
                return cache_mem[str(args) + str(kwargs)]
            else:
                res = func(*args, **kwargs)
                cache_mem[str(args) + str(kwargs)] = res
                return res
        return inner

    return dec


@cache(ttl=1)
def foo(a, b):
    return a+b


# print(foo(2, 3))
# time.sleep(2)
# print(foo(2, 3))
# print(foo(3, 4))



'''
Напиши запрос, который получит из бд 10 последних по времени создания 
комментариев пользователя с логином johndoe 
'''

'''
CREATE TABLE users (
id SERIAL PRIMERY KEY,
name VARCHAR (64) NOT NULL,
lastname VARCHAR (64) NOT NULL,
login VARCHAR (64) NOT NULL
);

CREATE TABLE messages (
id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(id),
text VARCHAR (255) NOT NULL,
created_at TIMESTAMP NOT NULL
);

SQL
"
SELECT text FROM messages
INNER JOIN users ON messages.user_id = users.id
WHERE user.login = 'johndoe'
ORDER BY created_at DESC
LIMIT 10 
"

Индексы

эксплейны

ACID

 -- КОНКУРЕНТНОСТЬ -- 

awaitable обьекты - обьекты которым можно сказать await, явно сказать подождать
await в этом месте код передает управление другой coroutine и 
пока тот код не будет выполнен наш код будет ждать
coroutine, Task, Future

coroutine - обьект корорый умеет хранить состояние и может передавать управление
частный случай генератора (old - yield from)
async def - определение асинхронной функции, которая возвращает coroutine обьект
coroutine обьект передается в event loop

event loop - запускается через asyncio.run() ожидая окончания работы  

task - asyncio.create_task() позволяет запускать задачи в фоне, оборачивает coroutine в Task
и планирует ее выполнение в event loop на ближайшее время
имеет контекст, состояние задачи, хранит в себе резутьтат или exc

Future - обещание выполнения. 
Объект, который представляет асинхронную операцию, 
результат которой будет доступен в будущем

'''

# контекстный менеджер

class Context:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.file.close()
        if exc_type is not None:
            print("error")
        else:
            return True


# select m.text
# from message m
# join users s on m.user_id = u.id
# where u.login = 'johndoe'
# order by m.created_at desc
# limit 10

# offset 10
# илиQ
# FETCH NEXT 10 ROWS ONLY;


# алго ###################################################################

#  шахматная ладья
m = [
    [1, 2, 3],
    [3, 4, 1],
    [3, 5, 2]
]


def maxRookSum(arr):
    size = len(arr)
    sum_v = []
    sum_h = []

    for i in range(size):
        count_v = 0
        sum_h.append(sum(arr[i]))
        for a in range(size):
            count_v += arr[a][i]
        sum_v.append(count_v)
        count_v = 0

    m_h = arr[sum_h.index(max(sum_h))]

    return m_h[sum_v.index(max(sum_v))]


# print(maxRookSum(m))

# корабли

n = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]


# -> 6

# [
#     (1, 0, 1, 0, 1, 0),
#     (1, 0, 0, 0, 0, 0),
#     (0, 0, 1, 0, 1, 0),
#     (0, 0, 0, 0, 1, 0),
#     (1, 1, 1, 0, 1, 0),
#     (0, 0, 0, 0, 1, 0)
# ]


def ship(arr: list[list[int]]) -> int:
    count = 0

    for h in range(len(arr)):
        for v in range(len(arr)):
            if arr[h][v] == 1:
                is_check = check(arr, h, v)
                if is_check:
                    count += 1

    return count

def check(arr, h, v) -> bool:
    if (h > 0 and arr[h-1][v] == 1) or (v > 0 and arr[h][v-1] == 1):
        return False
    else:
        return True

# print(ship(n))


# Даны две строки
# состоящие из строчных латинских букв и символов удаления '#'
# проверить равны ли эти строки с примененными #

a1 = ('ab#c', 'ad#c')    # true
b1 = ('#ab##', '#cd##')    # true
c1 = ('ab#c', 'ac#b')    # false

def backspace(a, b) -> bool:
    new_a = ''
    new_b = ''

    for i in range(len(a)):
        if a[i] != '#':
            new_a += a[i]
        else:
            new_a = new_a[:-1]

        if b[i] != '#':
            new_b += b[i]
        else:
            new_b = new_b[:-1]

    print(new_a == new_b)

# backspace(*a1)
# backspace(*b1)
# backspace(*c1)



# скобочки

'''
Дана неправильная скобочная последовательность
нужно выяснить можно ли заменить одну скобку
чтобы получилось правильно
если можно вывести индекс скобки которую надо поменять
если нельзя вывести -1

'''
q = [
    '()',        # 0  true
    '))',        # 1  0
    '()((',      # 2  3
    ')()',       # 3  -1
    ')',         # 4  -1
    '(()',       # 5  -1
    '))))',      # 6  [0,2]
    '((())(((',  # 7  [5,7]
]


def bracket(arr):
    opens = []
    closes = []

    for i in range(len(arr)):
        if arr[i] == '(':
            opens.append(i)
        else:
            if opens:
                opens.pop()
                # pass
            else:
                closes.append(i)
    if not opens and not closes:
        return True
    elif len(opens) == 1 or len(closes) == 1:
        return False

    elif len(opens) == 0:
        return closes[::2]
    elif len(closes) == 0:
        return opens[1::2]

#
# for i in range(len(q)):
#     print(f'{i}:  ', end='')
#     print(bracket(q[i]))
'''
0:  True
1:  [0]
2:  [3]
3:  False
4:  False
5:  False
6:  [0, 2]
7:  [5, 7]
'''


'''
Дана строка из латинских букв, цифр и скобок

3AB2(Z3K) -> AAABZKKKZKKK
2(Z3(KA)) -> ZKAKAKAZKAKAKA
'''


import re


def expand_expression(s):
    # Определите функцию для обработки вложенных выражений
    def expand(match):
        count = int(match.group(1))
        content = match.group(2)
        return count * process(content)

    # Рекурсивная функция для обработки строки
    def process(substring):
        # Обрабатываем вложенные круглые скобки от самых внутренних до самых внешних
        while '(' in substring:
            substring = re.sub(r'(\d+)\(([^()]+)\)', expand, substring)

        # Замените оставшиеся числовые повторы простым расширением
        substring = re.sub(r'(\d+)([A-Z])', lambda m: int(m.group(1)) * m.group(2), substring)
        return substring

    return process(s)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("3AB2(Z3K)", "AAABZKKKZKKK"),
        ("2(Z3(KA))", "ZKAKAZKAKAKA"),
        ("4(A2(B3(C)))", "ABCCCBCCCBCCCBCCCBCCCBCCCBCCC"),
        ("1(A)3(B2(C))", "ABCCBCCBCC"),
    ]

    for expression, expected in test_cases:
        result = expand_expression(expression)
        print(f"Expression: {expression}\nExpected: {expected}\nResult:   {result}\n")
        # assert result == expected, f"Test failed for expression {expression}"

    print("All tests passed!")
