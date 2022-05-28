import numpy as np
p = np.array([1,-1,1])
q = np.array([1,3,6])
r = np.array([2,-5,3])

pq = q - p
pr = r - p

print(pq)
print(pr)
print(np.cross(pq,pr))