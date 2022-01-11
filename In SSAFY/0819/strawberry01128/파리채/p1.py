import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    field = []
    answer = []
    box, che = map(int, input().split())
    print(che)
    for _ in range(box):
        field.append(list(map(int, input().split())))


    for i in range(box-(che -1)): # 0~4 까지
        for j in range(box-(che -1)): # 0~4까지
            sum = 0
            for k in range(che):
                for p in range(che):
                    sum += field[i+p][j+k] #시작점 잡아줌
            answer.append(sum)

    print('#{} {}'.format(tc, max(answer)))