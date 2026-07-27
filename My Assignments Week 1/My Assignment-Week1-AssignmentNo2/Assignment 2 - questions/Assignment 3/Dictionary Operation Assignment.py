# Python Program to Check if a Key Exists in a Dictionary or Not[This is a Python Program to check if a given key exists in a dictionary or not.]

dictionary = {"A":1,"B":2,"C":3}
search = str(input("Enter key: "))

if search in dictionary:
    print(f"It is in dictionary. Its value is {dictionary[search]}")      # Part of dictionary or not
else:
    print("Not present.")

#  Python Program to Add a Key-Value Pair to the Dictionary. The program takes a key-value pair and adds it to the dictionary.

dictionary = {"A":1,"B":2,"C":3}
keys = input("Enter key: ") 
value = int(input("Enter Value: "))
dictionary[keys] = value    # user stored key and value

print(f"Updated dictionary: {dictionary}.")

# Python Program to Find the Sum of All the Items in a Dictionary The program takes a dictionary and prints the sum of all the items in the dictionary.

dictionary = {"A":1,"B":2,"C":3}
summ = sum(dictionary.values())
print(f"Sum of dictionary: {summ}.")

# Python Program to Multiply All the Items in a Dictionary.

dictionary = {"A":1,"B":2,"C":3}
result = 1
for value in dictionary.values():
    result*= value
print(f"Multiplication: {result}")

summ = sum(dictionary.values())
print(f"Sum of dictionary: {summ}.")

# Python Program to Create Dictionary that Contains Number. The program takes a number from the user and generates a dictionary that contains numbers (between 1 and n) in the form (x,x*x).

number = int(input("Enter number: "))
square_dict = {x: x * x for x in range(1, number + 1)} #calculating value till the user number

print(f"Square dictionary: {square_dict}")

# Python Program to Concatenate Two Dictionaries. The program takes two dictionaries and concatenates them into one dictionary.

dictionary1 = {"A":1,"B":2,"C":3}
dictionary2 = {"D":5,"E":4,"F":6}

concate = dictionary1 | dictionary2     # union

print(f"Concatenation: {concate}")