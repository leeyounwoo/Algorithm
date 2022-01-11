import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # n개의 상자, q번 동작
    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        for j in range(L - 1, R):
            box[j] = i

    # print("#{}".format(tc+1), end=' ')
    #
    # for i in range(N):
    #     print(box[i], end=' ')
    # print()
    # 성공적으로 출력이 되나 줄일수 있는 방법을 생각해 봄
    print("#{}".format(tc+1), *box)