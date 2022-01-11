import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    paper = [[0] * 10 for _ in range(10)]                   # 빈 도화지 생성(0 = 하얀색)
    result = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())   # 앞에서부터 순서대로 좌표 생성, 마지막엔 무슨 색인지 구분

        for r in range(r1, r2 + 1):                         # 좌표대로 1번은 빨강, 2번은 파랑, 3번은 보라로 구분
            for c in range(c1, c2 + 1):
                if color == 1:                              # 빨강일 때
                    if paper[r][c] == 0:                    # 0(흰색)이면 
                        paper[r][c] = 1                     # 빨강을 칠해주고
                    if paper[r][c] == 2:                    # 2(파랑)이면
                        paper[r][c] = 3                     # 보라(3)으로 칠해주고, result에 1 추가
                        result += 1                         
                if color == 2:                              # 파랑일 때
                    if paper[r][c] == 0:                    # 0(흰색)이면 
                        paper[r][c] = 2                     # 2(파랑)을 칠해주고
                    if paper[r][c] == 1:                    # 2(빨강)이면
                        paper[r][c] = 3                     # 보라(3)으로 칠해주고, result에 1 추가
                        result += 1                         


    print('#{0} {1}'.format(tc+1, result))