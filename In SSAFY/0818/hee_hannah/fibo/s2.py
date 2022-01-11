#메모이제이션을 이용한 피보나치

def fibo_meno(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-1])
    return f[n]

print(fibo_meno(50))  # O(N) 시간복잡도