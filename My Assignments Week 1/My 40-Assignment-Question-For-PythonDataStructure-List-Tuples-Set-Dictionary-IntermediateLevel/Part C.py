# 1. Given two sets, find elements that are in the first set but not the second.

set_A = {"A", "B", "C", "D"}
print(f"Set A: {set_A}")

set_B = {"E", "F", "G", "H"}
print(f"Set B: {set_B}")

result1 = set_A - set_B
print(f"Elements which are first set but not in second: {result1}")

# 2. Find common items between three sets using intersection

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {5, 3, 6}
result = set_1 & set_2 & set_3

print(f"Intersection: {result}")

# 3. Given a sentence, return all unique words in lowercase.

string = "I am Unstoppable"
result2 = string.lower().split()
setting = set(result2)

print("Unique words = ",setting)

# 4. Convert a list with duplicates into a set, then back to a sorted list

set_1 = [1, 2, 3, 3, 3]
store = sorted(set(set_1))

print(store)

# 5. Check if one set is a strict subset of another.

set_1 = {1, 2, 3}
set_2 = {3}

if set_2 < set_1 :
    print("Strict subsets.")
else: 
    print('No subsets.')

# 6. Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.

set_5 = {}
set_5 = {i**2 for i in range(1,16) if i % 3 == 0}

print(f"Set: {set_5}")

# 7. Count how many duplicate values exist in a list using sets.

set_1 = [1, 3, 3, 3, 3]
length = len(set_1) 
length2 = len(set(set_1))
duplicate = length - length2

print(f"Duplicates are {duplicate}.")

# 8. Write a program to remove all vowels from a string using a set.

sets = {"a","v","e","b","c","i","o","u"}
vowel = {"a","e","i","o","u","A","E","I","O","U"}
consonant = [i for i in sets if i not in vowel]

print(f"Consonant = {consonant}")

# 9. Find the symmetric difference between two sets

set_6 = {1, 2, 3}
set_7 = {3, 4, 5}
result5 = set_6 ^ set_7

print(f"Result {result5}")

# 10. Check if two strings are anagrams using set comparison (unique characters only).

string1 = "Iron"
string2 = "Nori"
string3 = string1.lower()
string4 = string2.lower()

if set(string3) == set(string4):
    print("Anagrams")