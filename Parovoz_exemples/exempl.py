def mult():
    return [lambda x: i * x for i in range(5)]

print([m(2) for m in mult()])   ## [8, 8, 8, 8, 8]












