# Count Word Frequencies
import re
text =  "Apple banana apple cherry banana apple"
word = re.findall(r'\w+',text.casefold())
freq = {}
for i in word:
    freq[i] = freq.get(i,0)+1
print(f'Frequency of word: {freq}')