                                    # Input

while True:
        roll_no = int(input("Enter Student Roll no: "))
        if  roll_no > 100:
            print("Enter Correct Roll Number.")
            continue
            
        name = input("Enter Student Name: ")
        st_class = int(input("Enter Student Class: "))
        if st_class != 10:
            print("This Program is for only 10th Class Students. Your class result is still processing.... ")
        
        
        
        marks1 = int(input("Enter Marks in Physics: "))
        if marks1 >= 100:
            print("Enter Correct Marks!!!")
        else: 
             input("Press Enter to Proceed: ")
             
        marks2 = int(input("Enter Marks in Chemistry: "))
        if marks2 >= 100:
            print("Enter Correct Marks!!!")
        else: 
            input("Press Enter to Proceed: ")
            
        marks3 = int(input("Enter Marks in Computer: "))

        if marks3 >= 100:
            print("Enter Correct Marks!!!")
    
#_________________________________________________________________________________________________

                                    # Processing
        marks = marks1 + marks2 + marks3
        total_marks = 300
        percentage = (marks / total_marks) * 100
#_________________________________________________________________________________________________

                                    # Output

        print("\t\t\t\t\t\t\t Student Result")
        print("Student Name: " +name)
        print(f"Student Class: {st_class}" )
        print(f"Student Roll no: {roll_no}")
        print("________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("\n")
        print(f"Physics: \t\t{marks1}")
        print(f"Chemistry: \t\t{marks2}")
        print(f"Computer: \t\t{marks3}")
        print(f"Marks Gained: {marks}")
        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage}%")
    #_________________________________________________________________________________________________
                                    # Percentage
        if percentage > 90:
            print("Execellent!")
        elif percentage > 80:
            print("KEEP IT UP!")
        elif percentage > 70:
            print("VERY GOOD!")
        elif percentage > 40:
            print("YOU ARE DOING VERY GREAT.")
        else:
            print("You can do it, Try again. You can do anything. Just be PRESENT and let that result be the PAST and LEARN from it")
    
        print("_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

#________________________________________________________________________________________________________
        again = input("Another student? Yes/No: ")
        if again != "Yes":
                 break
