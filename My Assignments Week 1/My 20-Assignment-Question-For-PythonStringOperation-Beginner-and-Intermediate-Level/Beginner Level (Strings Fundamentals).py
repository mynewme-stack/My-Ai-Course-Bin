# 1. Length of a String, Write a program that reads a string and prints its length. o Input: "hello world" → Output: 11 Hint: Use len(s).

user = input("Enter a string: ")      
length = len(user)   
print(f"Length: {length}")

# 2. Uppercase & Lowercase, Convert the input string to uppercase and lowercase.,o Input: "Python3" → Output: "PYTHON3", "python3".Hint: Methods: s.upper(), s.lower().

variable = "Python3"

print(variable) 
print(variable.upper())   
print(variable.lower())

# 3. Count a Character, Count how many times a given character appears in a string (case-sensitive)..o Input: "banana", "a" → Output: 3.Hint: Use s.count(ch).

user = input("Enter a string: ")
char = input("Enter character to count: ")

print(user.count(char))       

# 4. First & Last Character.Print the first and last character of a string; handle empty input..o Input: "drawer" → Output: First: d, Last: r.Hint: Check empty with if not s; index via s[0] and s[-1].

user = input("Enter a string: ")

print("First: " , user[0])       
print("Last: " , user[-1])        

# 5. Check Substring Presence,Check if a substring exists in a string.o Input: "data science", "science" → Output: True.Hint: Use the in operator: sub in s.

user = input("Enter a string: ")
check = input("Enter Substring: ")  # part of string

if check in user:   
    print(True)
else:
    print(False)           

# 6. Slice a String. Print a substring from index start to end (exclusive).o Input: "programming", 3, 8 → Output: "gramm".Hint: Use slicing: s[start:end].

user = input("Enter a string: ")         
start = int(input("Starting Index: "))      
end = int(input("Ending Index: "))

print(user[start:end])        

# 7. Reverse a String.Reverse the string..o Input: "Python" → Output: "nohtyP".Hint: Slicing trick: s[::-1].

user = input("Enter a string: ")      
reverse = user[::-1]      # reversed 

print(reverse)

# 8. Replace Substring.Replace all occurrences of a word with another (case-sensitive)..o Input: "I love apples. Apples are great!", "apples", "oranges".o Output: "I love oranges. Apples are great!".Hint: s.replace(old, new) replaces exactly matching cases.

fruit1 = "I love apples. Apples are great!"
print(fruit1)                                 

fruit1 = fruit1.replace("apples","Oranges")  # replaces apples with oranges
print(fruit1)

# 9. Split and Join.Split a sentence on spaces and join with -.o Input: "split this sentence" → Output: "split-this-sentence".Hint: s.split() then "-".join(words).

user = input("Enter a string: ")
user = user.split()           # separate each
print("-" .join(user))      

# 10. Strip Whitespace.Remove leading and trailing spaces.o Input: " padded text " → Output: "padded text".Hint: Use s.strip().

user = "fifth   "
user = user.strip()        # removes spaces in the start and end

print(user)