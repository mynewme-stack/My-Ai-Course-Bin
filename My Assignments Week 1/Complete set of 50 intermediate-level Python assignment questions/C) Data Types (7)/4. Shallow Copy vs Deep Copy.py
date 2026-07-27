# 4. Shallow Copy vs Deep Copy
import copy
original = [[1,2]]
shallow = copy.copy(original)
shallow[0].append(99)
print(f'Shallow Original: {original}')
deep = copy.deepcopy(original)
deep[0].append(99)
print(f'Deep Original:{original}')