print('온도변환')
print('1. 섭씨 --> 화씨')
print('2. 화씨 --> 섭씨')

while True:

    select = int(input('번호를 입력하시오:'))
    
    if select == 1:
        c = int(input('섭씨 온도를 입력하시오'))
        f = c*9/5 + 32
        print('섭씨',c,'도는','화씨',f,'도 입니다.')
    elif select == 2:
        f = int(input('화씨를 입력하시오'))
        c = 5/9*(f-32)
        print('화씨',f,'도는','섭씨',c,'도 입니다.')    
    else:
        print('다시 입력하시오')
    
    if select == 0:
        print("종료되었습니다.")
        break