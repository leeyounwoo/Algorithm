import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)] # 0으로 된 리스트 만들기
    count = 0
    for n in range(N): # 주어진 박스 개수만큼 반복(2, 3,,)
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x2+1): # 그래프를 살펴보니 범위가 0~x2까지라,,
            for j in range(y2+1):
                # 상자 범위 안이고 칸이 칠해져있지않을때 색깔입혀주기
                if x2 >= i >= x1 and y2 >= j >= y1 and arr[i][j] == 0:
                    arr[i][j] = color
                # 상자 범위 안이고 칸이 칠해져있으면서 내 색깔일때 패스
                elif x2 >= i >= x1 and y2 >= j >= y1 and arr[i][j] != 0 and arr[i][j] == color:#같은색
                    continue
                # 상자 범위 안이고 칸이 칠해져있으면서 남의 색깔일때 하나체크하고 패스
                elif x2 >= i >= x1 and y2 >= j >= y1 and arr[i][j] != 0 and arr[i][j] != color: #다른색
                    count += 1
                    continue
    print('#{} {}'.format(tc, count))

