# 1. Count Vowels & Consonants.Count vowels and consonants (letters only; ignore digits/punctuation)..o Input: "Hello, World! 123" → Output: Vowels: 3, Consonants: 7.Hint: Iterate characters; check ch.isalpha(); membership test like ch.lower() in "aeiou".

user = "Hello, World"
vowels = "AEIOUaeiou"
vowel_count = 0                      # Count vowels 
constant = 0                          # Count Constants

for i in user:                   
    if i.isalpha():                    # Separate alphabets
        if i in vowels:                # if i in alphabets is in vowels 
         vowel_count += 1                
        else:                   
            constant += 1       # If not a vowel than a constant

print(f"Vowels: {vowel_count} \n Constants: {constant}")

# 2. Palindrome Check (Ignore Case & Non-alphanumerics)/Determine if a string is a palindrome ignoring case and non-alphanumeric characters..o Input: "A man, a plan, a canal: Panama!" → Output: True/Hint: Normalize with ''.join(ch.lower() for ch in s if ch.isalnum()); compare to.its reverse.

user =  "A man, a plan, a canal: Panama!"
clean = ""

for i in user: 
   if i.isalnum():                      # Separate alphabets and numbers
        clean += i.lower()              # Makes every single alphabet lower in case
reverse = clean[::-1]                # Reversed

if clean == reverse:                        # Alphabets in order is equal to reverse in order
    print(True)
else:
    print(False)

# 3. Title Case (Manual).Convert a sentence to title case without using .title().o Input: "hELLO wORLD from PYTHON" → Output: "Hello World From Python".Hint: Split into words; for each word: word[0].upper() + word[1:].lower().(guard empty words)

words = "hELLO wORLD from PYTHON"                
split_words = words.split()      

title = []                                    # Variable to store Uppercase letter

for i in split_words:                     
    fix = i[0].upper() + i[1:].lower()
    print(title.append(fix))

print(" ".join(title))                       

# 4. Find All Indices of a Substring (Allow Overlaps)/Return a list of starting indices where a substring occurs./o Input: s="aaaa", sub="aa" → Output: [0, 1, 2].Hint: Loop i from 0 to len(s) - len(sub); compare slices s[i:i+len(sub)]

string = "aaaaa"
sub_string = "aa"
indices = []                                      # Variable to store 

for i in range(len(string) - len(sub_string) + 1):
    parts = string[i:i+len(sub_string)]
    if sub_string == parts:
        indices.append(i)

print(indices)

# 5. Character Frequency Dictionary:Build a frequency dictionary for characters (case-insensitive, skip spaces).o Input: "Baa Baa Black Sheep"o Output (order may vary): {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1}Hint: Iterate for ch in s.lower(): and if ch != ' ': then count with a dict;dict.get(ch, 0)+=1.

variable = input("Enter String: ").lower()
freq_dict = {}

for i in set(variable):                 # Using Loop to print every character 
    if i != " ":
        freq_dict[i] = variable.count(i)
print(freq_dict)

# 6. Anagram Checker,Check if two strings are anagrams (ignore spaces, punctuation, and case).o Input: "Listen", "Silent" → Output: Tr/ue//Hint: Normalize to letters with ch.isalpha() and lower(), then comparesorted(s1) vs sorted(s2) or frequency dicts.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

clean1 = []
clean2 = []

for i in string1:
    if i.isalpha():
        clean1.append(i.lower())
for i in string2:
    if i.isalpha():
        clean2.append(i.lower())
if sorted(clean1) == sorted(clean2):
    print(True)
else:
    print(False)

# 7. Compress Repeated Characters (RLE-lite)Compress runs of the same character as <char><count>.o Input: "aaabbcaaaa" → Output: "a3b2c1a4"Hint: Track current char and run length; flush when char changes or at theend.

s = input("Enter a string to compress (e.g., aabcc): ")

if not s:
    print("")
else:
    compressed = []
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1 
    compressed.append(s[-1] + str(count))
    final_string = "".join(compressed)
    print(final_string)

# 8. Longest Word in a SentenceFind the longest word; if multiple, return the first. Consider words as alphabeticsequences.o Input: "Find the longest_word here!" → Output: "longest"Hint: Filter to letters using ''.join(ch for ch in token if ch.isalpha()); track maxby length.

sentence = input("Enter a sentence: ")
tokens = sentence.split() 
longest_word = ""  

for token in tokens:
    clean_word = ''.join(ch for ch in token if ch.isalpha())
    if len(clean_word) > len(longest_word):
        longest_word = clean_word

print(longest_word)

# 9. Remove Duplicate Characters but Keep OrderRemove duplicates while preserving the first occurrence order.o Input: "banana" → Output: "ban"Hint: Maintain a seen set; build result by adding chars not in seen.

s = input("Enter a string: ")
seen = set()
result = []

for ch in s:
    if ch not in seen:
        result.append(ch) 
        seen.add(ch)       
final_string = "".join(result)

print(final_string)

# 10. Mask Email Username.Mask all but the first and last character of the username with *; keep domain intact.o Input: "john.doe@example.com" → Output: "j******e@example.com"Hint: Split on '@'; for the left part, if length ≥ 2, keep first and last andreplace middle with '*' * (len-2); if shorter, handle edge cases.email = input("Enter email: ")

email = input("Enter email: ")
username, domain = email.split('@')

if len(username) >= 2:
    masked_username = username[0] + "*" * (len(username) - 2) + username[-1]
else:
    masked_username = username
final_email = masked_username + "@" + domain 

print(final_email)