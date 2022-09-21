#합 구하기 for문
'''n = int(input("n을 입력하세요:"))
s = 0

for i in range(1, n+1):
    s = s + i
print(s)
'''
#합 구하기 가우스 방정식
'''
n = int(input(":"))
s = 0
s = n * (n+1)//2
print(s)
'''

'''#성능분석(1)
import time
n = int(input("n을 입력하시오:"))

start = time.time()
s = 0
for i in range(1, n+1):
    s = s + 1
end = time.time()
print(s, end-start)
'''

'''
#성능분석(2)
import time
n = int(input("n을 입력하시오:"))
start = time.time()
s = 0
s = n * (n+1)//2
end = time.time()
print(s, end-start)
'''


#tutle

import turtle

turtle.title("거북이 사각형 그리기")
turtle.shape("turtle")

angle = 72
dist = 72

turtle.forward(dist)
turtle.right(angle)
turtle.forward(dist)
turtle.right(dist)
turtle.forward(dist)
turtle.right(angle)
turtle.forward(dist)
turtle.right(angle)
turtle.forward(dist)
turtle.right(angle)

turtle.done()
