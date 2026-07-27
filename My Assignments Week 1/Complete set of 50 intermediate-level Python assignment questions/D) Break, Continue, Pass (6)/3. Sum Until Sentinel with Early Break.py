#  Sum Until Sentinel with Early Break
data = [10, 20, -999, 40, 30]
total_sum = 0

for num in data:
    if num == -999: # Sentinel
        break
    total_sum += num

print(f'Sum of values before sentinel: {total_sum}.')