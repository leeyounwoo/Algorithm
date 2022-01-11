import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100x100 2차원배열
    result = 0  ## 최종 결과 값을 저장할 변수로 가장 큰 값만 저장할꺼임
    # 각 행의 합
    for r in range(100):
        sum = 0
        for c in range(100):  # 열 증가하면서 가로로 더한다.
            sum += arr[r][c]  ## r= row행, c = columm 열
        if sum > result:
            result = sum
    # 각 열의 합
    for c in range(100):
        sum = 0
        for r in range(100):
            sum += arr[r][c]
        if sum > result:
            result = sum
    # 대각선 \
    sum = 0
    for i in range(100):
        sum += arr[i][i]  # [i][i] 는 \ 대각선을 나타냄
    if sum > result:
            result = sum
    # 대각선 /
    sum = 0
    for i in range(100):
        sum += arr[100-1-i][i]  # [-1]이 가장 끝 인덱스니깐 / 대각선은 N-1-i 또는 -1-i도 가능
    if sum > result:
            result = sum

    print('#{} {}'.format(T, result))