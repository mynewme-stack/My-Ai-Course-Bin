# This is a Python Program to find the largest number in a list. The program takes a list and prints the largest number in the list

number = [1,2,3,4,5]
largest = max(number)
print(f"Largest in list is {largest}.")

# The program takes a list and prints the largest number in the list. The program takes a list and prints the second largest number in the list.

number = [1,2,3,4,5]
great = number[0]       # let greates is 0
sec_great = number[0]       # let second greates is 0
for i in number:
    if i > great:          # if element in list are greater than 0
        sec_great = great     # second great = 0
        great = i                    # and great = all numbers
    elif i > great and i != great:    # great is > than great and number not equal to great 
        sec_great = i         # second great that number
print(f"Largest number is {great} and second largest is {sec_great}.")

# Python Program to Print Largest Even and Largest Odd Number in a List. The program takes in a list and prints the largest even and largest off number in it. 

number = [1,2,3,4,5]
even = []
odd = []
for i in number:
    if i % 2 == 0:  # even stored
        even.append(i)
    else:
        odd.append(i)  # odd store
max_even = max(even) 
max_odd = max(odd)
print(f"The largest even number is {max_even} and odd {max_odd}.")

# Python Program to Find Average of a List. The program takes the elements of the list one by one and displays the average of the elements of the list.

elements_list = []
total = int(input("Enter the number of elements: "))
for i in range(total):
    element = int(input(f"Enter element {i + 1}: "))
    elements_list.append(element)
avg = sum(elements_list) / total
print(f"Average: {avg}")

# Python Program to Count Occurrences of Element in List. The program takes a number and searches the number of times the particular number occurs in a list.

lists = [1,2,3,4,5,6,7,8,9,0,1,3,4,6,7,6,4,3,6,7,8,7,4,1,1,9,3,5]
numbers = int(input("Enter number which frequecny we want: "))
occurence = lists.count(numbers)  # counting
print(f"The number repeatance: {occurence}. ")

# Python Program to Remove Duplicates from a List. The program takes a lists and removes the duplicate items from the list.

lists = [1,2,3,4,5,6,7,8,9,0,1,3,4,6,7,6,4,3,6,7,8,7,4,1,1,9,3,5]
set_lists = set(lists)          # make set instead cz it has heterogeneous property
print(f"Without duplicate: {set_lists}")

# Python Program to Find the Number Occurring Odd Number of Times in a List. A list is given in which all elements except one element occurs an even number of times. The problem is to find the element that occurs an odd number of times.

lists = [1,1,2,2,3]
odd = 0
for i in lists:
    odd ^= i
print(f"Result: {odd}")

# Python Program to Find the Union of Two Lists. The program takes two lists and finds the unions of the two lists

listt = [1,2,3]
lists = [3,4,5]
listted = list((set(listt) | set(lists)))
print(f"This union of sets = {listted}")

# Python Program to Swap the First and Last Element in a List. Python Program to Swap the First and Last Element in a List

index = [1,2,3,4,5]
index[0], index [4] = index [4], index[0]
print(f"Swapped list = {index}")

#  Python Program to Return the Length of the Longest Word from the List of Words. The program takes a list of words and returns the word with the longest length.

words = ["Water","banana","apple"]
long = max(words, key= len)
length = len(long)
print(f"Length of longest word ({long}) and its length {length}.")

# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List. The program takes in the number of elements and generates random numbers from 1 to 20 and appends them to the list.

import random

num = int(input("Enter number of elements: "))
randoms = [random.randint(0, 20) for _ in range(num)]
print(f"Random elements are: {randoms}")