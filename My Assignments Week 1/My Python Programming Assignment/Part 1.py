# 1. Write a program to print "Hello, World!" and your name on two separate lines.

print("Hello, World!")    
print("Abdul Rabb")   

# 2. Ask the user for their favorite color using input() and print "Your favorite color is [color]"
 
color = str(input("Enter your Favourite Color: ")) 
print(f"Your Favourite Color is {color}")    

# 3. Use a single print() statement to display three different words separated by a hyphen (-).

word1 = "I"
word2 = "AM"
word3 = "THE"
print(f"{word1}-{word2}-{word3}")  

# 4. Prompt the user for their birth year and print their age (assume the current year is 2026).

user = int(input("Enter Your Birth Year: ")) 
year = 2026
age = 2026 - user                                
print(f"Your Age is {age}.")              

# 5. Print the result of 5 + 5 such that the output is: The sum of 5 and 5 is 10.

print(f"The sum of 5 and 5 is {5+5}")           

# 6. Use the end parameter in print() to join two separate print statements with a space.

print("I am", end =" ")
print("here.")    

# 7. Write a program that takes two strings from the user and prints them joined together.

string1 = str(input("Enter String: "))
string2 = str(input("Enter String: "))   
print(string1+string2)           

# 8. Create a greeting that takes a user's name and prints "Welcome, [Name]!" in all uppercase.

name = str(input("Enter Username: "))
print(f"Welcome, {name.upper()}!")       

# 9. Ask for a user's city and country, then print them in the format: "City, Country".

city = str(input("Enter City: "))
country = str(input("Enter Country: "))
print(f"{city}, {country}")    

# 10. Experiment: What happens if you try to add a string and an integer in a print statement? Write a code snippet that fixes this using str().

name = "Iphone "
model = 18
print("Name is " + name + str(model))     