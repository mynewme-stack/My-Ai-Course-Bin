#Distribute Items Equally - You have n candies and k students.Write a program to find:how many candies each student gets,how many are left

students = int(input("Enter Number of Students: "))  
candies = int(input("Enter Number of Candies: "))    
if candies >= students: 
    distribution = candies // students                   
    left = candies % students                              
    print(f"Each Student will get {distribution} Candies.")
    print(f"{left} Candies are Left.")
else: 
    print('Enter valid amount of candies and students.')