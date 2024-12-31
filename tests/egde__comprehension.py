#1
a = [i for i in range(5)]
b = (i for i in range(5))


print(a)    ## [0, 1, 2, 3, 4]
print(b)    ## generator object

#2
def printer(value=[]):
    value.append(1)
    print(value)


printer()
printer()
printer(value=[2])
# [1]
# [1, 1]
# [2, 1]

