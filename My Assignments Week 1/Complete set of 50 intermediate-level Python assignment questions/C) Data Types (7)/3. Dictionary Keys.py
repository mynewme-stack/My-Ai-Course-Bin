# 3. Dictionary Keys: Hashability Rules
dic = {'alphabet':1,23:2,(1,2):324}
print('Valid key hash', hash((1,2)))
try:
    bad = {[1,2]:'list'}
except TypeError as e:
    print('Error:',e)
try: 
    hash((1,[2,3]))
except TypeError as m:
    print('Tuple Error:', m)