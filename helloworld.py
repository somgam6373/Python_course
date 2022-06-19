#1(3분반)
'''
def exp(a,b):
    if b > 0:
        return a * exp(a,b-1)
    else:
        return 1


a = int(input("밑수 입력:"))
b = int(input("지수 입력:"))
print("%d의 %d승은"%(a,b),exp(a,b))
'''

#2(3분반)
'''
def f(n):
    if n < 0:
        return '0'
    elif n == 1:
        return '1'
    if (n%2==0):
        return f(int(n/2)) #+ '0'
    elif n % 2 == 1:
        return f(int(n/2)) #+ '1'
n = int(input(":"))
print(f(n))
'''

#3(3분반)

def f(a,b):
    if a == 2:
        return '3 5 7 11 13'
    for i in range(2,a):
        if a%i != 0:
            return 
        else:


    

    
a = int(input("a 입력:"))
b = int(input("b 입력:"))
print("%d보다 큰 %d개의 가장 작은 소수:"%(a,b),f(a,b))