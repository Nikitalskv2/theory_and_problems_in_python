from typing import List


# 217. Contains Duplicate


def containsDuplicate(nums:  List[int]) -> bool:
    seen = set([])
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

    # if len(nums) == len(set(nums)):
    #     return False
    # return True



# a = [1,2,3,1]   # True
# b = [1,2,3,4]   # False
# print(containsDuplicate(a))
# print(containsDuplicate(b))



# 268. Missing Number
'''
При наличии массива nums, содержащего n различных чисел в диапазоне [0, n], 
верните единственное число в диапазоне, которое отсутствует в массиве.

Входные данные: nums = [3,0,1]
Выходные данные: 2
Пояснение: n = 3, поскольку имеется 3 числа, поэтому все числа находятся в диапазоне [0,3]. 
2 - это пропущенное число в диапазоне, поскольку оно не отображается в числах.
'''

def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

#   for i in range(0, len(nums)+ 1):
#       if i not in nums:
#           return i

# n = [3, 0, 1]   # 2
# print(missingNumber(n))


# 448. Find All Numbers Disappeared in an Array
'''
Учитывая массив nums из n целых чисел, где nums[i] находится в диапазоне [1, n], 
верните массив всех целых чисел в диапазоне [1, n], которые не отображаются в nums.

Входные данные: nums = [4,3,2,7,8,2,3,1]
Выходные данные: [5,6]
'''


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    result = []
    s = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in s:
            result.append(i)
    return result


# a = [1, 1]              # [2]
# b = [4,3,2,7,8,2,3,1]   # [5, 6]
# print(findDisappearedNumbers(a))
# print(findDisappearedNumbers(b))


# 136. Single Number
'''
Задан непустой массив целых чисел nums, каждый элемент которого, 
за исключением одного, отображается дважды. Найдите этот единственный элемент.
Необходимо реализовать решение с линейной сложностью во время выполнения 
и использовать только постоянный дополнительную память.

Ввод: nums = [2,2,1]
Вывод: 1
Ввод: nums = [4,1,2,1,2]
Вывод: 4
'''

def singleNumber(nums: List[int]) -> int:
    # XOR 41212
    # 0    000  4    100  5    101    7    111   6    110
    # 4    100  1    001  2    010    1    001   2    010
    # 4 -> 100  5 -> 101  7 -> 111    6 -> 110   4 -> 100 -->> 4

    mask = 0
    for num in nums:
        print(bin(num))
        mask ^= num     # ^= - XOR
    return mask


# s = [4, 1, 2, 1, 2]     # 4
# print(singleNumber(s))


# 70. Climbing Stairs
'''
Вы поднимаетесь по лестнице. Чтобы достичь вершины, требуется сделать n шагов.
Каждый раз вы можете подняться на 1 или 2 ступени. 
Сколькими различными способами вы можете подняться на вершину?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
###### ФИБОНАЧИ
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    n1 = 1
    n2 = 2

    for i in range(3, n + 1):
        n1, n2 = n2, n1 + n2
    return n2


# print(climbStairs(3))
# 2 - 2
# 3 - 3
# 4 - 5
# 5 - 8
# 6 - 13


# 121. Best Time to Buy and Sell Stock
'''
Вам предоставляется массив цен, где prices[i] - это цена данной акции на i-й день.
Вы хотите максимизировать свою прибыль, 
выбрав один день для покупки одной акции и другой день в будущем для продажи этой акции.
Верните максимальную прибыль, которую вы можете получить от этой транзакции. 
Если вы не можете получить никакой прибыли, верните 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Обратите внимание, что покупка во 2-й день и продажа в 1-й день запрещены, 
потому что вы должны купить перед продажей.
'''

def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        price = prices[i]

        profit = max(profit, price - buy)
        buy = min(buy, price)

    return profit

# n1 = [7,1,5,3,6,4]  # 5
# n2 = [7,6,4,3,1]    # 0
# print(maxProfit(n1))


# 53. Maximum Subarray
'''
Учитывая целочисленный массив nums, найдите
подмассив
с наибольшей суммой и верните его сумму.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    current = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        current = max(current + num, num)
        max_sum = max(current, max_sum)

    return max_sum

# s = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(s))     # 6


# 303. Range Sum Query - Immutable
'''
Вычисляем сумму элементов nums между индексами left и right включительно, где left <= right.
Реализуем класс NumArray:

NumArray(int[] nums) Инициализирует объект целочисленным массивом nums.
int sumRange(int left, int right) возвращает сумму элементов nums между 
  индексами слева и справа включительно 
(т.е. nums[слева] + nums[слева + 1] + ... + nums[справа]).

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
'''


class NumArray:
# сохраняем сумму элементов в лист
    def __init__(self, nums: List[int]):
        sums = []
        current_sum = 0

        for num in nums:
            current_sum += num
            sums.append(current_sum)
        self.sums = sums
        print(sums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


# l = [-2, 0, 3, -5, 2, -1]
# k = [2, 5]
# n = NumArray(l)
# n1 = n.sumRange(*k)
# print(n1)


# 338. Counting Bits
'''
Учитывая целое число n, верните массив ans длиной n + 1 таким образом, 
чтобы для каждого i (0 <= i <= n) ans[i] было числом 1 в двоичном представлении i.

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''

def countBits(n: int) -> List[int]:
    memo = [0] * (n+1)
    for i in range(1, n+1):
        memo[i] = memo[i >> 1] + i % 2

    return memo[:n+1]


# print(countBits(5))
