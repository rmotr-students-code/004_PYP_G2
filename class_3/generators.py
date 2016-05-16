
def first_n_integers(n=10):
    i = 0
    while i < n:
        yield i
        i += 1


class first_n_integers(object):
    def __init__(self, n=0):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == n - 1:
            raise StopIteration()

        aux = i
        self.i += 1

        return aux

    next = __next__
