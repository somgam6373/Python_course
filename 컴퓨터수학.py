a = int(input("검사하려는 수를 입력하시오:"))

def IS_PNum(a):
    if(len(str(a)) == 1):
        if((a == 2) or (a == 3) or (a == 5) or (a ==7)):
            return("소수입니다.")
        else:
            return("소수가 아닙니다.")
    if(len(str(a)) >= 2):
        if((a % 2 == 0) or (a % 3 == 0) or (a % 5 == 0) or (a % 7 == 0)):
            return("소수가 아닙니다.")
        else:
            return("소수입니다.")
print(IS_PNum(a))
b = int(input("수를 입력:"))

def Print_PNum (a , b): 
    list = []
    while(True):  
        result = IS_PNum(a)  
        if(result == '소수입니다.'):
            list.append(a)
        if(len(list) > b):
            break
        a += 1
    return(list)

print(Print_PNum(a , b))