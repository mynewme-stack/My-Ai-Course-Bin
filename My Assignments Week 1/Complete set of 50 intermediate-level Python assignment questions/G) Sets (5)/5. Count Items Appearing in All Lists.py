# Count Items Appearing in All Lists
listed = [[1,5,4],[4,5,6]]
common = set(listed[0])
for lis in listed[1:]:
    common &= set(lis)
result = list(common)
print(result)