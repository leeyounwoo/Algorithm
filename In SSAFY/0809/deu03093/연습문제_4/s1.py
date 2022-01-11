import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    n = input()
    ans = 0
    check = [0] * 10
    check_flag = [0] * 10
    i = 0
    while i < len(n):
        if i <= 3:
            now = int(n[i])
            next1 = int(n[i + 1])
            next2 = int(n[i + 2])
            if (now - next1 == 1 and next1 - next2 == 1) or (now - next1 == -1 and next1 - next2 == -1):
                i += 3
                continue
        check[int(n[i])] += 1
        i += 1

    for i in range(len(check)):
        if check[i] % 3 == 0:
            check[i] = 0

    if sum(check) == 0:
        ans = 1
    else:
        ans = 0
    # print(check)
    print('#{} {}'.format(T, ans))
