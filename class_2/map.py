
# list > list

def op(x):
    return x * x

# [1, 2, 3] > [1, 4, 9]
# [1, 2, 3] > [op(1), op(2), op(3)] > [1, 4, 9]

numbers = [1, 2, 3]

squared = map(op, numbers)
squared_lc = [op(x) for x in numbers]

print(numbers)
print(squared)


"""
a_list = [1,3,4,5,"aa"]

def op(x):
    return "***{}***".format(x)

adjust = map(op, a_list)


for x in adjust:
    print (x)


"""
# Python 3.4 prints:
# <map object at 0x7fd121023208> 