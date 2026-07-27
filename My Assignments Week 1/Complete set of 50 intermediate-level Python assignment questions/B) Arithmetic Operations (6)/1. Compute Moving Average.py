# 1. Compute Moving Average (Window k)
data = [1,2,3,4,5]
k= 3
moving = []
for i in range(len(data)-k+1):
    chunk = data[i:i+k]        # For moving average
    avg= sum(chunk)/k
    moving.append(avg)
print (moving)