#1 안타(범위) 및 베이스 구현 => 회의 후 수정
#2 3이닝 구현 and 이닝 카운트 => 회의 후 수정 
#3 볼 구현

import random

PC_score = 0
USER_score = 0

def Hitter(USER_score):

    strike = 0
    out = 0
    ball = 0
    base = 0
    PC_score = 0
    
    print('\n1회초/Hitter\n')

    while(True):
        PC_Picher = random.randrange(0,9)
        print(PC_Picher)
        Swing = int(input("타자, 스윙할 위치를 선택하시오(1~9):"))
            
        if(Swing == 0):
            ball += 1
            print("ball!  %dS %dB"%(strike, ball))
        elif(Swing == PC_Picher and Swing != 0):
            USER_score = USER_score + base + 1
            strike = 0
            ball = 0
            base = 0
            print("HOMERUN!! %d:%d"%(USER_score,PC_score))
        else:
            strike +=1
            print("strike!  %dS %dB"%(strike, ball))
       
        if(strike==3):
            out += 1
            strike = 0
            print("out!! %d아웃"%out)
       
        if(ball == 4):
            base += 1
            ball = 0
       
        if(base == 0):
            print("\n    ^    \n<       >\n    -\n")
        elif(base == 1):
            print("\n    ^    \n<       @\n    -\n")
        elif(base == 2):
            print("\n    @    \n<       @\n    -\n")
        elif(base == 3):
            print("\n    @    \n@       @\n    -\n")

        if(out == 3):
            print("\n이닝 종료!! 공수교대!!")
            Picher(USER_score)


def Picher(USER_score):

    strike = 0
    out = 0
    ball = 0
    base = 0
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
            PC_score = PC_score + base + 1 
            strike = 0
            ball = 0
            base = 0
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

        if(ball == 4):
            base += 1           
            ball = 0

        if(base == 0):
            print("\n    ^    \n<       >\n    -\n")
        elif(base == 1):
            print("\n    ^    \n<       @\n    -\n")
        elif(base == 2):
            print("\n    @    \n<       @\n    -\n")
        elif(base == 3):
            print("\n    @    \n@       @\n    -\n")

        if(out == 3):
            print("\n이닝 종료!! 공수교대!!")
            Hitter(USER_score)


print("=====start baseballgame=====")
select = input("choice attack or defend:")

if(select == 'a' or select == 'A'):
    Hitter(USER_score)
elif(select == 'd' or select == 'D'):
    Picher(USER_score)  

'''if ball == 4:
    Hit += 1
   if Hit == 1:
    print("         ^     
           
             <             @
                  
                    -")
    elif Hiit == 2:
        print("")'''
