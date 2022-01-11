import sys
sys.stdin = open('input.txt')

def magnetic(lst):
    global cnt
    # 1 : N극 / 2: S극
    # N극 테이블 S극

    # 자기장을 걸었을 경우 이동 : 1 -> +1 / 2 <- -1
    # 만약, 해당 라인의 왼쪽 끝에만 자석이 하나 있을 경우가 최대 이동 횟수 : 100
    for _ in range(100):
        for i in range(100):
            if lst[i] == 1:
                # 오른쪽 칸에 아무 것도 없을 경우 오른쪽 칸으로 이동
                if i+1 < 100 and lst[i+1] == 0:
                    lst[i] = 0
                    lst[i+1] = 1
                # 오른쪽 칸이 인덱스를 넘어갈 경우 테이블 밑으로 떨어짐
                elif i+1 == 100:
                    lst[i] = 0

            elif lst[i] == 2:
                # 왼쪽 칸에 아무 것도 없을 경우 왼쪽 칸으로 이동
                if i-1 > -1 and lst[i-1] == 0:
                    lst[i] = 0
                    lst[i-1] = 2
                # 왼쪽 칸이 인덱스를 넘어갈 경우 테이블 밑으로 떨어짐
                elif i+1 == -1:
                    lst[i] = 0

    # 이동을 완료한 후, 한 번 더 순회하며 교착 상태 카운트
    for j in range(100):
        # 보통의 경우 1의 오른쪽에 2가 있으면 교착 상태
        if j < 99 and lst[j] == 1:
            if lst[j+1] == 2:
                cnt += 1

        # 만약 1이 오른쪽끝에 있고, 2가 1의 왼쪽에 있고
        # 해당하는 2의 왼쪽에 1이 없을 경우 -> 교착
        elif j == 99:
            if lst[j-1] == 2 and lst[j-2] != 1:
                cnt += 1


for t in range(1, 11):
    N = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 전치행렬 : N극 테이블 S극
    for i in range(100):
        for j in range(100):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    cnt = 0
    for row in arr:
        magnetic(row)

    print('#{} {}'.format(t, cnt))