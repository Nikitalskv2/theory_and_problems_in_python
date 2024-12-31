class A:
    def method(self):
        print("method A")


class B(A):
    def method(self):
        print("method B")


class C(A):
    def method(self):
        print("method C")


class D(B, C):
    pass

D().method()    ## method B
print(D.__mro__)
"""
(<class '__main__.D'>, 
<class '__main__.B'>, 
<class '__main__.C'>, 
<class '__main__.A'>, 
<class 'object'>)

"""