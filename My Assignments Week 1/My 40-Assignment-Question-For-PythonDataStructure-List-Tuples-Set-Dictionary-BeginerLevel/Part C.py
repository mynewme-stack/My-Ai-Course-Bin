# 1. Create a set from [1, 2, 2, 3] and print it.

a = {1, 2, 2, 3}
print(a)

# 2. Add element 4 to the set {1, 2, 3}

sets = {1, 2, 3}
print("Set = ",sets)

sets.add(4)
print("After adding = ",sets)

# 3. Remove element 2 from the set {1, 2, 3}.

sets = {1, 2, 3}
print("Set = ",sets)

sets.remove(2)
print("After removing = ",sets)

# 4. Check if 5 is in the set {1, 3, 5}

sets = {1, 3, 5}

for i in sets:
    if i == 5:
        print("5 is present.")

# 5. Find the length of set {10, 20, 30}

sets = {10, 20, 30}
length = len(sets)

print(f"Length of set is {length}.")

# 6. Clear all elements from the set {1, 2, 3}

sets = {1, 2, 3}

print("Set is ",sets)
print(sets.clear())

# 7. Create a set {'a', 'b'} and add 'c' only if it’s missing

a = {'a', 'b'} 

if 'c' not in a:
    a.add("c")

print(a)

# 8. Convert list ['a', 'a', 'b'] into a set to remove duplicates

listn = ['a', 'a', 'b']
sets = set(listn)

print("List = ", sets)

# 9. Create two sets and print their union.

a = {1, 2, 3}
b = {4, 5, 6}

c = a | b

print("Union of sets = ",c)

# 10. Create two sets and print their intersection

a = {1, 2, 3}
b = {3, 4, 5}
c = a & b

print("Intersection of sets = ",c)
