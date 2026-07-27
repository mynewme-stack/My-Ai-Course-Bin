# 11. Create an integer variable age and a float variable height. Print their types.

age = 18           
height = 5.4       
print(type(age))   
print(type(height))  

# 12. Store the value 3 + 4j in a variable. Print the variable and its type.

value = complex(3 + 4j)     
print(value, type(value)) 

# 13. Create a boolean variable is_python_fun and set it to True.

is_python_fun = True     
print(is_python_fun)       

# 14. Method 1: Assign three different values to three variables in a single line

a, b, c = 1, 2, 3    

# 15. Method 2: Assign the same value to three different variables in a single line

a = b = c = 1          

# 16. Take a numeric input from a user and convert it to a float.

number = int(input("Enter Integer: ")) 
number = float(number)    
print(number, ':',type(number))      

#17. Take a string input "100" and convert it to an int.

value = int(input("Enter 100:\n "))
if value == 100:
    number1 = int(value)
    print(type(number1))    
else:
    print("You didn't enter 100.")

# 18. Create a variable with a complex number and print only its real part.

value = 4 + 9j
print(f'Real part of {value} is {value.real}.')      

# 19. Define a string variable containing a paragraph and print its length.

paragraph = """The year was 2147. Humanity had long since ceded control of its daily functions to artificial
intelligence. Cities operated like clockwork, transportation was seamless, and even emotions
could be regulated by neural implants. But deep beneath the surface of Neo-Tokyo, in a forgotten
data vault, something ancient stirred."""

print(f'The length of given paragrapgh is {len(paragraph)}.')

# 20. Swap the values of two variables a and b without using a third variable.

a = 1
b = 2
print(f'Before swaping, \na = {a}\nb = {b}')
a, b = b, a              
print(f'After swaping values,\na = {a}\nb = {b}')