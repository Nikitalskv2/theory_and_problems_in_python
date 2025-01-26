m = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Бинарный поиск

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


# Поиск в хеш-таблице

hash_table = {'apple': 1, 'banana': 2, 'cherry': 3}
print(hash_table.get('banana', 'Не найдено'))  # Вывод: 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Пример дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)


# Поиск по бинарному дереву

def bst_search(root, target):
    if not root or root.val == target:
        return root
    if target < root.val:
        return bst_search(root.left, target)
    return bst_search(root.right, target)


result = bst_search(root, 7)
print(result.val if result else "Не найдено")  # Вывод: 7


# Поиск в графе (Graph Search)

from collections import deque

def bfs_search(graph, start, target):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node == target:
            return True  # Элемент найден
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return False  # Элемент не найден

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print(bfs_search(graph, 'A', 'F'))  # Вывод: True


# Интерполяционный поиск (Interpolation Search)

def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return -1  # Элемент не найден

arr = [1, 3, 5, 7, 9, 11, 13]
print(interpolation_search(arr, 7))  # Вывод: 3