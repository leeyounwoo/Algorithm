import sys
sys.stdin = open('input.txt')

T = 10  # 총 10개의 테스트케이스

for tc in range(1, T+1):
    num = int(input())
    building = list(map(int, input().split()))

    result_view = 0
    for i in range(2, num-2):   # 맨 왼쪽, 오른쪽 2칸에는 건물이 지어지지 X
                                # 255부터 돌기
        while True:             # 오른쪽, 왼쪽 2개와 비교했을 때 가장 큰 값
            if building[i] > building[i+1] and building[i] > building[i+2] \
                    and building[i] > building[i-1] and building[i] > building[i-2]:
                result_view += 1
                building[i] -= 1  # 세대(층/높이) 차이까지 넣어주기
                                  # 225가 214와 같아질 때까지
            else:
                break
    print('#{0} {1}'.format(tc, result_view))