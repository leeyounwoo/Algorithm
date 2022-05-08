def solution(atmos):
    cnt = 0
    now = 0
    for i in range(len(atmos)):
        if cnt != 0:
            now += 1
        a, b = atmos[i][0], atmos[i][1]
        if a >= 151 and b >= 76:
            if now <= 2:
                now = 100
            else:
                cnt += 1
                now = 100
        else:
            if a >= 81 or b >= 36:
                if now > 2 or cnt == 0:
                    cnt += 1
                    now = 0

    #     print(a, b, cnt, now)
    # print(cnt)
    return cnt


print(solution([[80, 36]]))