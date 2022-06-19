x = int(input("십진수 숫자 입력:"))
y = ''
while x > 0:
    y = str(x%2) + y
    x//=2
print(y)
