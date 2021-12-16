n = int(input())

ans = -1
cnt_5, rest_5 = divmod(n, 5)
if rest_5 == 3:
    ans = cnt_5 + 1
    # print(cnt_5 + 1)
elif rest_5 == 0:
    ans = cnt_5
    # print(cnt_5)
else:
    if cnt_5 > 0:
        temp = rest_5 + 5
    else:
        temp = n
    while cnt_5 > 0:
        cnt_5 -= 1
        cnt_3, rest_3 = divmod(temp, 3)
        if rest_3 == 0:
            ans = cnt_5 + cnt_3
            break
        temp += 5
    else:
        ans = -1
print(ans)