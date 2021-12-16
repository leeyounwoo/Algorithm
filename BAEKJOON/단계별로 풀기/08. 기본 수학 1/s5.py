for _ in range(int(input())):
    ans = ''
    height, width, n = map(int, input().split())
    cnt, temp = divmod(n, height)
    # 1호부터 시작
    if temp == 0:
        floor = height
    else:
        cnt += 1
        floor = temp
    ans += str(floor)
    if cnt < 10:
        ans += '0' + str(cnt)
    else:
        ans += str(cnt)
    print(ans)
