# 31. Compare two numbers entered by the user and print if the first is greater than the second.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))     

if a > b:      
    print("First Number is Greater than Second Number.")
else:
    print("First number is less than second.")

# 32. Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result

number = int(input("Enter a Number: "))
print(number % 2 == 0)     

# 33. Write a program that checks if a number is between 10 and 50 (inclusive) using and .

number = int(input("Enter a Number: "))

if ( number >= 10 and number <= 50):     
    print("Yes")
else:
    print("You entered wrong number.")    

# 34. Check if a string entered by the user is equal to "Python"

user = str(input("Enter a String: ")) 
value = "Python"

if user == value:              
    print("Equal.")
else:    
    print("Entered string is not equal to (Python).")

# 35. Use the or operator to check if a user is either "Admin" or "Superuser".

user = str(input("Enter a your position: "))

if (user=="Admin" or user=="Superuser"): 
    print("Yes")
else:
    print("User is neither admin nor superuser")

# 36. Demonstrate the not operator by reversing a Boolean variable.

user = True 
user = not user 
print(user)

# 37. Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result.

print(0.1 + 0.2 == 0.3) 
print("It will show false because '==' checks if both are equal and = assign is used for assigning a value.")

# 38. Take a user's age and check if they are NOT under 18.

age = int(input("Enter Your Age: "))

if age >= 18:                         
    print("Not under 18.")
else:
    print("Under 18")

# 39. Check if a number is positive and odd using logical operators.

number = int(input("Enter a Number: "))

if (number > 0 and number % 2 != 0):          
    print("Number is Positive and Odd.")
else:
    print("Either number is not positve or even.")

# 40. Compare the lengths of two strings provided by the user.

string1 = str(input("Enter a String: "))
string2 = str(input("Enter a String: "))
length1 = len(string1)
length2 = len(string2)                           

if length1 > length2:                            
    print("First string is Greater in Length.")  
elif length1 < length2:                          
    print("First string is Smaller in Length.")  
elif length1 == length2:                         
    print("Both strings are Equal in Length.")