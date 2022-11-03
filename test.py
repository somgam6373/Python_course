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
'''
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
'''

import random

PC_score = 0
USER_score = 0

def Hitter(USER_score):

    strike = 0
    out = 0
    ball = 0
    PC_score = 0
    
    print('\n1회초/Hitter\n')

    while(True):
        PC_Picher = random.randrange(0,9)
        print(PC_Picher)
        Hit = int(input("타자, 스윙할 위치를 선택하시오(0~9):"))
            
        if(Hit == 0):
            ball += 1
            print("ball!  %dS %dB"%(strike, ball))
        
        elif(Hit == PC_Picher and Hit != 0):
            USER_score += 1
            strike = 0
            ball = 0
            print("HOMERUN!! %d:%d"%(USER_score,PC_score))
        else:
            strike +=1
            print("strike!  %dS %dB"%(strike, ball))
        if(strike==3):
            out += 1
            strike = 0
            print("out!! %d아웃"%out)
        if(out == 3):
            print("\n이닝 종료!! 공수교대!!")
            Picher(USER_score)

def Picher(USER_score):

    strike = 0
    out = 0
    ball = 0
    PC_score = 0

    print('\n1회초/Picher\n')
    print("123\n456\n789\n")    
    while(True):
       
        PC_Hitter = random.randrange(1,9)
        print(PC_Hitter)
        Picher = int(input("타자에게 던질 위치를 선택하시오(0~9):"))
        
        if(Picher == 0):
            ball += 1
            print("ball!  %dS %dB"%(strike, ball))
        elif(Picher ==  PC_Hitter and Picher != 0):
            PC_score += 1 
            strike = 0
            ball = 0
            print("HOMRUN!! %d:%d"%(PC_score,USER_score))
        else:
            strike += 1
            print(PC_Hitter)
            print("strike!  %dS %dB"%(strike, ball))
        if(strike == 3):
            out += 1
            strike = 0
            ball = 0
            print("out!! %d아웃"%out)
        if(out == 3):
            print("\n이닝 종료!! 공수교대!!")
            Hitter(USER_score)

print("=====start baseballgame=====")
select = input("choice attack or defend:")

if(select == 'a' or select == 'A'):
    Hitter(USER_score)
elif(select == 'd' or select == 'D'):
    Picher(USER_score)  


