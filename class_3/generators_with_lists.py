"""
results = [0, 1, 2, 3, 4]
"""



def first_n_integers(n=10):
    results = []
    for i in range(n):
        results.append(i)
    return results

elems = first_n_integers(5)
for elem in elems:
    print(elem)