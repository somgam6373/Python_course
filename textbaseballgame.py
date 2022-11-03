#1 안타(범위) 및 베이스 구현 => 회의 후 수정
#2 3이닝 구현 and 이닝 카운트
#3 볼 구현

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
            
        if(Hit == PC_Picher):
            USER_score += 1
            strike = 0
            ball = 0
            print("HOMERUN!! %d:%d"%(USER_score,PC_score))
        elif(Hit == 0):
            ball += 1
            print("ball! %d볼"%ball)
        else:
            strike +=1
            print("strike! %d스트라이크"%strike)
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
        
        if(Picher == PC_Hitter):
            PC_score += 1 
            strike = 0
            ball = 0
            print("HOMRUN!! %d:%d"%(PC_score,USER_score))
        elif(Picher == 0):
            ball += 1
            print
        else:
            strike += 1
            print(PC_Hitter)
            print("strike!! %d스트라이크"%strike)
        if(strike == 3):
            out += 1
            strike = 0
            ball = 0
            print("out!! %d아웃"%out)
        if(out == 3):
            print("이닝 종료!! 공수교대!!")
            Hitter(USER_score)

print("=====start baseballgame=====")
select = input("choice attack or defend:")

if(select == 'a' or select == 'A'):
    Hitter(USER_score)
elif(select == 'd' or select == 'D'):
    Picher(USER_score)