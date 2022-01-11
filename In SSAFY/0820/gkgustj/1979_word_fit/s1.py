import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []

    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    result = []

    # 행 탐색
    for i in range(len(puzzle)):
        cnt = 0
        for j in range(len(puzzle[i])):
            # 1인 칸이면 cnt +1
            if puzzle[i][j]:
                cnt +=1
            # 0인 칸을 만나면 cnt를 result리스트에 넣고 0으로 초기화
            else:
                result.append(cnt)
                cnt = 0
        # 만약 행의 마지막 숫자가 1이라면 cnt가 저장되지 않으므로
        # 행 탐색이 끝난 후 cnt추가 (마지막 숫자가 0이라면 어차피 0)
        result.append(cnt)

    # 열 탐색
    for j in range(len(puzzle[0])):
        cnt = 0
        for i in range(len(puzzle)):
            if puzzle[i][j]:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)

    # result에서 K의 개수 세기
    ans = 0
    for num in result:
        if num == K:
            ans += 1

    print('#{} {}'.format(t, ans))