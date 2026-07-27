# Create a list comprehension that returns the squares of only the even numbers from 0–20.

square = [i ** 2 for i in range (0, 21) if i % 2 == 0]
print(f'Square: {square}')

# 2. Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.

nums = [3, 1, 4, 1, 5, 9]
sorted_num = sorted(nums)  # It makes a new list which has sorted items while nums.sort() sorts the actual list

print("After sorting numbers: ",sorted_num)

# 3. Remove duplicates from a list while preserving the original order

nums = [3, 1, 4, 1, 5, 9]
new = list(dict.fromkeys(nums))

print(f'Without duplicates: {new}')

# 4. Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension

lists = [[1, 2], [3, 4], [5]]
new_list = []
new_list = [ab for an in lists for ab in an]

print("Flatten List: ",new_list)

# 5. Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore case.

names = ['Bob', 'alice', 'charlie', 'DAVID']
lower_case = [i.lower() for i in names]
lower_case.sort()

print("Alphabetical Order: ", lower_case)

# 6. Replace items from index 2–4 in a list with [100, 200] using slice assignment

listed1 = [10, 20, 30, 40, 50 ,60]
listed1[2:5] = [100, 200]

print("After Slicing: ", listed1)

# 7. Write a program to find all indices of a value in a list (e.g., all indices of 7)

nums = [7, 1, 4, 7, 7, 5, 9]
indice = [d for d,e in enumerate(nums) if e == 7]

print("All indices of 7 are ",indice)

# 8. Create a new list containing only elements that appear exactly once in the original list

nums = [7, 1, 4, 7, 7, 5, 9]
count = 0
my_new = [f for f in nums if nums.count(f)==1]

print("New list: ", my_new)

# 9. Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).

l = [1,2,3,4]
new_l = [l[-1]] + l[:-1]
print(f'List rotated: {new_l}')

# 10. Split a list into two lists: one with even numbers, one with odd numbers.

lists = [range(0,21)]
even = [n for n in range (0, 21) if n % 2 == 0]

print("Even list: ",even)

odd = [h for h in range (0, 21) if h % 2 != 0]
print("Odd list:", odd)