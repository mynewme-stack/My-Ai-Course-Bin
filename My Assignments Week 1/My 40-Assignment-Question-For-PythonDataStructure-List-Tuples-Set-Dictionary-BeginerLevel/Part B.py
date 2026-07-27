# 1. Create a tuple t = (10, 20, 30) and print the second element.

t = (10, 20, 30)
print(t[1])

# 2. Find the length of tuple ('a', 'b', 'c').

tuplen = ('a', 'b', 'c')
length = len(tuplen)

print(f"Length of tuple is {length}.")

# 3. Unpack the tuple (4, 5) into variables x and y.

tuplen = (4, 5)
x , y = tuplen

print("Now tuple in x and y : ",x,y)

# 4. Check if 'b' is in the tuple ('a', 'b', 'c').

tuplen = ('a', 'b', 'c')

for i in tuplen:
    if i == "b":
        print("b is present.")

# 5. Create an empty tuple and print its type

tuplen = ()

print(type(tuplen))

# 6. Concatenate (1, 2) and (3, 4) into a new tuple.

a = (1, 2)
b = (3, 4)

print(a)
print(b)
print("Adding: ", a + b)

# 7. Repeat (7,) three times.

a = (7,) 
print(a)
result = a * 3
print("Result = ",result)

# 8. Find the index of 2 in (1, 2, 3, 2).

a = (1, 2, 3, 2)
b = a.index(2)

print("Index is ", b)

# 9. Count how many times 2 appears in (1, 2, 3, 2)

a = (1, 2, 3, 2)
count = 0 

for i in a:
    if i == 2:
        count += 1

print(f"{count}x times it appears.")

# 10. Create a single‑ element tuple containing the value 5.

tuplen = (5,)
print("Tuple is ", tuplen)