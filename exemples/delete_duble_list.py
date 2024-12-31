l = [1, 1, 9, 3, 4, 5, 5]


def func(l: list) -> list:
    s = set()
    result = []
    for i in l:
        if i not in s:
            s.add(i)
            result.append(i)
    return result


print(func(l))
