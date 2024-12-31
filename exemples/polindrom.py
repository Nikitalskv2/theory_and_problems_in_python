s1 = 'Qwerewq'
s2 = 'qwert'
s3 = 'qweewq'


def func(s: str):
    s = "".join(s).lower()
    if s == s[::-1]:
        return True
    else:
        return False


print(func(s1))
