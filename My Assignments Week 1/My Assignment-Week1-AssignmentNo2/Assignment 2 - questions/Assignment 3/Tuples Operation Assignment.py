# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number. The program takes a range and creates a list of tuples within that range with the first element as the number and the second element as the square of the number. 

low = int(input("Enter lower range: "))
high = int(input("Enter high range: "))
tuple_list = [(x, x*x) for x in range(low,high + 1)]

print(f"Tuple list: {tuple_list}")

# Python Program to Remove All Tuples in a List Outside the Given Range. The program removes all tuples in a list of tuples with the USN outside the given range.

lists = [("MS01", "ALI"),("MS02", "ALI"),("MS03", "Azan")]
low = int(input("Min Roll: "))
high = int(input("Max Roll: "))
result = [i for i in lists if low <= int(i[0][2:]) <= high]

print(result)