def solution(dartResult):
    temp = []
    flag = False
    for i in range(len(dartResult)):
        if flag:
            flag = False
            continue
        now = dartResult[i]
        if now == 'S':
            continue
        elif now == 'D':
            temp[-1] **= 2
        elif now == 'T':
            temp[-1] **= 3
        elif now == '*':
            temp[-1] *= 2
            if len(temp) == 1:
                continue
            else:
                temp[-2] *= 2
        elif now == '#':
            temp[-1] *= -1
        elif now == '1':
            if i != len(dartResult) - 1 and dartResult[i+1] == '0':
                temp.append(10)
                flag = True
            else:
                temp.append(int(now))
        else:
            temp.append(int(now))

    answer = sum(temp)

    return answer

print(solution('1D2S#10S'))