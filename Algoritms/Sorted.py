m = [8, 7, 4, 6, 1, 3, 9, 2, 5]


def tim_sort(lst: list):
    return sorted(lst), 'tim_sort'

# m = [8, 7, 4, 6, 1, 3, 9, 2, 5]


def fast_sort_hoare(lst: list):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    # right = [x for x in lst if x > pivot]

    right = []
    for i in lst:
        if i > pivot:
            right.append(i)

    return fast_sort_hoare(left) + middle + fast_sort_hoare(right)


def insert_sort(lst: list):
    '''
    for i in range(1, len(lst)):
        key = lst[i]
        sorted = i - 1
        while sorted >= 0 and key < lst[sorted]:
            lst[sorted + 1] = lst[sorted]
            sorted -= 1
        lst[sorted + 1] = key
    '''

    for i in range(1, len(lst)):
        sorted = i - 1
        while sorted >= 0 and lst[sorted] > lst[sorted+1]:
            lst[sorted + 1], lst[sorted] = lst[sorted], lst[sorted + 1]
            sorted -= 1
    return lst, 'insert_sort'


def select_sort(lst: list):
    for i in range(len(lst)-1):
        min_index = i
        for a in range(i+1, len(lst)):
            if lst[min_index] > lst[a]:
                min_index = a
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst, 'select_sort'


def bubble_sort(lst: list):
    count = len(lst)
    while (count > 0):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i + 1] = lst[i+1], lst[i]
        count -= 1
    return lst, 'bubble_sort'


# print(tim_sort(m))
print(fast_sort_hoare(m))
# print(insert_sort(m))
# print(select_sort(m))
# print(bubble_sort(m))

