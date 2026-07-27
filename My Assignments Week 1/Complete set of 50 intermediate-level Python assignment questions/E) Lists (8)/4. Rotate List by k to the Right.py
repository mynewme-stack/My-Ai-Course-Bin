# Rotate List by k to the Right
lst = [1,2,3,4,5,6,7,8,9]
k = 3
if lst:
    k%= len(lst)
    rotate = lst [-k:]+lst[:-k]
else:
    rotate=[]
print(rotate)