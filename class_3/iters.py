class SimpleIterator(object):
    def __init__(self):
        self.next_number = 0

    def __iter__(self):
        self.next_number = 0
        return self

    def __next__(self):
        self.next_number += 1
        if self.next_number >= 5:
            raise StopIteration()

        return self.next_number

    next = __next__


it = SimpleIterator()

"""j
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # 5th

"""
for numb in it:
    print(numb)

print("2nd for-loop:")

for numb in it:
    print(numb)
