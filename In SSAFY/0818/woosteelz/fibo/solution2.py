# with Memozation

def fibo_memo(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-2] + f[i-1])


    return f[n]

print(fibo_memo(50))