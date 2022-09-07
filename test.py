#1 딕셔너리
'''dic = {"A":['a1','a2','a3'], 'B':['b1','b2']}

for i in range(5):
    num = input(":")
    dic["B"] = ["b1",'b2',num]
    
    for key, value in dic.items():
        if 'b10' in value:
            print(key)'''

#2 중간연계_순환함수(A부터 B까지 더하기)
'''a = int(input(":"))
b = int(input(":"))
def f(a,b):
    if b == 1:
        return 1
    else:
        return a + f(a+1,b-1) 
print(f(a,b)+b-1)'''

#3 지수함수 구하기
'''def f(a,b):
    if b == 1:
        return a
    else:
        return a * f(a,b-1)
print(f(2,1))'''

#4 소수 판별
'''n = int(input(":"))
def f(n):
    for i in range(2,n):
        if n%i != 0:
            return '소수'
        else:
            return 'x'
print(f(n))   '''

#5
'''
a = int(input(":"))
b = int(input(":"))
def f(a,b):
    if b == 1:
        return 1
    else:
        return a + f(a+1,b-1) 
print(f(a,b)+b-1)

#https://seong6496.tistory.com/72
'''
# 입력한 수 이하의 소수를 출력하시오

def f(n):
    list = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            list.append(i)
    return list
print(f(100))



