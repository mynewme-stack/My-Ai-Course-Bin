#Percentage of Correct Answers,Input total questions and correct answers, and calculate the percentage score

correct_answer = int(input("Enter Correct Answer: "))     
total_question = int(input("Enter Total Questions: "))     
percentage: float = (correct_answer/total_question)*100    
print(f"Percentage: {percentage}%")                        
