'''
Итератор — это объект в Python, который позволяет перебирать элементы коллекции
(список, кортеж, строка и другие итерируемые объекты) по одному за раз. Он поддерживает два ключевых метода:

1. __iter__() — возвращает сам объект-итератор. Это делает объект итерируемым.
2. __next__() — возвращает следующий элемент из коллекции. Если элементов больше нет, вызывает исключение StopIteration.
'''

# Список является итерируемым объектом
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # 1


class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Останавливает итерацию, когда достигнут конец
        self.current += 1
        return self.current - 1


my_iter = MyIterator(1, 5)

# Перебор значений с помощью next()
for val in my_iter:
    print(val)



