# 1. List Comprehension: Filter and Transform
lst = [1,2,3,4,5,6,7,8,9]
a = [i**2 for i in lst if i%2==0]
print(a)