dic = {"A":['a1','a2','a3'], 'B':['b1','b2']}

for i in range(1):
    num = input(":")
    dic["B"] = ["b1",'b2',num]
    
    if 'b3' in dic['B']:
        print('B`')

def f(n):
    for i in range(2,n):
        if n%i != 2:
            return '소수x'
        return '소수'

def num(a,b):
    list = []
    for i in range(a+1,10000):
        if f(i) == '소수':
            list.append(i)
            print(list[:b])
n = int(input(":"))
print(f(n))
print(num(10,5))'''