import sys
sys.stdin = open('input.txt')

def collison(arr, length):
    count = 0
    for i in range(length):
        flag = False
        for j in range(length):
            if not flag: # 1을 만나기 전까지는 False
                if arr[j][i] == 1:
                    flag = True # 1을 만나면 True
            else: # 1을 만난 이후에 2를 만나기 전까지 True
                if arr[j][i] == 2:
                    flag = False # 다시 1을 만날때까지 False
                    count += 1 # 1과 2를 만나게해서 count 증가
    return count

for tc in range(1, 11):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 1은 N극 2는 S극 1은 아래로 2는 위로
    # 남아 있는 교착상태 반환하기

    # 1. 세로로 탐색한다.
    # 2. 제일 위에있는 1부터 탐색하고, 그 밑에 가장 가까운 2를 찾고 그 다음에 1을..

    answer = collison(arr, length)
    print('#{} {}'.format(tc, answer))
