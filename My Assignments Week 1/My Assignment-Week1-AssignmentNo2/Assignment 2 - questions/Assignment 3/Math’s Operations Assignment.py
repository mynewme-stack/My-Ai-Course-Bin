# Python Program to Find the Area of a Triangle

breadth = float(input("Enter base in meters: "))
length = float(input("Enter height in meters: "))
area = (1 / 2) * breadth * length

print(f"The area of this triangle is {area}m\u00b2.")

# Python Program to Find Quotient and Remainder of Two Numbers

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
quotient = num1 // num2
remainder = num1 % num2

print(f"The quotient is {quotient} and remainder is {remainder}.")

# Python Program to Print an Identity Matrix 

size = int(input("Enter size of matrix: "))
for row in range(size):
    for column in range(size):
        if row == column:
            print(1, end=" ")
        else:
            print(0, end=" ")
print()

# Python Program to Find the LCM of Two Numbers 

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))

if num1 > num2:
    great = num1
else: 
    great = num2
while True:
    if great % num1 == 0 and great % num2 == 0:
        lcm = great
        break
    great += 1

print(f"LCM of {num1} and {num2} is {lcm}.")

# Python Program to Find the Sum of Natural Numbers

limit = int(input("Enter the limit: "))
total = 0

if limit > 0:
    for i in range(1, limit +1):
        print(i, i + 1)
        total += i
    print(f"Sum is {total}.")
else:
    print("Only positive numbers.")

#  Python Program to Check If Two Numbers are Amicable Numbers or Not

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
sum1 = 0

for i in range(1,num1):
    if num1 % i == 0:
        sum1 += i
sum2 = 0

for i in range(1, num2):
    if num2 % i == 0:
        sum2 += i
if sum1 == num2 and sum2 == num1:
    print("Ammicable.")
else:
    print("Not Ammicable.")

# Python Program to Find All Perfect Squares in the Given Range.

num1 = int(input("Enter lower range: ")) 
num2 = int(input("Enter upper range: "))
perfect_square = []
numb = 1

while numb **2 <= num2:
    square = numb**2
    if square >= num1:
        perfect_square.append(square)
    numb += 1
    
print(f'Perfect squares: {perfect_square}')

#  Python Program to Check Armstrong Number

number = int(input("Enter number: "))
number_str = str(number)
number_digit = len(number_str)
armstrong = 0

for digs in number_str:
    armstrong += int(digs) ** number_digit
if armstrong == number:
    print("ARMSTRONG NUMBER.")
else: 
    print("Not armstrong.")