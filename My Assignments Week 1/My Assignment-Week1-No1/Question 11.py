# Age in Months and Days,Input your age in years. Calculate and print age in:, Months, Days (approximate)

age = int(input("Enter Age: "))     

months = age * 12                   
days = age * 365.25  # For leap year cz (365*4)/4 = 365.25                

print(f"Age in Months: {months}")   
print(f"Age in Days: {int(days)}")       