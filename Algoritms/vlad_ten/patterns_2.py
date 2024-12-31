# 141. Linked List Cycle
'''
По заданному заголовку, началу связанного списка, можно определить, есть ли в связанном списке цикл.
В связанном списке есть цикл, если в списке есть какой-либо узел,
к которому можно снова перейти, непрерывно следуя следующему указателю.
Внутренне pos используется для обозначения индекса узла,
к которому подключен следующий указатель tail.
Обратите внимание, что pos не передается в качестве параметра.
Верните значение true, если в связанном списке есть цикл. В противном случае верните значение false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head) -> bool:
    if not head:
        return False

    slow = fast = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False


# node1 = ListNode(3)
# node2 = ListNode(2)
# node3 = ListNode(0)
# node4 = ListNode(-4)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
#
# print(hasCycle(node1))


# 876. Middle of the Linked List
'''
Учитывая начало односвязного списка, 
верните средний узел связанного списка.
Если есть два средних узла, верните второй средний узел.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val


# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
#
# print(middleNode(n1))   # 4


# 206. Reverse Linked List
'''
https://leetcode.com/problems/reverse-linked-list/description/
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# pr = reverseList(n1)
# while True:
#     if not pr:
#         break
#     print(pr.val)
#     pr = pr.next


# 234. Palindrome Linked List
'''
https://leetcode.com/problems/palindrome-linked-list/description/
Input: head = [1,2,2,1]
Output: true
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        if not head:
            return None

        middle = self.middleNode(head)
        reverse = self.reverseList(middle)

        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head):
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev

# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(2)
# n4 = ListNode(1)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
#
# pr = Solution()
# p = pr.isPalindrome(n1)
# print(p)


# 203. Remove Linked List Elements
'''
https://leetcode.com/problems/remove-linked-list-elements/description/
Учитывая заголовок связанного списка и целое число val, 
удалите все узлы связанного списка, у которых есть Node.val == val, 
и верните новый заголовок.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    result = ListNode(0)
    result.next = head

    current = result

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return result.next


# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(6)
# n4 = ListNode(3)
# n5 = ListNode(4)
# n6 = ListNode(5)
# n7 = ListNode(6)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
#
# pr = removeElements(n1, 6)
# while True:
#     if not pr:
#         break
#     print(pr.val)
#     pr = pr.next


# 83. Remove Duplicates from Sorted List
'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
Учитывая начало отсортированного связанного списка, удалите все дубликаты, 
чтобы каждый элемент отображался только один раз. 
Верните отсортированный связанный список.

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head

    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# n1 = ListNode(1)
# n2 = ListNode(1)
# n3 = ListNode(6)
# n4 = ListNode(4)
# n5 = ListNode(4)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# pr = deleteDuplicates(n1)
# while True:
#     if not pr:
#         break
#     print(pr.val)
#     pr = pr.next


# 21. Merge Two Sorted Lists
'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
Вам будут предоставлены заголовки двух отсортированных связанных списков list1 и list2.
Объедините два списка в один отсортированный список. 
Список должен быть создан путем объединения узлов первых двух списков.
Верните заголовок объединенного связанного списка.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    merged = ListNode(0)
    result = merged

    while l1 and l2:
        if l1.val < l2.val:
            merged.next = ListNode(l1.val)
            l1 = l1.next
        else:
            merged.next = ListNode(l2.val)
            l2 = l2.next
        merged = merged.next

    while l1:
        merged.next = ListNode(l1.val)
        l1 = l1.next
        merged = merged.next

    while l2:
        merged.next = ListNode(l2.val)
        l2 = l2.next
        merged = merged.next
    return result.next


# 252. Meeting Rooms
'''
https://www.lintcode.com/problem/920/description
Учитывая массив временных интервалов собраний, 
состоящий из времени начала и окончания [(s1,e1),(s2,e2),...] (si < ei), 
определите, может ли человек присутствовать на всех собраниях.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend_meetings(intervals) -> bool:
    intervals = sorted(intervals, key=lambda x: x.start)

    for i in range(len(intervals) - 1):
        if intervals[i].end > intervals[i + 1].start:
            return False
    return True


intervals = [Interval(0,30),
             Interval(5,10),
             Interval(15,20)]

# print(can_attend_meetings(intervals))


# 704. Binary Search
'''
https://leetcode.com/problems/binary-search/description/
Учитывая массив целых чисел nums, отсортированный в порядке возрастания, 
и целочисленный целевой объект, напишите функцию для поиска целевого объекта в nums. 
Если целевой объект существует, то верните его индекс. 
В противном случае верните значение -1.

Необходимо написать алгоритм со сложностью выполнения O(log n).

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''


def search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = left + (right-left) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return - 1


# print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
