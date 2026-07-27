# 1. Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.

lists = [1, 2, 3, 4]
tuples = tuple(lists)

print(tuples)
a, b, c, d = tuples

# 2. Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.

t = (('a', 1), ('b', 2), ('c', 3))
second = [ i[1] for i in t ]

print("List of all second elements is: ",second)

# 3. Write a function that returns multiple values (sum, min, max) using a tuple.

def my_first(numbers):
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, minimum, maximum
a = (10, 20, 30, 40)
total, minimum, maximum = my_first(a)

print("Sum: ", total)
print("Minimum: ", minimum)
print("Maximum: ", maximum)

# 4. Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.

t_1 = (1, 2, 3)
print("First tuple: ", t_1)

t_2 = (4, 5)
print("Second tuple: ", t_2)

result = t_1 + t_2
print("Addition of these two tuples is ", result)

# 5. Given a tuple of numbers, find the element with the highest frequency.

t_1 = (1, 2, 2, 2, 3, 3, 3, 3, 3)
print(t_1)

count = max(t_1, key=t_1.count)
print("The highest frequency number is ",count,".")

# 6. Check if two tuples contain the same elements regardless of order.

t_1 = (1, 2, 3)
t_2 = (3, 2, 1)

if sorted(t_1) == sorted(t_2):
    print("Tuples are equal.")

# 7. Extract the last three items from a tuple using slicing.

t_1 = (0 , 1, 2, 3)
print(t_1)

last = t_1[-3:]
print("Last: ",last)

# 8. Concatenate a tuple with itself three times (repeat operation).

t_1 = (0 , 1, 2, 3)
print(t_1)

concate = t_1*3
print(f"Concatenation: {concate}.")

# 9. Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).

t_1 = ((1,2),(3,4))
flat_tuple = tuple([ab for an in t_1 for ab in an])

print("Flatten Tuple: ",flat_tuple)

# 10. Store coordinates in tuples and calculate the Manhattan distance.

point_a = (1, 2)
point_b = (5, 6)
x_1 , y_1 = point_a
x_2 , y_2 = point_b
first = abs(x_1-x_2)
second = abs(y_1-y_2)
manhattan = first+second

print(f"Manhattan = {manhattan}")