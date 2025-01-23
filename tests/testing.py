b = [3,2,1,4,9,7,8,5,6]

def select_sort(arr):
    for i in range(len(arr) - 1):
        min_i = i
        for a in range(i+1, len(arr)):
            if arr[a] < arr[min_i]:
                min_i = a
        if arr[min_i] < arr[i]:
            arr[min_i], arr[i] = arr[i], arr[min_i]
    return arr

# print(select_sort(b))

def insert_sort(arr):
    for i in range(len(arr)):
        sort = i - 1
        while sort >= 0 and arr[sort] > arr[sort + 1]:
            arr[sort], arr[sort + 1] = arr[sort + 1], arr[sort]
            sort -= 1
    return arr

# print(insert_sort(b))



def sorting(arr):
    middle = arr[len(arr)//2]

    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

    left = sorted(arr[len(arr) - len(middle)])
    right = sorted(arr[len(arr) - len(middle)])






