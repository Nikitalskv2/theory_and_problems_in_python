l = ("AAABBCZZZDDDDAAA")


def func(letter: str) -> str:
    a = ''
    b = []  # ['', 'A3', 'B2', 'C', 'Z3', 'D4']
    count = 1
    for i in letter:
        if i != a:
            if count == 1:
                b.append(a)
            else:
                b.append(a + str(count))
            a = i
            count = 1
        else:
            count += 1
    if count == 1:
        b.append(a)
    else:
        b.append(a + str(count))
    result = ''.join(b)
    return result


print(func(l))


