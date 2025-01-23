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


# цикличный обход и подсчет суммы уровней деревав
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


def rec_average_level(root):
    q = []
    res = []
    sum_l = 0
    q.append(root)
    while (len(q) > 0):
        print(q[0].val)
        node = q.pop(0)
        sum_l += node.val

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
        res.append(sum_l / len(q))

    return res


# print(rec_average_level(root))



