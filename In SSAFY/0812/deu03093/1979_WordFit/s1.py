import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    arr_size, word_size = map(int, input().split())
    arr = []
    for _ in range(arr_size):
        arr.append(list(map(int, input().split())))

    ans = 0
    for i in range(arr_size):
        # 가로
        count_w = 0
        for j in range(arr_size):
            if arr[i][j]:
                count_w += 1
                # 길이를 증가시켰을 때 원하는 문자의 길이이고 더 이상 공간이 없거나 다음 문자열이 0인 경우
                if count_w == word_size and (j == arr_size - 1 or arr[i][j + 1] == 0):
                    ans += 1
            # 0을 만나면 갯수를 초기화 시켜줌
            else:
                count_w = 0

        # 세로
        count_h = 0
        for j in range(arr_size):
            if arr[j][i]:
                count_h += 1
                # 길이를 증가시켰을 때 원하는 문자의 길이이고 더 이상 공간이 없거나 다음 문자열이 0인 경우
                if count_h == word_size and (j == arr_size - 1 or arr[j + 1][i] == 0):
                    ans += 1
            # 0을 만나면 갯수를 초기화 시켜줌
            else:
                count_h = 0
    print('#{} {}'.format(T, ans))