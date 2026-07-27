# 1. Immutable Coordinates with Tuples
import math
p1,p2 = (1,2),(4,5)
distance = math.hypot(p2[0]-p1[0],p2[1]-p1[1])
print(f'The distance between (1,2) and (4,5) is {distance}.')