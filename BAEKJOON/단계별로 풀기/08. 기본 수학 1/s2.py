n = int(input())

ans = 1
start = 1
flag = 6
while start < n:
    start += flag
    flag += 6
    ans += 1
print(ans)
