# 6. Longest Word and Its Frequency
import re
text = 'The quick brown fox jumps over the lazy dog!'
words = re.findall(r'[A-Za-z]+', text)
if not words:
    maxs, count = 0, 0
else:
    lenghts = [len(w) for w in words]
    maxs = max(lenghts)

    count = lenghts.count(maxs)
print(f'Longest length: {maxs}, Occurance: {count}')