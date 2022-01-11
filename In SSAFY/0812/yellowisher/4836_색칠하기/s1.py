import sys
sys.stdin = open('input.txt')

T = int(input()) # ( 1 ≤ T ≤ 50 )

for tc in range(T):
    N = int(input()) # ( 2 ≤ N ≤ 30 )
    arr = [[0] * 10 for _ in range(10)] # 배열 초기화
    purple_count = 0 # 보라색 카운트 변수

    for i in range(N):
        r1, c1, r2, c2, color = map(int, (input().split())) # ( 0 ≤ r1, c1, r2,  2 ≤ 9 )

        for j in range(r1, r2 + 1): # x축
            for k in range(c1, c2 + 1): # y축
                if arr[j][k] == 0:  # 배열이 비어있으면
                    if color == 1:
                        arr[j][k] = 1 # 빨간색은 1로
                    else:
                        arr[j][k] = 2 # 파란색은 2로
                else:
                    # arr[j][k] = 3
                    purple_count += 1  # 1도 아니고 2도 아니면 count

    print("#%d %d" % (tc + 1, purple_count))