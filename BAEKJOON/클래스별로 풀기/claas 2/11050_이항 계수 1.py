n, k = map(int, input().split())
check = [[1] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i):
        check[i][j] = check[i-1][j-1] + check[i-1][j]
print(check[n][k])