# 일반적인 재귀 형태의 피보나치
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

