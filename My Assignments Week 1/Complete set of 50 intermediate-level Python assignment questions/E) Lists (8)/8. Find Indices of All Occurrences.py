# 1. Find Indices of All Occurrences
listed = [4,1,2,3,3,4,3,4]
target = 4
indice = [i for i, v in enumerate(listed) if v==target]
print(f'Number for comes: {indice}.')