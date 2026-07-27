# 3. Find and Replace with Whole-Word Matching
import re as r

sentence = "My cat is gre8te and 8te my lunch.."
target = "8te"
replace = "ate"
pattern = r'\b{}\b'.format(r.escape(target))

for match in r.finditer(pattern, sentence, flags = r.IGNORECASE):
    found = match.group(0)
    if found.isupper():
        actual_replace = replace.upper()
    elif found.istitle():
        actual_replace = replace.title()
    else:
        actual_replace = replace.lower()
    sentence = sentence.replace(found, actual_replace ,1)

print(sentence)