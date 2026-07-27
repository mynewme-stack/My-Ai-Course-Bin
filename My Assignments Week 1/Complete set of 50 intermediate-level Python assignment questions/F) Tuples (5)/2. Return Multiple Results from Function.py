# 1. Return Multiple Results from Function
def mn_mx_avg(list1):
    if not list1:
        print('Enter correct number.')
     
    mn = min(list1)
    mx = max(list1)
    avg = sum(list1)/ len(list1)
    return mn,mx,avg
list1 = [1,2,3,4,5]
low, high, aver = mn_mx_avg(list1)
print(f'Minimum Value: {low}\nMaximum Value: {high}\nAverage Value: {aver}')