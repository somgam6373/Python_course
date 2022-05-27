#np.dot : 내적
#np.cross : 외적

import numpy as np
a = np.array([1,-1,1])
b = np.array([1,3,6])
c = np.array([2,-5,3])

first = a+b
first_1 = np.dot(first,c)
print("(a+b)c =",first_1)

second = np.dot(a,c)+np.dot(b,c)
print("ac+bc =",second)

import sympy as sp
k = 10
third = np.dot(k*a,b)
print("(ka)b",third)

forth = k*(np.dot(a,b))
print("k(ab)",forth)

fifth = np.dot(a,k*b)
print("a(kb)",fifth)
