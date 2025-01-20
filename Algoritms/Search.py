m = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def recursive_binary_search(lst: list, num):
    return recursive_search(lst, num, 0, len(lst)-1)
def recursive_search(lst, num, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == num:
        return mid
    elif lst[mid] < num:
        return recursive_search(lst, num, mid + 1, right)
    else:
        return recursive_search(lst, num, left, mid - 1)


print(recursive_binary_search(m, 1))



