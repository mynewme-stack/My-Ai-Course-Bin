# Total Marks and Percentage. Input marks of 5 subjects. Print: Total marks, Percentage, Average

subject1 = float(input("Enter Marks in First Subject: "))            
subject2 = float(input("Enter Marks in Second Subject: "))           
subject3 = float(input("Enter Marks in Third Subject: "))            
subject4 = float(input("Enter Marks in Fourth Subject: "))           
subject5 = float(input("Enter Marks in Fifth Subject: "))            
total_marks = float(input("Enter Total Marks: ")) 

marks_gained = subject1 + subject2 + subject3 + subject4 + subject5  

percentage = (marks_gained/total_marks ) * 100                       

average = (subject1 + subject2 + subject3 + subject4 + subject5)/ 5  

print(f"{marks_gained} Out of {total_marks}.")                       
print(f"Average Marks: {average}")                                 
print(f"Percentage: {percentage}%")                                

