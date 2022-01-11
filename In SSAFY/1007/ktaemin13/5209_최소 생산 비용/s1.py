import sys
sys.stdin = open('input.txt')

T = int(input())


def min_cost(idx, total):
    global result

    if total >= result:  # 만약 total 값이 이미 구한 result 보다 크다면 종료
        return
    if idx == N:  # idx == N은 검사가 끝난 경우
        result = total
        return
    for i in range(N):  # 열 탐색 시작
        if not visited[i]:  # 방문 하지 않은 경우,
            visited[i] = 1  # 방문 체크
            min_cost(idx + 1, total + arr[idx][i])  # 열 탐색하면서 값을 더함
            visited[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = float('inf')  # 최댓값 설정
    min_cost(0, 0)

    print("#{} {}".format(tc, result))
