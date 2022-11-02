import random

strike = 0
ball = 0
out = 0
USER_score = 0
PC_score = 0

print("=====start baseballgame=====")
select = input("choice attack or defend:")

if(select == 'a' or select == 'A'):
    print('1회초/Hitter')   
    while(True):
        PC_Picher = random.randrange(0,9)
        print(PC_Picher)
        Hit = int(input("스윙할 위치를 선택하시오(0~9):"))
            
        if(Hit == PC_Picher):
            USER_score += 1
            strike = 0
            ball = 0
            print("HOMERUN!! %d점"%USER_score)
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
            break
elif(select == 'd' or select == 'D'):
    print('1회초/Picher')
    print("123\n456\n789") 
    while(True):
        Picher = int(input("던질 위치를 선택하시오(0~9):"))
        PC_Hitter = random.randrange(1,9)
        if(Picher == PC_Hitter):
            PC_score += 1 
            strike = 0
            ball = 0
            print(PC_Hitter)
            print("HOMRUN!! %d점"%PC_score)
        elif(Picher == 0):
            ball += 1
            print
        else:
            strike += 1
            print(PC_Hitter)
            print("strike!! %d스타라이크"%strike)
        if(strike == 3):
            out += 1
            strike += 0
            ball = 0
            print("out %d아웃"%out)
        if(out == 3):
            break
