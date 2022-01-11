import sys
sys.stdin = open('input.txt')
# 100 * 100 들어오고, 가로 세로 다 확인해서
# 가장 긴 회문의 길이를 구하래
# 이걸 어떻게 구해;;
T = 10
for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]  # 100 * 100

    # row
    max_len_r = -1  # palindrome 최댓값 구해줘
    for i in range(100):  # row
        for j in range(100, 0, -1):  # 회문 1에서 M(palindrome의 길이)
            for k in range(100 - j + 1):
                # 회문 검사
                cnt = 0
                for l in range(j // 2):
                    if arr[i][k + l] == arr[i][j + k - l - 1]:
                        cnt += 1       # 기러기는오는기러기
                    if cnt == j // 2:  # palindrome!!
                        if j > max_len_r:
                            max_len_r = j  # pal들 중 최대

    # column - 정사각형이니까 위치만 바꿔주면 돼
    max_len_c = -1
    for i in range(100):
        for j in range(100, 0, -1):
            for k in range(100 - j + 1):
                cnt = 0
                for l in range(j // 2):
                    if arr[k + l][i] == arr[j + k - l - 1][i]: # 여기만
                        cnt += 1
                    if cnt == j // 2:
                        if j > max_len_c:
                            max_len_c = j

    if max_len_r > max_len_c:
        result = max_len_r
    else:
        result = max_len_c
    print('#{} {}'.format(tc, result))
