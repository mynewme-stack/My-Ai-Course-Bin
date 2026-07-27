# Python Program to Check if a String is a Pangram or Not [The program takes a string and checks if it is a pangram or not.

user = str(input("Enter a string: "))
unique = set(char for char in user.lower() if char.isalpha()) 
length = len(unique) 

if length == 26:       
    print("Pangram") 
else:
    print("Not a pangram.")

# Python Program to Replace Every Blank Space with Hyphen in a String

string = "Who is am i ?"      
spliting = string.replace(" ", "-")

print(f"By replacing: {spliting}")

# This is a Python Program to display which letters are in the two strings but not in both.

set1 = set(input("Enter First String: "))
set2 = set(input("Enter Second String: ")) 
both = set1 ^ set2              # intersection between sets

print(f"The characters in both {both}.")

# Python Program to Find the Larger String without using Built-in Functions[The program takes in two strings and display the larger string without using built-in function.

a = input("Enter First String: ") 
b = input("Enter Second String: ")
count1 = sum([1 for char in a])
count2 = sum([1 for char in b])

if count1 > count2:
    print("Fisrt is greater than second.")
elif count1 < count2:
    print("Second is greater than first.")
else:
    print("Both are equal.")

# Python Program to Count Number of Uppercase and Lowercase Letters in a String

strings = input("Enter a string: ")
upper_count = sum([1 for char in strings if char.isupper()])
lower_count = sum([1 for char in strings if char.islower()])

print(f"Upper case letters are: {upper_count}")
print(f"Lower case letters are: {lower_count}")

# Python Program to Check if Two Strings are Anagram.

str_1 = input("Enter First String: ")
str_2 = input("Enter Second String: ")
low_1 = sorted(str_1.lower())
low_2 = sorted(str_2.lower())

if low_1 == low_2:
    print("Anagrams")
else:
    print("Not Anagrams")

# Python Program to Check if the Substring is Present in the Given String. 

string1 = "gang is back"
sub = "gang"

if sub in string1:
    print("Substing is present.")
else:
    print("Substing is not present.")

# Python Program to Print All Permutations of a String in Lexicographic Order without Recursion. The problem is the display all permutations of a string in lexicographic or dictionary order

number = [1,2,3]
length = len(number)
print(f"Sorted: {number}")

while True:
    i = length - 2
    while i >= 0 and number[i] >= number[i + 1]:
        i -= 1
    if i < 0:
        break
    j = length - 1
    while number[j] <= number[i]:
        j -= 1
    number[i], number[j] = number[j], number[i]
    number[i + 1:] = reversed(number[i + 1:])
    print(f"Sorted: {number}")

# Python Program to Calculate the Length of a String Without using Library Functions

string = "Hello"
count6 = 0

for i in string:
    count6+=1

print(f"Length of string is {count6}.")

# Python Program to Create a New String Made up of First and Last 2 Characters. The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string

aabcc = "ABDUL RABB"
aa = aabcc[0:2:]
cc = aabcc[-2:]

print(f"FIRST TWO CHARACTERS AND LAST TWO CHARACTERS FROM ORIGINAL STRING ARE :{aa},{cc}")