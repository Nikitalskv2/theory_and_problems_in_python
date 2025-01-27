from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node4 = Node(4)
node7 = Node(7)
node13 = Node(13)
node1 = Node(1)
node6 = Node(6, node4, node7)
node14 = Node(14, node13)
node3 = Node(3, node1, node6)
node10 = Node(10, None, node14)
root = Node(8, node3, node10)
'''
      8
    /   \ 
    3    10 
   / \    \ 
  1   6    14
     / \  / 
     4 7 13 
     
q = [8,3,10,1,6,Null,14,Null,4,7,13,Null] 
'''

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# [1, 3, 4, 6, 7, 8, 10, 13, 14]
# обхода дерева по центрированному алгоритму
# inorder(root)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# [1, 4, 7, 6, 3, 13, 14, 10, 8]
# обхода дерева по обратному алгоритму
# postorder(root)


def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# [8, 3, 1, 6, 4, 7, 10, 14, 13]
# обхода дерева по прямому алгоритму
# preorder(root)


def level_order(root):
    q = []
    q.append(root)
    while(len(q) > 0):
        print(q[0].val)
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

# [8, 3, 10, 1, 6, 14, 4, 7, 13]
# обход дерева в ширину с помощью очереди
# level_order(root)


# цикличный обход и подсчет среднего арифметического уровней деревьев
from collections import deque


def norec_average_level(root):
    q = deque([root])

    result = []

    while q:
        n = len(q)
        level_sum = 0
        for _ in range(n):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_sum / n)

    return result

# print(norec_average_level(root))
# [8.0, 6.5, 7.0, 8.0]


# рекурсивно сумма уровней
def rec_sum_level(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        if level >= len(result):
            result.append(0)
        result[level] += node.val

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


# print(rec_sum_level(root))
# [8, 13, 21, 24]


# Дано дерево, найти его минимальную глубину
# 111. Minimal depth of binary tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# BFS

# from collections import deque
def minDepth(root) -> int:
    if not root:
        return 0

    depth = 1

    q = deque([root])

    while q:
        for _ in range(len(q)):
            node = q.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth

# print(minDepth(root))
# 3


node4 = Node(5)
node7 = Node(8)
node13 = Node(14)
node1 = Node(2)
node6 = Node(7, node4, node7)
node14 = Node(15, node13)
node3 = Node(4, node1, node6)
node10 = Node(11, None, node14)
root2 = Node(9, node3, node10)


# Проверить два одинаковых дерева
# 100. same tree
# https://leetcode.com/problems/same-tree/description/

# from collections import deque
def same_tree(p, q) -> bool:
    queue = deque([p, q])

    while queue:
        p = queue.popleft()
        q = queue.popleft()

        if not p and not q:
            continue

        if not p or not q:
            return False
        if p.val != q.val:
            return False

        queue.append(p.left)
        queue.append(q.left)
        queue.append(p.right)
        queue.append(q.right)

    return True


# print(same_tree(root, root2))     # False


# реккурсивно сравниваем деревья
def rec_same_tree(p, q) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    return rec_same_tree(p.left, q.left) and rec_same_tree(p.right, q.right)


# print(rec_same_tree(root, root2))     # False


# Дано дерево и таргет. Определить есть ли такой путь в сумме дающий таргет
# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/

def path_sum(root, target: int) -> bool:
    if not root:
        return False

    target -= root.val
    if not root.left and not root.right:
        return target == 0

    return path_sum(root.left, target) or path_sum(root.right, target)


# print(path_sum(root, 12))     # True


# Найти диамерт (самый длинный путь между листьями)
# 246 через класс, 269 через рекурсию и tuple

# 543. Diameter of binary tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# dfs

class Solution:
    def diameter_self_tree(self, root) -> int:
        self.diameter = 0

        def lp(node):
            if not node:
                return 0

            left = lp(node.left)
            right = lp(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        lp(root)
        return self.diameter


c = Solution()
# print(c.diameter_self_tree(root))   # 6


def diameter_tree(root) -> int:
    def dfs(node):
        if node == None:
            return (0, 0)

        left_path, left_diameter = dfs(node.left)
        right_path, right_diameter = dfs(node.right)
        return (max(left_path, right_path) + 1, max(left_diameter, right_diameter, left_path + right_path))

    return dfs(root)[1]


# print(diameter_tree(root))  # 6


# Соединить два дерева (если есть ноды - сложить, если нет нод - создать)
# 617. merge two binary trees
# https://leetcode.com/problems/merge-two-binary-trees/

def mergeTrees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1

    root1.val += root2.val

    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1

# merge = mergeTrees(root, root2)
# print(level_order(merge))


# Найти самый длинный путь
# 104. maximum depth of binary tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def max_depth(root) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


# print(max_depth(root))  # 4


# Бинарное дерево поиска.
# Найти общего предка дерева от p и q
# 345 рекурсивно
# 235. lowest common ancestor of a binary search tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

def lowest_common_ancestor(root, p, q):
    node = root

    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node

    return None

# print(lowest_common_ancestor(root, node1, node7))


# recursive
def rec_lowest_ancestor(root, p, q):
    if root.val > p.val and root.val > q.val:
        return rec_lowest_ancestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return rec_lowest_ancestor(root.right, p, q)

    return root

# print(rec_lowest_ancestor(root, node7, node1))


# Поиск поддерева
# 572. subtree
#

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)