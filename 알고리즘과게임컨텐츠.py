#1
'''print("삼각형의 세변의 길이를 변c가 가장 길게 입력해주세요.")
a = int(input("변 a의 길이:"))
b = int(input("변 b의 길이:"))
c = int(input("변 c의 길이:"))

if c*c == a*a + b*b:
    print("직각 삼각형입니다.")
else:
    print("직각 삼각형이 아닙니다.")
'''
#2

import turtle

turtle.shape("turtle")
select = int(input("그리고 싶은 도형을 선택하세요 (1.삼각형, 2. 사격형, 3.원) >>>"))

if select == 1:
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)   
    turtle.forward(100)
    turtle.right(120)  

elif select == 2:
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

elif select == 3:
    turtle.circle(50)  

turtle.done()         
