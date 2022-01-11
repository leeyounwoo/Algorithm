import sys
sys.stdin = open('input.txt')

T = int(input())
#print(T)

for tc in range(3): #테스트 케이스 3번 돌리기
    p = 0           #puple = 0
    board = [[0]*10 for _ in range(10)] # 100칸짜리 보드 만들
    N = int(input())
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())  # 인풋 값 출력
        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                board[r][c] += color
    for r in range(10):
        for c in range(10):
            if board[r][c] == 3:
                p += 1

    print('#{} {}'.format(tc+1, p))