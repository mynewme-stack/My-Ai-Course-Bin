# 1. Write a program to create a new string made of an input string’s first, middle, and last character.

variable = str(input("Enter String: "))
length = len(variable)                 
a = variable[0]                         # First
b = variable[length//2]                 # Second
c = variable[-1]                        # Third

print(f'{a+b+c}')                            

# 2. Write a program to count occurrences of all characters within a string Given.

variable = str(input("Enter String: "))
for i in set(variable):                 
    print(f"{i} : {variable.count(i)}") 
    
#3. Reverse a given string

variable = str(input("Enter String: ")) 
print(f'Original: {variable}')
print(f'Reversed: {variable[::-1]}')      # Output reversed

# 4. Split a string on hyphens

variable = str(input("Enter String: ")) 
print(variable.split("-"))              

# 5. Remove special symbols / punctuation from a string

variable = str(input("Enter String: ")) 
store = ""
for i in variable:
    if i.isalpha():                # Checks if a character or symbol and store it in store
        store += i
print(store)                      