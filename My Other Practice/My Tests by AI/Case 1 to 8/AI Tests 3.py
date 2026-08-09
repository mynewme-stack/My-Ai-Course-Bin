import sys
print (sys.version)
import math

#_______________________________________________________________________________________________________________
                                            # Worker Input

name = str(input("Enter Worker's Name: "))
age = int(input("Enter Worker's Age: "))                                              
factory_name = str(input("Enter Factory Name: "))
unit = int(input("Enter Untis Produced: "))
price = float(input("Enter Price Per Unit: "))
machine_frequency = complex(10 + 9j)
worker_id = int(931)
worker_id = int(932)

print(type(name))
print(type(age))
print(type(factory_name))
print(type(unit))
print(type(price))
print(type(machine_frequency))
print(type(worker_id))

sqrt = math.sqrt(unit)
total_revenue = unit * price
tax = total_revenue * 0.10
net_revenue = total_revenue + tax
bonus = total_revenue ** 0.05
units_per_day = unit // 7
leftover_units = unit % 7

print(unit == 100)
print(unit != 50)
print(total_revenue > 10000)
print(unit > 50 and price > 100.0)
print(unit < 10 or price < 50.0)
print(not(unit == 0))

#_________________________________________________________________________________________________________________
                                            # Output

print(name)
print(str(age))
print(factory_name)
print(str(unit))
print(str(price))
print(str(machine_frequency))
print(str(worker_id))
print(str(sqrt))
print(str(total_revenue))
print(str(tax))
print(str(net_revenue))
print(str(bonus))
print(str(units_per_day))
print(str(leftover_units))

A =["Production", "Quality Control", "Packaging", "Dispatch"]
for i in A:
    print(i)
B =["Wear helmet", "Check machine", "Log hours"]
for i in B:
    print(i)






















