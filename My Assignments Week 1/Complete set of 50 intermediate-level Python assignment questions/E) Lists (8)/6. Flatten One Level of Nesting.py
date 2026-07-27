# 1. Flatten One Level of Nesting
nest_lst = [[2,3,4],[6,7,8,9]]
flat = [j for i in nest_lst for j in i]
print(flat)