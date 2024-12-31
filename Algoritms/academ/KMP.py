#1. Алгоритм Кнута-Морриса-Пратта

a = "лилила"

p = [0]*len(a)
j = 0
i = 1

while i < len(a):
    if a[j] == a[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]

print(p)