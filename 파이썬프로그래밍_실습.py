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
def fib( n):
    if(n==0):
        return 0
    else if(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


