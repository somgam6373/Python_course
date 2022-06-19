import numpy as np

a = np.array([[1,3,5],[3,2,1]])
b = np.array([[1,-4,7],[-2,5,8],[3,-6,9]])

print(np.dot(a,b))

at = np.transpose(a)

print(np.cross(at,b))