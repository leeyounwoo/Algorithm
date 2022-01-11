# 일반적인 재귀 형태의 피보나치
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(7))

def fibo_memo(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]
print(fibo_memo(50))
