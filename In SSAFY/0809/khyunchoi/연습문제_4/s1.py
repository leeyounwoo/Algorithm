import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    arr = list(map(int, input()))
    check_list = [0] * 12

    for i in arr:
        check_list[i] += 1

    i = 0
    run, triplet = 0, 0
    while i < 10:
        if check_list[i] >= 3:
            check_list[i] -= 3
            triplet += 1
            continue

        if check_list[i] >= 1 and check_list[i+1] >= 1 and check_list[i+2] >= 1:
            check_list[i] -= 1
            check_list[i+1] -= 1
            check_list[i+2] -= 1
            run += 1
            continue

        i += 1

    if run + triplet == 2:
        print('Baby gin!')
    else:
        print('Nope!')