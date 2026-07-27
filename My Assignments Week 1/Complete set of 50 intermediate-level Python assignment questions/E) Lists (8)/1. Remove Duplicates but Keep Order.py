# 1. Remove Duplicates but Keep Order
listed = [1,2,3,3,3,4,4,5]
listed_dic = list(dict.fromkeys(listed))
print(listed_dic)