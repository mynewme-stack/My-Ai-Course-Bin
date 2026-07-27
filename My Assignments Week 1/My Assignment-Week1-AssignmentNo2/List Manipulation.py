# 1. Reverse a list in Python

liked = ["Black",10,0.9,True] 

print(f'Reversed list: {liked[::-1]}')             # Reverse

# 2. Turn every item of a list into its square

numbers = [1,2,3,4,5]
a = []

for i in numbers:
    a.append(i**2)
print(f'Squared: {a}')

# 3. Remove empty strings from the list of strings

string = ["A","","B","C","","D"]
b = []

for i in string: 
    if i != "":                  # Only strings with values can pass
        b.append(i)
print(f'Without any empty string: {b}')

# 4. Add new item to list after a specified item

liked = ["Black",10,0.9,True] 
liked.insert(3, 10000)        

print("List after adding: ", liked)  

# 5. Replace list’s item with new value if found

liked = ["Black",10,0.9,True] 
print("Before Replacement: ", liked)
liked[1] = "Blue"             
liked[2] = "Green"
liked[3] = "Grey"
print("After Replacement: ", liked)   