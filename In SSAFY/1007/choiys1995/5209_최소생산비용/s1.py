import sys
sys.stdin = open("input.txt")

def cost(idx, total):
    global result
    # 만약 값이 이미 구한 값 초과한다면 종료
    if total >= result:
        return
    # 만약 다 검사를 마쳤다면
    if idx == N:
        # total 값은 결과값 ( 위에서 이미 걸렀기 때문 )
        result = total
        return
    # N만큼 돌면서 x축검사
    for i in range(N):
        # 만약 x의 인덱스가 방문한 적이 없다면
        if not visited[i]:
            # 방문 후 다음 idx값 살펴보고 다시 돌아오는 과정
            visited[i] = 1
            cost(idx+1, total+arr[idx][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 100 * N
    cost(0, 0)

    print("#{} {}".format(tc, result))