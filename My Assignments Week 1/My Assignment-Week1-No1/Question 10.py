#Salary Calculator,Input basic salary. Calculate:, HRA = 20% of basic, DA = 15% of basic, Total Salary = Basic + HRA + DA

basic_salary = float(input("Enter Basic Salary: "))               

house_rent_allowance = (basic_salary * 20)/ 100                   

dearness_allowance = (basic_salary* 15)/ 100                       

total = basic_salary + house_rent_allowance + dearness_allowance   

print(f"Total Salary = {total}")                                   
