#2 -> 10
'''
def f(n):
    if n == 1:
        return 1
    elif 
'''

x = '1100'
y = 0
for i in range(-len(x),0,1):
    y += int(x[i])*2**(-i-1)
print(y)