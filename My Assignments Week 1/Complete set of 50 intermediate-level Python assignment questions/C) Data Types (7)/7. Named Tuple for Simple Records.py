# 7. Named Tuple for Simple Records
from collections import namedtuple
student = namedtuple('student',['name','score'])
s = student('abdul', [90,87,67])
aver = sum(s.score)/len(s.score)
print(f'{s.name} average: {aver}')
s_update = s._replace(name='rabb')