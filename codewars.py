def sort_array(orr):
    even_dct = {}
    odd_dct = {}
    fin = []
    for i in orr:
        if i%2==0:
            even_dct[i] = orr.index(i)
        else:
            odd_dct[i] = orr.index(i)
    sort_odd = sorted(odd_dct.items())
    cnt = 0
    for a in orr:
        if a % 2 == 0:
            fin.append(a)
        else:
            fin.append(sort_odd[cnt][0])
            cnt += 1
    return fin
# берем у нечет значения
#  сорт нечет меняем местами


# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   orr

# {8: 1,  6: 3,  4: 5,  2: 7,  0: 9}  even_dct

# {9: 0,  7: 2,  5: 4,  3: 6,  1: 8}  odd_dct

# [(1, 8), (3, 6), (5, 4), (7, 2), (9, 0)]  sort_odd  берем первое


print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
