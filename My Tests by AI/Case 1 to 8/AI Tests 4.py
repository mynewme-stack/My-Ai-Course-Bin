 #__________________________________________________________________________________________________________________
                                        # Input 
name = str(input("Enter Player Name: "))
runs = int(input("Enter Player Runs: "))
balls = int(input("Enter Total Played Balls: "))
matches = int(input("Enter Total Matches Played: "))
wickets = int(input("Enter Total Wickets: "))
centuries = int(input("Enter Centuries: "))
half_centuries = int(input("Enter Half Centuries: "))

 #____________________________________________________________________________________________________________________
                                        # Calculations 

average = runs / wickets
percentage = centuries / matches

#____________________________________________________________________________________________________________________
                                        # Output

print("\n\nPlayer Name is " +name)
print("Player Total Runs = "+str(runs))
print("Player Balls = "+str(balls))             
print("Player Matches = "+str(matches))
print("Player Wickets = "+str(wickets))
print("Player Centuries = "+str(centuries))
print("Player Half Centuries = "+str(half_centuries))
print("\n\n\nPlayer Average = "+str(average))
print("Player Percentage = "+str(percentage))

#____________________________________________________________________________________________________________________