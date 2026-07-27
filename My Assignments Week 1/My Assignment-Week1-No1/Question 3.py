#Calculate Compound Interest, Use the formula: CI = P * (1 + R/100)**T - P ,Where P = principal, R = rate, T = time

principal = float(input("Enter Principal: "))                 
rate = float(input("Enter Rate: "))                           
time = float(input("Enter Time: "))                           
compound_interest = principal*(1+rate/100)**time - principal  
print(f"Compound Interest = {compound_interest}")             