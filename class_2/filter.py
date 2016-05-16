"""
# [1, 2, 3, 4] > [2, 4]

# x > True | False

def condition(x):
    return x % 2 == 0



evens = filter(condition, a_list)
evens_lc = [x for x in a_list if x % 2 == 0]
print(evens)

a_list = [1, 2, 3, 4]

evens_lc = [x * x for x in a_list if x % 2 == 0]
print(evens_lc)
"""

# Reduce: 
def op(acc, item):
    return acc + item

reduce(op, a_list, initial_value)