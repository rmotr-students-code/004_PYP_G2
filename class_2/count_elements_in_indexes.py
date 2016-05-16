a_list = [1, 4, 3, 4, 'a', 'c', '5', 2, 4]
allowed_indexes = [3, 4, 8]


# new_list = [a_list[3], a_list[4], a_list[8]]
# print(new_list.count(4))
"""
new_list = []
count = len(a_list)
i = 0
while i < count:
    elem = a_list[i]
    if i in allowed_indexes:
        new_list.append(elem)
    i += 1
new_list.count(4)
"""

"""
count = 0
result = 0
for elem in a_list:
    if elem == 4 and (count in allowed_indexes):
        result += 1
    count += 1
print(result)
"""

"""
for i in range(len(a_list)):
    elem = a_list[i]
    if i in allowed_indexes:
        # blah
        pass
"""
"""
for idx, elem in enumerate(a_list):
    if elem == 4 and (idx in allowed_indexes):
        result += 1

"""