                                           # Input from User

rob = str(input("Enter Robot Name: "))
eng = str(input("Enter Engineer Name: "))
rob_version = float(input("Enter Robot Version: "))
voltage = float(input("Enter Voltage: "))
resistance = float(input("Enter Resistance: "))
battery_capacity = int(input("Enter Battery Capacity: "))

#__________________________________________________________________________________________________________________
                                            # Calculations

current = voltage / resistance
power = voltage * current
battery_life = battery_capacity / ( current * 1000 )
efficiency = ( power / voltage ) * 100

#__________________________________________________________________________________________________________________
                                            # System Check up

if (power >= 100):
    print("Warning: Overload!!!")
else:
    print("Battery is Fine.")

#__________________________________________________________________________________________________________________
                                            # Printing Output

print("_______________________________________________________________________________________________________________________________________________________________________________________________")                                            
      
print("Robot Name: " +rob)
print("Engineer Name: " +eng)
print("Robot Version: "+str(rob_version))
print("\nResults: ")
print("Voltage: " +str(voltage) + "V")
print("Resistance: " +str(resistance) + "R")
print("Current: " +str(current) + "A")
print("Power Consumed: "+str(power) + "W")
print("Battery Capacity: " +str(battery_capacity) +"mAh")
print("Battery Life: " +str(battery_life) +"hours")
print("Efficiency Rating: " +str(efficiency) +"%")

#_____________________________________________________________
                   
                   # Battery Health

if (battery_life < 2):
    print("\n\n\n                                Warning: Low Battery Life!!!")
    
else:
    print("\n\n\n                                Battery is very Healthy.")
    

#_____________________________________________________________

                    # System Condition

if (power <= 100):
    print("\n\n\n                                Your system is in the Best Condition!!")
    
else :
    
      print("\n\n\n                                Please Check Robot IMMEDIATELY!!!!!")
    
   

#_____________________________________________________________

if (battery_life <=2 and power >= 100):
    print("WARNING: CRITICAL CONDITION!!!")
else:
    print("                                                                                      ")
    


#_______________________________________________________________________________________________________________
                       
                                        # Components of Robot

robot_components =["Monitor","Sensor","Controller","Battery","Transmitter",]
for i in robot_components:
    print(i)

print("__________________________________________________________________________________________________________________________________________________________________________________________")

#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________