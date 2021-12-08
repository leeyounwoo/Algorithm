n = int(input())

ans = 2
start = 1
flag = 1
while n > start:
    flag += 1
    start += flag
    ans += 1
temp = start - n + 1
if ans % 2:
    print('{}/{}'.format(ans-temp, temp))
else:
    print('{}/{}'.format(temp, ans-temp))
