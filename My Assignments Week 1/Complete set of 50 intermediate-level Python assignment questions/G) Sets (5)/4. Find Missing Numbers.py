# Find Missing Numbers
listed = [1,2,3,4,4,6,6,8]
n = 9
miss = list(set(range(1, n+1))- set(listed))
print(miss)