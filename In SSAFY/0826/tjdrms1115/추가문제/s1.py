import sys
sys.stdin = open('input.txt')


# 위치가 경계 안에 있는지 확인하는 함수입니다.
def border_check(N, i, j):
    if (0 <= i < N) and (0 <= j < N):
        return True
    return False


# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):

    # 입력값을 입력받습니다.
    N = int(input())
    village = [input() for _ in range(N)]

    # 집의 개수와 집의 위치, 기지국의 위치를 저장할 변수들입니다.
    house_num = 0
    house_check = [[0 for _ in range(N)] for _ in range(N)]
    base_station = []
    # 입력받은 배열을 탐색하면서 집과 기지국을 탐색합니다.
    for i in range(N):
        for j in range(N):
            # 해당 위치가 집이라면 집의 개수를 추가하고 위치를 표시합니다.
            if village[i][j] == 'H':
                house_num += 1
                house_check[i][j] = 1
            # 해당 위치가 기지국이라면 기지국의 정보를 저장합니다.
            elif village[i][j] == 'A':
                temp = {'coord': [i, j], 'level': 1}
                base_station.append(temp)
            elif village[i][j] == 'B':
                temp = {'coord': [i, j], 'level': 2}
                base_station.append(temp)
            elif village[i][j] == 'C':
                temp = {'coord': [i, j], 'level': 3}
                base_station.append(temp)

    # 방향을 알려줄 리스트입니다.
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 기지국 별로 탐색합니다.
    for station in base_station:
        i, j = station['coord']
        for dist in range(1, station['level']+1):
            for di, dj in delta:
                di = di * dist
                dj = dj * dist
                if border_check(N, i+di, j+dj):
                    # 기지국 범위 안에 집이 있다면
                    # 체크하고 전체 집의 개수에서 하나씩 빼줍니다.
                    if house_check[i+di][j+dj] == 1:
                        house_check[i + di][j + dj] = 2
                        house_num -= 1

    # 남은 집의 개수를 출력합니다.
    answer.append(house_num)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
