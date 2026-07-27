# 1. Reverse the tuple

my_tuple = (10, 20, 30, 40, 50)
print(f'Original: {my_tuple}')  
print(f'Reversed: {my_tuple[::-1]}')               # Reversed

# 2. Access value 20 from the tuple

my_tuple = (10, 20, 30, 40, 50)     # Tuple
print(my_tuple[1])                   # Accessing element

# 3. Swap two tuples in Python

my_tuple = (10, 20, 30, 40, 50)     # Tuple 1
his_tuple = (60, 70, 80, 90, 100)     # Tuple 2

print("My tuple is: " , my_tuple)      # Tuple 1
print("His tuple is: ", his_tuple)     # Tuple 2

my_tuple, his_tuple = his_tuple, my_tuple

print("\n\n\tAfter Swapping")
print("My tuple is: " , my_tuple)       # Tuple 2
print("His tuple is: ", his_tuple)      # Tuple 1