# 1. Split List into Chunks of Size n
data = [1,2,3,4,5,6]
n = 2
chunk = [data[i:i+n] for i in range(0, len(data),n)]
print(chunk)