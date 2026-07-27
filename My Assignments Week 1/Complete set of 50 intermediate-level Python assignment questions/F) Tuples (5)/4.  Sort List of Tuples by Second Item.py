# 1. Sort List of Tuples by Second Item
tuples = [('a',3),('b',1)]
sort = sorted(tuples, key=lambda t: t[1])
print(f'Sorted Data:\n{sort}')