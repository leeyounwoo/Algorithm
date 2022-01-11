import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    charg_list = list(map(int, input().split()))

    check_list = [0]*(N+1)
    for charg in charg_list:
        check_list[charg] += 1

    error_num = 0
    result_count = 0
    now_location = 0
    while now_location < N:
        now_location += K
        if now_location >= N:
            break
        if check_list[now_location] != 1:
            for back in range(K):
                now_location -= 1
                error_num += 1
                if check_list[now_location] == 1:
                    break
        if error_num == K:
            result_count = 0
            break
        result_count += 1

    print('#{0} {1}'.format(tc+1, result_count))