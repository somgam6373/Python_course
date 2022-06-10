import numpy as np
A = np.zeros((3,2))
sum = 0
import numpy as np
for i in range(1,4):
    for j in range(1,3):
        A[i-1][j-1] = i+2*j
        sum = sum + A[i-1][j-1]
        print(A)