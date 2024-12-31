'''
Нужно написать функцию, которая переворачивает строку.Входная строка задается, как массив символов s.Нужно изменить входной массив на месте без дополнительной памяти

Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

Input: s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]

def func(lst: list) -> list:
    index_end = len(lst) - 1
    index_start = 0
    while index_start < index_end:
        lst[index_start], lst[index_end] = lst[index_end], lst[index_start]
        index_start += 1
        index_end -= 1
    return lst

Реализовать декоратор с параметрами, который будет выводить в результате время выполнения и количество вызовов декорируемой функции(Часть 1)
Параметризовать декоратор так, чтобы можно было контролировать количество вызовов(Часть 2)

from functools import wraps
import time

def my_decorator(count):
    def dec(func):
        @wraps(func)
        def inner(*args, **kwargs):
            times = 0
            for i in range(0, count):
                time_start = time.time()
                res = func(*args, **kwargs)
                times += time.time() - time_start
            print(f'Время выполенния {(times/count):.2f}, кол-во вызовов {i + 1}')
            return res
        return inner
    return dec

@my_decorator(1)
def add_numbers(x: int, y: int) -> int:
    return x + y

add_numbers(1, 2) #-> Время выполенния 0.01, кол - во вызовов 1
add_numbers(3, 4) #-> Время выполенния 0.02, кол - во вызовов 2
add_numbers(5, 5) #-> Время выполенния 0.03, кол - во вызовов 3


-> Реализовать контекстный менеджер RedisLock, который будет делать sleep(1.0), если в редисе стоит лок

def redis_get(key: str): pass
def redis_set(key: str, value: Any, expire: float): pass
def redis_delete(key: str): pass

class RedisLock:
    def __init__(self, key, expire=60):
        self.key = key
        self.lock = False
        self.value = ''
        self.expire = expire

    def __enter__(self):

        if redis_get(self.key) is not None:
            time.sleep(1)
        else:
            self.lock = True
            redis_set(self.key, self.value = "True", self.expire)
            return self

    def __exit__(self):
        if redis_delete(self.key) is not None:
            self.lock = False
# хз

def heavy_code():
    ...

def main_user_handler(user_id: int):
    key = f"user__{user_id}"
    with RedisLock(key=key):
        heavy_code()


-> Оцени примерное время выполнения функции get_data

async def get_data():
    await get_users()  # execution - 0.5 seconds
    await get_orders()  # execution - 1.0 seconds
# 1.5s

→ Пусть есть таблица товаров и их производителей.

Таблица
"product"
+----------------+---------+
| Column    Name | Type    |
+----------------+---------+
| id             | int     | - уникальный ключ для таблицы продуктов
| name           | varchar | - наименование продукта
| company        | varchar | - наименование производителя
| product_count  | int     | - количество продукта
| price          | int     | - цена продукта
| is_discounted  | int     |  - есть скидка на продукт(bool)

1. Надо сгруппировать товары по производителям с ценой выше 30000 рублей.Вывести наименование производителя и кол - во товаров

SELECT company, COUNT(name) AS count_name
FROM product
WHERE price > 30000
GROUP BY company
ORDER BY company DESC

'''


