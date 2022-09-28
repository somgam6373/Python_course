'''

money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환할 돈은 얼마?:"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n 500원짜리 ==> %d개" % c500)
print(" 100원짜리 ==> %d개" % c100)
print(" 50원짜리 ==> %d개" % c50)
print(" 10원짜리 ==> %d개" % c10)
print(" 바꾸지 못한 잔동 ==> %d원" % money)

'''

sel = int(input("입력진수 결정(16/10/8/2):"))
num = input("값 입력:")

if sel == 16:
    num10 = int(num, 16)
if sel == 10:
    num10 = int(num, 10)
if sel == 8:
    num10 = int(num, 8)
if sel == 2:
    num10 = int(num, 2)

print("16진수 ==>", hex(num10))
print("10진수 ==>", num10)
print("8진수 ==>", oct(num10))
print("2진수 ==>", bin(num10))