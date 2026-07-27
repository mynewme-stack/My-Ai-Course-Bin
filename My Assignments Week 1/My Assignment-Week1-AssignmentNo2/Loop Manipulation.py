# 1. Print first 10 natural numbers using while

number = 1            
a= []

while number <= 10:   
    a.append(number)     
    number += 1       
print(f'First 10 natural number: {a}')              # made a list for easy reading

# 2. Take Input from user , and print even number till that input number

user_number = int(input("Enter Number: "))   
number = 1                                    
c = []

while number <= user_number:             
    if number % 2 == 0:                 
        c.append(number)              
    number += 1                    
print(f'Even numbers till input number: {c}')        # for cleaner dislay

# 3. Take Input from user , and print odd number till that input number

user_number = int(input("Enter Number: "))  
number = 1                                  
d = []

while number <= user_number:         
    if number % 2 != 0:            
        d.append(number)              
    number += 1                    
print(f'Odd numbers till input number: {d}')

# 4. Take Input from user , and print prime number till that input number

user_number = int(input("Enter Number: ")) 
number = 2                            
while number <= user_number:    
    prime = True                           # Takes every number as prime 
    i = 2                
    while i < number:                # It runs till i is less than number
        if number % i == 0:         # If divides completely number is not prime
            prime = False      
        i += 1                  # Checks next number if divisible by number variable
    if prime:                            # And if prime
        print(number)          
    number += 1                

# 5 Print multiplication table of a given number

user_number = int(input("Enter Number: "))    
number = 1                                  
while number <= 10:                                         
    print(f"{user_number} * {number} = ", user_number * number) 
    number += 1  