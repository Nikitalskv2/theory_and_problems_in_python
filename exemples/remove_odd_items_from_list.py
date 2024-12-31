# удалить все елементы на нечетных позициях из списка

l = [1, 2, 3, 4, 5]


def func_1(lst: list) -> list:
    # 12345
    # 13245
    # 13542
    # 13524
    l = 1
    for i in range(2, len(lst), 2):  # переносим четные индексы в конец
        lst[l], lst[i] = lst[i], lst[l]
        l = i
    for i in range(len(lst) // 2):  # удаляем с конца
        lst.pop()
    return lst
# Сложность по времени: O(n)
# Сложность по памяти: O(1)


# срезом
def func_2(lst: list) -> list:
    return lst[::2]
# Время: O(n)
# Память: O(n) (создает новый список)


# enumerate
def func_3(lst: list) -> list:
    return [value for index, value in enumerate(lst) if index % 2 == 0]
# Время: O(n)
# Память: O(n)


print(func_1(l))
