#except: 예외상황 발생 시 실행되는 명령
#finally: 예외상황이 발생했든 안 했든 마지막 문장 실행

'''def factorial(n):
    if n == 1:
        return(1)
    else:
        return n*factorial(n-1)

n = int(input("정수를 입력하시오."))
print(n, "!=", factorial(n))
'''
'''
def hanoi_tower(n, org, tmp, to):
    if(n==1):
        print("원판 1을",org,"에서",to,"로 옮긴다.")
    else:
        hanoi_tower(n-1,org,to,tmp)
        print("원판", n,"을", org,"에서", to, "로 옮긴다.")
        hanoi_tower(n-1,tmp,org,to)
hanoi_tower(4,"A","B","C")
'''

import numpy as np
import matplotlib.pyplot as plt