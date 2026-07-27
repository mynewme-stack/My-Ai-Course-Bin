# 21. Write a program to calculate the area of a rectangle (Length × Width)

length = float(input("Enter Length of Rectangle in meter: "))    
width = float(input("Enter Width of Rectangle in meter: "))      
area = length * width                                   
print(f"Area of Rectangle is {area}m\u00b2.")                   

# 22. Take two numbers and print the result of the first raised to the power of the second (a^b)

number_1 = int(input("Enter First Number: "))
number_2 = int(input("Enter Second Number: "))
number = number_1 ** number_2   
print(f"The first raised to the power of the second (a^b): {number}.")

# 23. Demonstrate the difference between / (division) and // (floor division) with the numbers 10 and 3

a = 10
b = 3
c = a/b                    
print(f"Division: {c}")   
d = a//b                      # giving whole number after division
print(f"Floor Division: {d}")

# 24. Use the modulus operator % to find the remainder when 25 is divided by 4.

remainder = 25 % 4
print(f"Remainder: {remainder}")

# 25. Calculate the average of five numbers entered by the user.

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))
number4 = int(input("Enter Fourth Number: "))
number5 = int(input("Enter Fifth Number: "))
average = (number1 + number2 + number3 + number4 + number5)/ 5
print(f"Average: {average}")

# 26. Create a program that converts minutes into hours and remaining minutes.

minutes = float(input("Enter Minutes: "))                 
hours = minutes//60                           
remaining_minutes = minutes % 60                          
print(f"{hours} hours and {remaining_minutes} minutes.")  

# 27. Calculate the area of a circle where Area = \pi r^2 (Use 3.14 for \pi).
pi = 3.14
radius = float(input("Enter Radius in meter: "))
area = pi * radius**2          
print(f"Area of circle = {area}m\u00b2")

# 28. Find the cube of a number entered by the user.

number = int(input("Enter number: "))
cube = number**3           # number^3
print(cube)

# 29. Perform the calculation 10 + 5 * 2. Does Python follow PEMDAS? Prove it with code.

calculation = 10 + 5 * 2 
print(calculation)
print("Yes, It follows PEMDAS Rule.") 

# 30. Write a program to calculate simple interest: (P \times R \times T) / 100.

principal = float(input("Enter Principal: "))                  
rate = float(input("Enter Rate: "))                            
time = float(input("Enter Time: "))                            
simple_interest = (principal*rate*time) /100  
print(f"Simple Interest = {simple_interest}") 