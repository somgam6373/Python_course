import math as m
a = int(input("이차함의 계수 입력:"))
b = int(input("일차항의 계수 입력:"))
c = int(input("상수항 입력:"))

x = (-b+-m.sqrt(b**2-4*a*c))/2
print(x)


D = b**2 - 4*a*c
if D < 0:
    print("해가 2개")
elif D == 0:
    print("해가 1개")
else:
    print("해가 없음")

n = int(input("각도 입력:"))
print(m.sin(m.radians(n)))