import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 사용 중인 복도를 표시할 리스트
    corridor = [0] * 200

    # 학생들의 방 위치를 복도를 기준으로 바꾸어서 카운팅
    '''
    stu_room 1 3 5 7 ... 399
    corridor 0 1 2 3 ... 199
    stu_room 2 4 6 8 ... 400
    '''
    for n in range(N):
        temp = list(map(int, input().split()))
        for i in range(2):
            if temp[i] % 2:
                temp[i] = (temp[i] - 1) // 2
            else:
                temp[i] = (temp[i] - 2) // 2

        if temp[0] <= temp[1]:
            for j in range(temp[0], temp[1]+1):
                corridor[j] += 1
        else:
            for j in range(temp[1], temp[0]+1):
                corridor[j] += 1

    # 가장 많이 카운팅된 수를 출력하면, 그 복도를 동시에 사용할 수 없는 횟수이기 때문에 정답

    print('#{} {}'.format(t, max(corridor)))