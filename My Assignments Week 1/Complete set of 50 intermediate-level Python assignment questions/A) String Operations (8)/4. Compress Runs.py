# 4. Compress Runs (Run-Length Encoding)
inputed = 'aaabbc'
count_great_1 = True
compress = ''                # Alphabets and numbers container
count = 1                     # Number of repeated a b and c

for i in range(len(inputed)):
    if i +1 < len(inputed) and inputed[i] == inputed[i+1]:
        count+=1
    else:
        compress+=inputed[i]
        if not count_great_1 or count>1:
            compress+=str(count)

        count = 1
print('Compressed text:\n',compress)