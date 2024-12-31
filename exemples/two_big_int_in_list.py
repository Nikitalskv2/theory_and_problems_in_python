nums = [1, 9, 3, 4, 5, 5]


def func(nums: list):
    n = 0
    l = list(set(nums))
    l.sort()
    print(l[-2])


func(nums)