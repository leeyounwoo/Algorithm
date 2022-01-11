# memoization을 활용한 피보나치
# 재귀 함수
memo = [0, 1]

def fibo1(n):
    if n >=2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

print(fibo1(7))

# 반복문
def fibo2(n):
    memo = [0, 1]

    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])

    return memo[n]

print(fibo2(7))