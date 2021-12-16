ans = 0
n = int(input())
for i in range(1, n+1):
    now = str(i)
    if len(now) <= 2:
        ans += 1
    else:
        flag_1 = int(now[0]) - int(now[1])
        flag_2 = int(now[1]) - int(now[2])
        if flag_1 == flag_2:
            ans += 1
print(ans)

