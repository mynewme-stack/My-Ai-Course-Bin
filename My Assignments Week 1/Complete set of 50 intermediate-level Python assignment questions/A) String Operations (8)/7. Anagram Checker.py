# 7. Anagram Checker Ignoring Spaces/Punct/Case
a1 = input("Enter first word: ")
a2 = input("Enter second word: ")

a1 = a1.lower()
a2 = a2.lower()

clean1= []
clean2=[]

for i in a1.split():
    if i.isalpha():
        clean1.append(i)
        
for j in a2.split():
    if j.isalpha():
        clean2.append(j)

if sorted(clean1)==sorted(clean2):
    print("Anagrams.")
else:
    print("Not Anagrams.")