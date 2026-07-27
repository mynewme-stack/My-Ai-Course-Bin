# 1. Find Second Largest Unique Number
num=[1,2,3,4,5,6,7,8,9]
unique = sorted(set(num))
result = unique[-2] if len(unique)>=2 else None
print(f'Second largest greater number: {result}.')