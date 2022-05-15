# int, float, str
# 아스키코환
# ord(아스키코드를 10진수로 변환), bin(10진수를 2진수로 변환)
# string, index
# [n:m] n은 포함하고 m은 제외(n부터 m-n개)

#========================================

num_1 = int(input("첫번째 양의 정수를 입력하시오:"))
num_2 = int(input("두번째 양의 정수를 입력하시오:"))
num_3 = int(input("세번째 양의 정수를 입력하시오:"))

total_num = num_1 + num_2 + num_3

if total_num % 2 == 0:
    
    if num_1 < num_2 < num_3:
        print(num_3)
    elif num_1 < num_3 < num_2:
        print(num_2)
    elif num_2 < num_1 < num_3:
        print(num_3)
    elif num_2 < num_3 < num_1:
        print(num_1)
    elif num_3 < num_2 < num_1:
        print(num_1)
    else:
        print(num_2)

else:
    print(total_num)
