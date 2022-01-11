T = 10
for tc in range(1, T + 1):
    _ = input()
    password = list(map(int, input().split()))

    flag = 1
    while flag:
        for i in range(1, 6):
            password.append(password.pop(0) - i)
            if password[-1] <= 0:
                password[-1] = 0
                flag = 0
                break

    result = ' '.join(map(str, password))
    print('#{} {}'.format(tc, result))