class Value:
    def __init__(self, v):
        self.v = v

    def __repr__(self):
        return f'{self.v}'

    def __hash__(self):
        return hash(self.v)

    def __eq__(self, other):
        if not isinstance(other, Value):
            raise NotImplementedError()
        return self.v == other.v

storage = set([Value(1), Value(42), Value(1), Value("1")])
print(storage)
# ===> {1, 42, 1}
















