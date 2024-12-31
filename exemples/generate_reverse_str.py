# Написать функцию,
# которая генерирует все возможные перестановки символов строки.

from itertools import permutations


def revers(s: str):
    # return [''.join(p) for p in permutations(s)]

    # Базовый случай: если строка пустая или состоит из одного символа
    if len(s) == 1:
        return [s]
    permutations = []  # Список для хранения всех перестановок
    # Для каждого символа строки
    for i in range(len(s)):
        # Получаем оставшуюся часть строки без текущего символа
        remaining = s[:i] + s[i + 1:] # оставить начало  + ставить сзади + 1
        # Рекурсивно генерируем все перестановки для оставшейся части строки
        for perm in revers(remaining):
            # Добавляем текущий символ к каждой перестановке из оставшейся части
            permutations.append(s[i] + perm)

    return permutations

print(revers("abcd"))