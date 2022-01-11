#일반적인 형태의 재귀 피보나치
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)


print(fibo(5))