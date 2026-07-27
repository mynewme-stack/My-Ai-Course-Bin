# 1. Create a dictionary {'name': 'Ali', 'age': 25} and print the name.

dictionary = {'name': 'Ali', 'age': 25}

print(dictionary['name'])

# 2. Add key 'city': 'Lahore' to a dictionary.

dictionary = {'name': 'Ali', 'age': 25}
dictionary.update({'city': 'Lahore'})

print("Updated dictionary = ", dictionary)

# 3. Change 'age' in {'name': 'Ali', 'age': 25} to 30

dictionary =  {'name': 'Ali', 'age': 25, 'city': 'Lahore'}
dictionary.update({'age': 30})

print("Updated dictionary: ", dictionary)

# 4. Delete key 'age' from a dictionary.

dictionary =  {'name': 'Ali', 'age': 25, 'city': 'Lahore'}
dictionary.pop('age')

print("After deleting dictionary: ", dictionary)

# 5. Check if key 'salary' exists in a dictionary

dictionary =  {'name': 'Ali', 'age': 25, 'city': 'Lahore'}

if 'salary' in dictionary:
    print("Yes")
else:
    print("No")

# 6. Print all keys from {'a': 1, 'b': 2}.

a = {'a': 1, 'b': 2}
print(a.keys())

# 7. Print all values from a dictionary.

a = {'a': 1, 'b': 2}
print(a.values())

# 8. Iterate and print key‑ value pairs from {'x': 10, 'y': 20}

a = {'x': 10, 'y': 20}

for i in a:
    print(i, a[i])

# 9. Use get() to safely read key 'score' from an empty dictionary.

a = {}
result = a.get('score')

print(result)

# 10. Create a dictionary from two lists: keys = ['a','b'], values = [1,2].

keys = ['a','b']
values = [1,2]

c = dict(zip(keys,values))
print(c)