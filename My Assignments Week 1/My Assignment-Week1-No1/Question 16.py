#Calculate Body Mass Index (BMI),Input weight (kg) and height (m), then calculate:,BMI = weight / (height ** 2)

weight = float(input("Enter Weight in kg: "))
height = float(input("Enter Height in m: "))

bmi =  weight / (height ** 2)               

print(f"BMI is {bmi}")                   