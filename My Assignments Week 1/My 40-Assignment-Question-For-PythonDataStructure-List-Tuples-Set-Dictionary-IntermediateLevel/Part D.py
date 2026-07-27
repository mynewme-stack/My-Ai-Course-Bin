# 1. Count word frequencies in a sentence and store the results in a dictionary.

sentence = "I am the Best the Best"
word1 = sentence.split()

count = {}

for i in word1:
    count[i] = count.get(i, 0) + 1

print(f"Word frequencies: {count}")

# 2. Invert a dictionary where all values are unique

dict_1 = {"A": 1, "B": 2}
dict_2 = {}

new = {value:key for key, value in dict_1.items()}

print(f"New dictionary: {new}.")

# 3. Merge two dictionaries where second dictionary overrides first.

dict_1 = {"A": 1, "B": 2}
dict_2 = {"C": 3, "D": 4}

merge = {**dict_1, **dict_2}

print(f"Merged dictionaries: {merge}")

# 4. Group words by their first letter into a dictionary of lists

words = ["Iron" , "Iphone", "Apple"] 
group = {}

for word in words:
    letter = word[0]
    group.setdefault(letter, [])
    group[letter].append(word)

print(group)

# 5. Filter a dictionary to keep only entries with values greater than 50.

dict_9 = {"A": 50, "B": 60}

great = {key:value for key,value in dict_9.items() if value > 50}
print(f" The value greater than 50 :{great}")

# 6. Given a nested dictionary, safely access a deeply nested key.

a = {
    "A": {"A1": 1},
    "B": {"B1": 2}
}

result_1 = a.get("A",{}).get("A1")
result_2 = a.get("B",{}).get("B1")

print(f"My nested result: {result_1} and {result_2}")

# 7. Write a dictionary comprehension that maps numbers 1–10 to their cubes.

a = {} 

a = sorted({i for i in range(1,11)})
print(a)

a = sorted({i:i**3 for i in range(1,11)})
print(f" The cube of numbers in range of 1 to 10: {a}.")

# 8. Find the key with the highest value in a dictionary.

dict_9 = {"A": 50, "B": 60}
result = max(dict_9, key = dict_9.get)

print(f"The highest number in my dictionary: {result}")

# 9. Combine two lists into a dictionary (keys from first list, values from second).

keys = ["A","B","C"]
nums = [1, 2, 3]
results = dict(zip(keys, nums))

print(f"By combing: {results}")

# 10. Remove all keys from a dictionary whose values are None.

dic1 = {"A":1,
        "B":None,
        "C":3}
remove = {key:value for key, value in dic1.items() if value != None }

print(f"Dictionaries having values: {remove}")