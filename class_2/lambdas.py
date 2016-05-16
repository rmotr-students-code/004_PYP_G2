def subtract(x, y):
    if x < 10:
        return float()
    return x - y

def add(x, y):
    return x + y

def compute(x, y, op):
    return op(x, y)

compute(1, 2, add)
compute(1, 2, lambda x, y: x > 10 and float(x - y) or (x - y))