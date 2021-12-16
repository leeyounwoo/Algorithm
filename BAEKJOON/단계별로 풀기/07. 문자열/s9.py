s = input()
flag = 0
ans = 0
for i in range(len(s)):
    # 앞의 문자가 c인 경우
    if flag == 1:
        if s[i] == '=':
            flag = 0
            continue
        elif s[i] == '-':
            flag = 0
            continue
        else:
            flag = 0
    # 앞의 문자가 n인 경우
    elif flag == 4:
        if s[i] == 'j':
            flag = 0
            continue
        else:
            flag = 0

    # 앞의 문자가 s인 경우
    elif flag == 5:
        if s[i] == '=':
            flag = 0
            continue
        else:
            flag = 0

    # 앞의 문자가 z인 경우
    elif flag == 6:
        if s[i] == '=':
            flag = 0
            continue
        else:
            flag = 0

    # 앞의 문자가 d인 경우
    elif flag == 2:
        if s[i] == 'z':
            ans += 1
            flag = 22
        elif s[i] == '-':
            flag = 0
            continue
        else:
            flag = 0

    # 앞의 문자가 dz인 경우
    elif flag == 22:
        if s[i] == '=':
            flag = 0
            ans -= 2
        else:
            flag = 0

    # 앞의 문자가 l인 경우
    elif flag == 3:
        if s[i] == 'j':
            flag = 0
            continue
        else:
            flag = 0

    if flag == 0:
        if s[i] == 'c':
            flag = 1
        elif s[i] == 'd':
            flag = 2
        elif s[i] == 'l':
            flag = 3
        elif s[i] == 'n':
            flag = 4
        elif s[i] == 's':
            flag = 5
        elif s[i] == 'z':
            flag = 6
        ans += 1
print(ans)