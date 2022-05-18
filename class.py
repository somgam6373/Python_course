#1부터 n이하까지 홀수 덧셈
n = int(input("양의 정수 n을 입력하시오:"))
i = 0
k = n - 1
if n % 2 == 1:
    while 0 < n:
        i = i + n
        n = n - 2
    print(i)
elif n % 2 == 0:
    while 0 < k: 
        i = i + k
        k = k - 2
    print(i)

#회문 - while
word = str(input("문자입력:"))
len = len(word)
i = 0
while (True):
    if word[i] != word[-i - 1]:
        print("False")
        break
    else:
        print("True")
        break

# 문자열 거꾸로 출력 - for
word = str(input("문자열 입력:"))
len = len(word)
for i in range(-1, -len-1, -1):
    print(word[i], end='')

# 회문 - for
word = str(input("문자열 입력:"))
len = len(word)
for i in range(0,len+1):
    if word[i] == word[-i-1]:
        print("회문")
        break
    else:
        print("mot 회문")
        break

#2진수 10진수로 출력
n = int(input("2진수로 입력하시오:"))
reversed_n = n[::-1]
len_of_n = len(n)
result = 0
i = 0

while True:
    i-=1
    k = reversed_n[i]
    result = result + int(k) * (2 ** i)
    if i == -1:
        break
print(result)

# 10진수를 2진수로 변환 - while
x = int(input("십진수 숫자 입력:"))
y = ''
while x > 0:
    y = str(x%2) + y
    x//=2
print(y::-1)

# x값을 나눈 나머지가 먼저 와야 하므로 x//=2 보다 y = str(x%2) + y 식이 먼저 나왔다. 그리고 x값을 y에게 계속 할당해야 하기 때문에 x//=2 라는 식이 나왔다.
# 문자로 나열해야 하기 때문에 int(x%2) 가 아닌 str(x%2)를 써야한다.'''

# 2진수를 10진수로 변환 - while
x = str(input("2진수 숫자 입력:"))
y = 0
len = len(x)
while len > 0:
    len -= 1
    y += (int(x[-len-1]) * 2**(len))

print(y) 

# 2진수를 10진수로 변환 - for
x = str(input("2진수 입력:"))
len = len(x)
y = 0
for i in range(-len,0,1):
    y += int(x[i])*2**(-i-1)
print(y)