# 1. Check if a value exists in a dictionary

alphabets = {"A":1, "B":2, "c": 3}
print(10 in alphabets.values())   
print(1 in alphabets.values())    
print(2 in alphabets.values())       
print(3 in alphabets.values())       

# 2. Get the key of a minimum value from the following dictionary

alphabets = {"A":1, "B":2, "C": 3}   
minimum = "C"                       # Assume that C is smallest
for i in alphabets:                          
    if alphabets[i] < alphabets[minimum]:          # Each in dictionary is smaller than A
        minimum = i                           # The minimum will be i
print(f'Smallest key is {minimum}')                    

# 3. Delete a list of keys from a dictionary

alphabets = {"A":1, "B":2, "c": 3}
del alphabets["B"]            
print(alphabets)              