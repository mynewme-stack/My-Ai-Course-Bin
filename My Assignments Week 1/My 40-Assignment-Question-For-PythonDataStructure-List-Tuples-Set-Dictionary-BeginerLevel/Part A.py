# 1. Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.

nums = [3, 1, 4, 1, 5]

print(f"First Element = {nums[0]}\nSecond Element = {nums[4]}")

# 2. Find the length of the list colors = ['red', 'blue', 'green'].

colors = ['red', 'blue', 'green']
length = len(colors)

print(f"Length of List = {length}.")

# 3. Append 'yellow' to the list colors = ['red', 'blue'].

colors = ['red', 'blue']
print("List = ", colors)

colors.append("yellow")
print("After using append = ", colors)

# 4. Insert 'orange' at index 1 in fruits = ['apple', 'banana']

fruits = ['apple', 'banana']
print("List = ", fruits)

fruits.insert(1, "orange")
print("After Inserting List = ", fruits)

# 5. Remove 'banana' from fruits = ['apple', 'banana', 'grapes']

fruits = ['apple', 'banana', 'grapes']
print("List = ", fruits)

fruits.remove("banana")
print("After Removing List = ", fruits)

# 6. Pop the last element from items = [10, 20, 30] and print the popped value

items = [10, 20, 30]
print("List = ", items)

items.pop(2)
print("After Removing List = ", items)

# 7. Check if 3 is in the list nums = [1, 2, 3, 4].

nums = [1, 2, 3, 4]
print("List = ", nums)

for i in nums:
    if i == 3:
        print(f"There is {i}.")

# 8. Print the slice [2, 3] from the list [0, 1, 2, 3, 4].

lists = [0, 1, 2, 3, 4]
print(f"List is ", lists)
print("Here it is,",lists[2:4])

# 9. Replace the element at index 1 in a = [5, 10, 15] with 12

a = [5, 10, 15]
print("List = ", a)

a[1] = 12
print("List = ", a)

# 10. Count how many times 2 appears in [1, 2, 2, 3, 2].

a = [1, 2, 2, 3, 2]
counts = 0

print("List = ", a)

for count in a:
    if count == 2:
        counts += 1
print(counts)